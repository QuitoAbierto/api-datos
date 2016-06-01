import couchdb
from app.errors import InvalidDocumentError


class Repository:

    def __init__(self, db):
        self.db = db

    def save(self, document):
        if not document:
            raise InvalidDocumentError('Invalid document provided')
        self.db.save(document)
        return document
