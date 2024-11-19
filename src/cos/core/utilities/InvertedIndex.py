#!/usr/bin/python
# Filename: InvertedIndex.py
# Description: Field map with a match row names to an array or rowname, ususally used in data retrieval.

from cos.core.utilities.TransactionalDatabase import TransactionalDatabase
from pygtrie import Trie

class DocInfo:
	def __init__(self, file, title, desc=None):
		""" constructor
		Arguments
				file -- File name or path
			desc -- Description of the file
		"""
		self.file	= file
		self.title	= title
		self.desc	= desc
		return

	def __eq__(self, other):
		""" Comparison operator
		Arguments
				other -- document info to compare to
		"""
		return other is not None and (self.file == other.file)

class SearchNode:
	def __init__(self):
		""" constructor
		Arguments
			"""
		self.files	= []
		return

class SearchTrie(Trie):
	def __init__(self):
		""" constructor
		Arguments
			"""
		Trie.__init__(self)
		return

	def find( self, key ):
		""" Finds a word node in the trie
		Arguments
				key -- Trie key (search word)
		"""
		if Trie.has_key(self, key) == False:
			return None

		return Trie.__getitem__( self, key )

	def add( self, key ):
		""" Adds a word to the trie
		Arguments
				key -- Trie key (search word)
		"""
		if Trie.has_key(self, key) == True:
			return Trie.__getitem__( self, key )


		node	= self.create_node(key)
		Trie.__setitem__( self, key, node )
		return node

	def create_node( self, key ):
		""" Overridable function to create a node on the trie
		Arguments
			key -- Trie key (search word)
		"""
		return SearchNode()

class SearchIndexParseCallbacks:
	def __init__(self, add_word=None, add_doc=None, add_ndx=None):
		""" Constructor
		Arguments
			add_word=None -- Callback to add a word
			add_doc=None -- Callbackto add a doc
			add_ndx=None -- Callback to add an (word,doc) index
		"""
		self.add_word	= add_word
		self.add_doc	= add_doc
		self.add_ndx	= add_ndx
		return


	@staticmethod
	def add_word(word_id, word, word_info, db):
		""" Adds a word to the index
		Arguments
			word_id -- Word ID
			word -- Word
			word_info -- Word information
			db -- Database to add record to
		"""
		db.add( 'words',
				{
					'id': 	word_id,
					'word': word
				}
			)
		return

	@staticmethod
	def add_doc(doc_id:int, filename:str, title:str, desc:str, doc_info, db):
		""" Adds a document to the index
		Arguments
			doc_id -- Document ID
			filename -- File name of the document
			desc -- Description of the document
			doc_info -- Document source information
			db -- Database to add record to
		"""
		if desc == None:
			desc	= ''

		db.add( 'docs',
				{
					'id': 	doc_id,
					'type': 1,
					'title': title,
					'filename': filename,
					'description': desc
				}
			)
		return

	@staticmethod
	def add_index(word_id:int, doc_id:int, db):
		""" Adds an index to the database
		Arguments
			word_id -- Word ID
			doc_id -- Document ID
			db -- Database to add record to
		"""
		db.add( 'word_indices',
				{
					'word_id': 	word_id,
					'doc_id': 	doc_id
				}
			)
		return

class SearchIndex:
	def __init__(self):
		""" constructor
		"""
		self.doc_count	= 0
		self.doc_trie	= SearchTrie()
		return

	def add_text( self, text, doc, minlen=3 ):
		""" Adds a text to the index
		Arguments
			text -- Text segment to index
			doc -- Document source of the text
		"""
		text = text.replace( ',', ' ' );
		text = text.replace( '.', ' ' );
		text = text.replace( ';', ' ' );
		text = text.replace( '-', ' ' );
		text = text.replace( '_', ' ' );
		text = text.replace( ':', ' ' );
		text = text.replace( '\'', ' ' );
		text = text.replace( '"', ' ' );
		text = text.replace( '\r', ' ' );

		Words	= text.lower().split();

		for word in Words:
			word	= word.strip();

			if len(word) < minlen:
				continue;

			self.add_word( word, doc );

		return

	def add_word( self, word, doc ):
		""" Adds a word text and its information to the index
		Arguments
			word -- Text of the word in the document
			doc -- Document information
		"""
		node	= self.doc_trie.add( word )

		if node == None:
			return True

		self.__add_doc( node.files, doc )
		return True

	def find_docs( self, word ):
		""" Finds the files containing a word
		Arguments
			word -- Word to search for
		"""
		node	= self.doc_trie.find( word )
		if node == None:
			return []

		return node.files

	@property
	def trie(self):
		""" Returns the trie data structure	tracking words in documents
		"""
		return self.doc_trie

	@property
	def num_docs(self):
		""" Returns the number of documents
		"""
		return self.doc_count

	def for_each(self, callbacks, ctxt=None):
		""" Process each item in the trie
		Arguments
			callbacks -- Callbacks to handle processing records
			ctxt=None -- Opaque context passed to callbacks
		"""
		docs	= set()
		for k, v in self.doc_trie.iteritems():
			# Iterate through all the words
			word_id	= id(v)
			if callbacks.add_word != None:
				callbacks.add_word( word_id, ''.join(k), v, ctxt)

			if (callbacks.add_doc == None) and (callbacks.add_ndx == None):
				return

			# Iterate through all the documents
			# associatedwith the words.
			for d in v.files:
				doc_id	= id(d)
				if callbacks.add_doc != None:
					if doc_id not in docs:
						callbacks.add_doc( doc_id, d.file, d.title, d.desc, d, ctxt)
						docs.add(doc_id)

				if callbacks.add_ndx != None:
					callbacks.add_ndx( word_id, doc_id, ctxt )
		return

	def dump(self, path):
		""" dumps the index to a file
		Arguments
			path -- Path of the file
		"""
		db			= TransactionalDatabase()
		callback	= SearchIndexParseCallbacks(
							SearchIndexParseCallbacks.add_word,
							SearchIndexParseCallbacks.add_doc,
							SearchIndexParseCallbacks.add_index )

		# Open the database
		db.open(path)

		# Iterate through all the records
		self.for_each( callback, db )

		# Flush pending transactions
		db.flush()

		# Close the database
		db.close()
		return

	def __add_doc( self, files, doc ):
		""" Add a document to the file list
		Arguments
			files -- Files list to which to add the document
			doc -- Document to add
		"""

		# If the document is already in the list,
		# do not add it again.
		if doc in files:
			return False

		files.append( doc )
		self.doc_count	+=1
		return True

if __name__ == "__main__":
	idx 	= SearchIndex()

