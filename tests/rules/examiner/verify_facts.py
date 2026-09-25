#!/usr/bin/python
# Filename: verify_facts.py
# Description: Checks a run's database against the E1 exit criteria (PLAN-E1 §4)
# Usage: verify_facts.py <run.s3db> --log <run.log> [--expect-colreg] [--baseline <other.s3db>]

import argparse, os, re, sqlite3, sys
from xml.dom import minidom

import yaml

ROOT		= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..') )
SCHEMA		= os.path.join( ROOT, 'config', 'data', 'maritime.xml' )
ZONES		= os.path.join( ROOT, 'config', 'examiner', 'zones.yaml' )
TERRITORY	= os.path.join( ROOT, 'config', 'simulation', 'tk', 'turkeli', 'risk.yaml' )

RO			= 'fact_concern'
AUDIT		= ['creation_time', 'audit_status', 'case_id']
AUDIT_REGISTER	= 1000
DERIVED		= ('id',)			# Columns the table adds that the schema does not declare

# Log lines that mean a finding was lost or a producer was misconfigured
LOST		= [ 'No such topic', 'schema expects', 'Concern mapping:', 'Scorecard:',
				'maps to no concern', 'Spatial zones:', 'No spatial zones' ]


class Report:
	def __init__(self):
		self.failed	= 0

	def check(self, code, ok, text):
		print( f'  {"PASS" if ok else "FAIL"}  {code:6} {text}' )
		if not ok:
			self.failed	+= 1

	def skip(self, code, text):
		print( f'  SKIP  {code:6} {text}' )

	def info(self, text):
		print( f'        {text}' )


def declared(schema):
	""" Fact table -> declared field names, in order """
	doc		= minidom.parse( schema )
	tables	= {}
	for fact in doc.getElementsByTagName('Fact'):
		table	= fact.getElementsByTagName('TableName')[0].childNodes[0].nodeValue
		tables[table]	= [ m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
							for m in fact.getElementsByTagName('Measure') ]
	return tables


def columns(db, table):
	return [ r[1] for r in db.execute(f'PRAGMA table_info({table})')
			 if (r[1] not in DERIVED) and (not r[1].startswith('dim_')) ]


def count(db, sql, *args):
	return db.execute( sql, args ).fetchone()[0]


def main():
	parser	= argparse.ArgumentParser( description=__doc__ )
	parser.add_argument( 'db', help='The run database, e.g. maritime.workingset.s3db' )
	parser.add_argument( '--log', help='The run log (coslaunch stdout)' )
	parser.add_argument( '--schema', default=SCHEMA )
	parser.add_argument( '--zones', default=ZONES )
	parser.add_argument( '--territory', default=TERRITORY )
	parser.add_argument( '--expect-colreg', action='store_true',
						 help='The run contains a deliberate COLREG breach (E1-X6)' )
	parser.add_argument( '--baseline', help='A run of the same scenario and seed, for E1-X8' )
	args	= parser.parse_args()

	report	= Report()
	db		= sqlite3.connect( f'file:{args.db}?mode=ro', uri=True )
	log		= open( args.log, errors='replace' ).read() if args.log else None
	log		= re.sub( r'\x1b\[[0-9;]*m', '', log ) if log else None

	zones		= yaml.safe_load( open(args.zones) )
	vocabulary	= set( zones['concerns']['vocabulary'] )
	territory	= yaml.safe_load( open(args.territory) )['risk']
	spatial		= set( territory['spatial_zones']['order'] )

	# ---- Schema alignment ---------------------------------------------------
	print( 'Schema' )
	tables	= declared( args.schema )
	present	= { r[0] for r in db.execute("select name from sqlite_master where type='table'") }
	drift	= []
	for table, fields in sorted( tables.items() ):
		if table not in present:
			drift.append( f'{table}: declared, absent from the database' )
		elif columns(db, table) != fields:
			drift.append( f'{table}: declared {fields}, table has {columns(db, table)}' )
		elif fields[:3] != AUDIT:
			drift.append( f'{table}: does not open with {AUDIT}' )

	report.check( 'SCHEMA', not drift, f'{len(tables)} fact tables declared in maritime.xml match the database' )
	for d in drift:
		report.info( d )

	if any( d.startswith(f'{RO}:') for d in drift ):
		print( f'FAILED: {RO} does not match its declaration; nothing further can be read from it' )
		return 1

	if log is not None:
		rejected	= re.findall( r'Failed to push data to topic (\S+): payload has', log )
		report.check( 'ARITY', not rejected,
					  f'no push rejected for payload length'
					  + (f' - rejected: {sorted(set(rejected))}' if rejected else '') )
	else:
		report.skip( 'ARITY', 'no --log' )

	# ---- Row counts ---------------------------------------------------------
	print( 'Rows' )
	written	= {}
	for table in sorted( tables ):
		if table in present:
			n	= count( db, f'select count(*) from {table}' )
			if n:
				written[table]	= n
				report.info( f'{table:32} {n:>8}' )

	# ---- E1 exit criteria ---------------------------------------------------
	print( 'E1 exit criteria' )
	ro		= count( db, f'select count(*) from {RO}' )
	report.check( 'E1-X1', ro > 0, f'{RO} has {ro} rows' )

	rules	= count( db, f"select count(*) from {RO} where source in ('colreg','local')" )
	report.check( 'E1-X2', rules > 0, f'{rules} rule-sourced rows in {RO}' )
	for source, n in db.execute( f'select source, count(*) from {RO} group by source' ):
		report.info( f'{source:10} {n}' )

	ids		= {}
	for table in written:
		for (cid,) in db.execute( f'select distinct case_id from {table}' ):
			ids.setdefault( cid, [] ).append( table )

	kernel	= None
	if log is not None:
		m	= re.search( r'Case id (\d+) for scenario', log )
		kernel	= int( m.group(1) ) if m else None

	ok		= (len(ids) == 1) and (AUDIT_REGISTER not in ids) and ((kernel is None) or (kernel in ids))
	report.check( 'E1-X3', ok, f'case_id {sorted(ids)} in every written table'
				  + (f', kernel says {kernel}' if kernel is not None else ', kernel id not in log') )

	bad_zone	= count( db, f"select count(*) from {RO} where zone is null or zone = '' or zone = 'None'" )
	outside		= [ z for (z,) in db.execute(f'select distinct zone from {RO}') if z not in spatial ]
	bad_concern	= [ c for (c,) in db.execute(f'select distinct concern from {RO}') if c not in vocabulary ]
	report.check( 'E1-X4', not (bad_zone or outside or bad_concern),
				  f'zone and concern drawn from the vocabularies'
				  + (f' - {bad_zone} empty zones' if bad_zone else '')
				  + (f' - zones {outside}' if outside else '')
				  + (f' - concerns {bad_concern}' if bad_concern else '') )

	zero	= count( db, f'select count(*) from {RO} where penalty is null or penalty <= 0' )
	report.check( 'E1-X5', zero == 0, f'{zero} rows with no penalty' )

	colreg	= count( db, f"select count(*) from {RO} where source = 'colreg'" )
	if args.expect_colreg:
		report.check( 'E1-X6', colreg > 0, f'{colreg} COLREG rows' )
	else:
		report.skip( 'E1-X6', f'{colreg} COLREG rows; pass --expect-colreg for a breach run' )

	if log is not None:
		lost	= [ l.strip() for l in log.splitlines() if any(k in l for k in LOST) ]
		report.check( 'E1-X7', not lost, f'{len(lost)} lost-finding or configuration errors in the log' )
		for l in sorted( set(lost) )[:10]:
			report.info( l[:160] )
	else:
		report.skip( 'E1-X7', 'no --log' )

	if args.baseline:
		base	= sqlite3.connect( f'file:{args.baseline}?mode=ro', uri=True )
		mine	= dict( db.execute(f'select source||"/"||event, count(*) from {RO} group by 1') )
		theirs	= dict( base.execute(f'select source||"/"||event, count(*) from {RO} group by 1') )
		report.check( 'E1-X8', mine == theirs, f'{sum(mine.values())} rows here, {sum(theirs.values())} in the baseline' )
		for k in sorted( set(mine) | set(theirs) ):
			if mine.get(k) != theirs.get(k):
				report.info( f'{k}: {mine.get(k, 0)} vs {theirs.get(k, 0)}' )
	else:
		report.skip( 'E1-X8', 'no --baseline' )

	matrix	= db.execute( f'select zone, concern, count(*), sum(penalty) from {RO} '
						  f'group by zone, concern order by zone, concern' ).fetchall()
	report.check( 'E1-X9', len(matrix) > 0, f'Ro is one aggregation over {RO}, {len(matrix)} (zone, concern) cells' )
	for zone, concern, n, total in matrix:
		report.info( f'{zone:20} {concern:14} {n:>6} rows  {total:>12.1f}' )

	# ---- Rb long form (REQ.018) ---------------------------------------------
	print( 'Rb' )
	rb		= count( db, 'select count(*) from fact_rb' )
	if rb == 0:
		report.skip( 'RB-X1', 'fact_rb is empty; nothing to reconcile' )
	else:
		short	= db.execute( 'select report_time, vessel_id, count(distinct concern) from fact_rb '
							  'group by report_time, vessel_id having count(distinct concern) != ?',
							  (len(vocabulary),) ).fetchall()
		report.check( 'RB-X1', not short, f'every sample has a row for each of the {len(vocabulary)} concerns'
					  + (f' - {len(short)} samples short' if short else '') )

		concerns	= { c for (c,) in db.execute('select distinct concern from fact_rb') }
		zones		= { z for (z,) in db.execute('select distinct zone from fact_rb') }
		report.check( 'RB-X2', (concerns == vocabulary) and zones <= spatial,
					  f'Rb indexed on the Ro basis: concerns {sorted(concerns)}, zones {sorted(zones)}' )

		off		= db.execute( 'select a.report_time, a.own_ship, a.cost, sum(b.exposure) '
							  'from fact_risk_assessment a join fact_rb b '
							  'on a.report_time = b.report_time and a.own_ship = b.vessel_id and a.case_id = b.case_id '
							  'group by a.id having abs(a.cost - sum(b.exposure)) > 1e-6 * max(1.0, abs(a.cost))' ).fetchall()
		report.check( 'RB-X3', not off, f'cost equals the sum of each sample\'s exposure'
					  + (f' - {len(off)} samples differ' if off else '') )

	print( f'{"FAILED" if report.failed else "PASSED"}: {report.failed} failure(s)' )
	return 1 if report.failed else 0


if __name__ == "__main__":
	sys.exit( main() )
