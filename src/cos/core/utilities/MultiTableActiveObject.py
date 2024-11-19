#!/usr/bin/python
# Filename: MultiTableActiveObject.py
# Description: Multi-table Active record design pattern for ORM DB access

from cos.core.utilities.ActiveRecord import ActiveRecord

class MultiTableActiveObject:
	def __init__(self, rec, oid, fk_name):
		self.rec		= rec
		self.id			= oid
		self.fk_name	= fk_name
		return

	def get_id(self):
		return self.id
	
	def get_meta_property(self, field):
		field_type	= None
		ndx			= field.find(':')		
		if ndx != -1:
			field_type	= field[ndx+1:]
			field		= field[:ndx]
			
		return (field, self.GetPropTable(field_type))
				
	def __getitem__(self, field):
		if self.IsProperty(field) == False:
			return self.rec.Get(self.id, field)

		rfield	= self.get_meta_property(field)
		field	= rfield[0]
		table	= rfield[1]
						
		t   	= (field,)
		c		= self.rec.conn.cursor()
		c.execute('SELECT value FROM {} WHERE name=? AND {}={} '.format(table, self.fk_name, self.id ), t )
		
		row	= c.fetchone()
		if row == None:
			return None
		return row[0]
		
		
	def __setitem__(self, field, value):
		if self.IsProperty(field) == False:
			return self.rec.Set(self.id, field, value)

		rfield	= self.get_meta_property(field)
		field	= rfield[0]
		table	= rfield[1]

		rec		= ActiveRecord( None, self.rec.conn, table )
		propid	= self.__get_meta_property_id(rec, field)
		
		# If a property already exists, update it
		if propid != None:
			rec.Set( propid, 'value', value )
			return
			
		values = {
			self.fk_name:self.id,
			'name': field,
			'value': value }
				
		rec.Add( values )
		return

	def __get_meta_property_id(self, rec, field):
		t   = (field,)
		c	= rec.conn.cursor()
		c.execute('SELECT id FROM {} WHERE name=? AND {}={}'.format(rec.table, self.fk_name, self.id), t )
		row	= c.fetchone()
		if row == None:
			return None
		return row[0]
	

if __name__ == '__main__':
    test = MultiTableActiveObject()

