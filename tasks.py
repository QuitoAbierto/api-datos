from invoke import Collection, task
from task import app, db, test


namespace = Collection(app, db, test)
