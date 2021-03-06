from test.helpers import *
from app.stop_repository import StopRepository
from app.errors import InvalidDocumentError
from app.scripts import get_db
import couchdb

class TestStopRepository:

    def setup(self):
        self.db = get_db.run()
        self.repo = StopRepository(self.db)
        delete_db()

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
        document1 = {'some_key': 'some_value', 'type': 'parada'}
        document2 = {'some_key': 'some_value', 'type': 'parada'}
        self.repo.save(document1)
        self.repo.save(document2)

        documents = self.repo.all()
        assert_equal(2, len(documents))

    def test_gets_only_documents_of_type_parada(self):
        self.db.save({'key': 'value1', 'type': 'cosa'})
        self.db.save({'key': 'value2', 'type': 'cosa'})
        self.db.save({'key': 'value3', 'type': 'parada'})

        documents = self.repo.all()
        assert_equal(1, len(documents))

    def test_gets_formated_stop(self):
        value = random_alpha(10)
        stop = {'some_key': value, 'type': 'parada'}
        self.repo.save(stop)

        stored_stop = self.repo.all()[0]
        assert_equal(value, stored_stop['some_key'])
