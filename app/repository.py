import couchdb
from app.errors import InvalidDocumentError


class Repository:

    def __init__(self, db):
        self.db = db

    def save(self, document):
        if not document:
            raise InvalidDocumentError('Invalid document provided')
        document['type'] = 'parada'
        self.db.save(document)
        return document

    def all(self):
        map_function = '''
            function(doc) {
                if(doc.type === 'parada') {
                    emit(doc._id, doc);
                }
            }'''
        return self.db.query(map_function)
