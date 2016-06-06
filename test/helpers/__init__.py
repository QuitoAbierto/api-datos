from nose.tools import *
from unittest.mock import *
import random
from app.scripts import get_db
from app.repository import Repository

def random_alpha(size):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(size))

def delete_db():
    db = get_db.run()
    repo = Repository(db)
    documents = repo.all()
    [db.delete(doc) for doc in documents]
