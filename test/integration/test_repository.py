from test.helpers import *
from app.repository import Repository
from app.errors import InvalidDocumentError
from app.scripts import create_db
import couchdb

class TestRepository:

    def setup(self):
        self.db = create_db.run()
        self.repo = Repository(self.db)

    def test_persist_new_document(self):
        document = {'some_key': 'some_value'}
        new_document = self.repo.save(document)
        assert_equal(new_document['_id'], document['_id'])
        assert_equal(new_document['_rev'], document['_rev'])

    def test_throws_exception_when_empty_document_is_provided(self):
        document = {}
        with assert_raises(InvalidDocumentError) as error:
            self.repo.save(document)
            assert_equal('Invalid document provided', error.msg)

    def test_gets_every_document(self):
        document1 = {'some_key': 'some_value'}
        document2 = {'some_key': 'some_value'}
        self.repo.save(document1)
        self.repo.save(document2)

        documents = self.repo.all()
        assert_equal(2, len(documents))
