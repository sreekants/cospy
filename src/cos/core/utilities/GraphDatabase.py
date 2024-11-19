#!/usr/bin/python
# Filename: GraphDatabase.py
# Description: Active record design pattern for graph database access

from cos.core.utilities.MultiTableActiveObject import MultiTableActiveObject
from cos.core.utilities.ActiveRecord import ActiveRecord

import uuid
from datetime import datetime

class GraphDatabaseConnection:
	def __init__(self, dbpath):
		self.dbpath		= dbpath
		return

	def create(self, table:str):
		return ActiveRecord.create('', self.dbpath, table)

class Arc(MultiTableActiveObject):
	def __init__(self, rec, arc_id):
		MultiTableActiveObject.__init__(self, rec, arc_id, 'arc_id')
		return
		
	def is_property(self, field):
		return field not in ['id','guid','graph_id','name','clsid','objid','type','weight','start','end']

	def get_property_table(self, field_type):
		if field_type == None:
			return 'arc_props'
		else:
			return 'arc_{}_props'.format(field_type)
		
	def get_weight(self):
		return self.rec.get(self.id, 'weight')

	def set_weight(self, value):
		return self.rec.set(self.id, 'weight', value)

	def increment_weight(self, value):
		return self.set_weight( self.get_weight()+value )
	
class Vertex(MultiTableActiveObject):
	def __init__(self, rec, vertex_id):
		MultiTableActiveObject.__init__(self, rec, vertex_id, 'vertex_id')
		return

	def is_property(self, field):
		return field not in ['id','guid','graph_id','name','clsid','objid','x','y','type','value','source']

	def get_property_table(self, field_type):
		if field_type == None:
			return 'vertex_props'
		else:
			return 'vertex_{}_props'.format(field_type)				

	def get_arcs_from(self):
		arcs = ActiveRecord('arc', self.rec.conn, 'arcs')
		return arcs.get_object_list(f'start={self.id}')

	def get_arcs_to(self):
		arcs = ActiveRecord('arc', self.rec.conn, 'arcs')
		return arcs.get_object_list(f'end={self.id}')

	def get_all_arcs(self):
		arcs = ActiveRecord('arc', self.rec.conn, 'arcs')
		return arcs.get_object_list(f'start={self.id} OR end={self.id}')

	def get_value(self):
		return self.rec.get(self.id, 'value')

	def set_value(self, value):
		return self.rec.set(self.id, 'value', value)

	def increment_value(self, value):
		return self.set_value( self.get_value()+value )

class GraphDatabase:
	def __init__(self, dbpath:str, graph_id=-1):
		self.conn		= GraphDatabaseConnection(dbpath)
		self.graph_id	= graph_id
		self.db			= None
		return
	
	def __getitem__(self, table):
		return self.conn.create(table)
	
	def __get_db(self, table='graphs'):
		self.db = self.conn.create(table)
		return self.db
	
	def create(self, name, graph_type, guid=None, description=None, metadata=None):
		if metadata == None:
			metadata	= ''

		if description == None:
			description	= ''

		if guid == None:
			guid	= str(uuid.uuid1()).lower()
		elif isinstance(guid, uuid.UUID):
			guid	= str(guid).lower()
			
		values = {
			'guid': guid,
			'name':name,
			'description': description,
			'metadata': metadata,
			'type': graph_type }

		self.graph_id = self.__get_db().add( values )
		return True
	
	def open(self, name, guid=None):
		if guid != None:
			if isinstance(guid, uuid.UUID):
				guid	= str(guid).lower()

		db = self.__get_db()

		if guid == None:
			self.graph_id = db.get_unique_by('id', 'name', name)
		else:
			self.graph_id = db.get_unique_by('id', 'guid', guid)

		if self.graph_id == None:
			return False
		
		return True

	def close(self):
		return

	def execute_sql(self, sql):
		self.__get_db().execute_sql(sql)
		return
		
	def get_vertices(self):
		rec = self.__get_vertex_model()
		return rec.get_object_list( f'graph_id={self.graph_id}')

	def get_arcs(self):
		rec = self.__get_arc_model()
		return rec.get_object_list( f'graph_id={self.graph_id}')

	def get_vertex_props(self, table="vertex_props")->ActiveRecord:
		return self.__getitem__(table)

	def get_arc_props(self, table="arc_props")->ActiveRecord:
		return self.__getitem__(table)

	def get_vertex_by_guid(self, guid):
		results	= self.__get_vertex_model().find_by('guid', guid)
		if results == None:
			return None
			
		return Vertex( self.__get_vertex_model(), results[0] )

	def get_arc_by_guid(self, guid):
		results	= self.__get_arc_model().find_by('guid', guid)
		if results == None:
			return None
			
		return Arc( self.__get_arc_model(), results[0] )
								
	def add_vertex(self, name, vert_type=0, guid=None, value=0):
		if guid == None:
			guid	= str(uuid.uuid1()).lower()
		elif isinstance(guid, uuid.UUID):
			guid	= str(guid).lower()
			
		creation_time = datetime.utcnow()
		values = {
			'graph_id':self.graph_id,
			'guid': guid,
			'creation_time': creation_time,
			'name': name,
			'value': value,
			'type': vert_type }

		v	= self.__get_vertex_model()
		return Vertex( v, v.add(values) )

	def is_Vertex(self, vid):
		if isinstance(vid, int):
			return (self.get_vertex_id(vid) != None)
		elif isinstance(vid, uuid.UUID):
			ids	= self.__get_vertex_model().find_by('guid', str(vid).lower())
		else:
			ids	= self.__get_vertex_model().find_by('name', vid)

		return (len(ids)!=0)

	def get_arc(self, aid):
		if isinstance(aid, int):
			return Arc( self.__get_arc_model(), aid )
		elif isinstance(aid, uuid.UUID):
			ids	= self.__get_arc_model().find_by('guid', str(aid).lower())
		else:
			ids	= self.__get_arc_model().find_by('name', aid)

		if len(ids)==0:
			return None
		return Arc( self.__get_arc_model(), ids[0] )

	def get_vertex(self, vid, type=None):
		if isinstance(vid, int):
			return Vertex( self.__get_vertex_model(), vid )
		elif isinstance(vid, uuid.UUID):
			ids	= self.__get_vertex_model().find_by('guid', str(vid).lower())
		else:
			ids	= self.__get_vertex_model().find_by('name', vid)

		if len(ids)==0:
			return None
		return Vertex( self.__get_vertex_model(), ids[0] )

	def get_vertex_by_name(self, name, vert_type=0, guid=None, value=0, auto_add=True):
		vid	= self.get_vertex_id(name)
		if vid != None:
			return Vertex( self.__get_vertex_model(), vid )
		
		if auto_add == False:
			return None
		
		return self.add_vertex(name, vert_type, guid, value)
		
	def get_vertex_id(self, vid):
		guid	= None
		if isinstance(vid, uuid.UUID):
			guid = str(vid).lower()

		t   = (vid,)
		c	= self.__get_vertex_model().conn.cursor()
		
		if guid == None:
			c.execute('SELECT id FROM vertices WHERE graph_id={} AND name=?'.format(self.graph_id), t  )
		else:
			c.execute('SELECT id FROM vertices WHERE graph_id={} AND guid=?'.format(self.graph_id), t  )

		row	= c.fetchone()
		if row == None:
			return None
			
		return row[0]
				
	def get_num_vertices(self):
		return self.__get_vertex_model().get_object_count( 'graph_id={}'.format(self.graph_id) )

	def get_num_arcs(self):
		return self.__get_arc_model().get_object_count( 'graph_id={}'.format(self.graph_id) )
			
	def delete_vertex(self, name):
		vid	= self.get_vertex_id(name)
		if vid == None:
			return False
			

		edge = self.get_vertex(vid)
		for a in edge.get_all_arcs():
			self.__delete_arc_ref(a)

			tables = ['vertex_props','vertex_int_props','vertex_float_props']
			for prop in tables:
				self.get_vertex_props(prop).delete_by('vertex_id',vid)	
				
		self.__get_vertex_model().delete_by(vid)
		return True

	def resolve_vertex(self, start, end):
		if isinstance(start, int):
			fromid	= start
		else:
			fromid	= self.__get_safe_vertex_id(start)
		
		if isinstance(end, int):
			toid	= end
		else:
			toid	= self.__get_safe_vertex_id(end)
				
		return (fromid, toid)

	def get_arc_id(self, fromid, toid):
		a	= self.__get_arc_model()
		c	= self.__get_arc_model().conn.cursor()
		c.execute('SELECT id FROM arcs WHERE graph_id={} AND start={} AND end={}'.format(self.graph_id, fromid, toid) )
		row	= c.fetchone()
		if row == None:
			return None
		
		return row[0]

	def is_joined(self, start, end, directed=False):
		fromid, toid	= self.resolve_vertex(start, end)
		
		if(self.get_arc_id(fromid, toid) != None):
			return True
		
		if directed == True:
			return False
				
		return (self.get_arc_id(toid, fromid) != None)
			
	def join(self, start, end, arc_type=0, guid=None, name=None, weight=0):
		fromid, toid	= self.resolve_vertex(start, end)
		arcid	= self.get_arc_id(fromid, toid)
		
		if arcid != None:
			Arc = Arc( self.__get_arc_model(), arcid )
			Arc['weight'] = weight
			return Arc

		if guid == None:
			guid	= str(uuid.uuid1()).lower()
		elif isinstance(guid, uuid.UUID):
			guid	= str(guid).lower()

		if name == None:
			name	= ''

		creation_time = datetime.utcnow()
		values = {
			'graph_id':self.graph_id,
			'guid': guid,
			'creation_time': creation_time,
			'name':name,
			'start': fromid,
			'end': toid,
			'weight': weight,
			'type': arc_type }
		
		return Arc( self.__get_arc_model(), self.__get_arc_model().add(values) )

									
	def detach(self, start, end):
		fromid, toid	= self.resolve_vertex(start, end)
		arcid	= self.get_arc_id(fromid, toid)
		
		if arcid != None:
			return False
			
		self.__delete_arc_ref(arcid)
		return True
	
	def __delete_arc_ref(self,arcid):
		self.__get_arc_model().delete(arcid)

		tables = ['arc_props','arc_int_props','arc_float_props']
		for prop in tables:
			self.get_arc_props().delete_by('arc_id',arcid)		

	def __get_safe_vertex_id(self, name):
		vid	= self.get_vertex_id(name)
		if vid == None:
			raise Exception("Invalid vertex {}.", name)
			
		return vid

	def __get_vertex_model(self)->ActiveRecord:
		return self.__getitem__('vertices')

	def __get_arc_model(self)->ActiveRecord:
		return self.__getitem__('arcs')
		
if __name__ == '__main__':
	test = GraphDatabase( "graph.s3db", 14 )
