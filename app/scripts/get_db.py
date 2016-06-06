import couchdb
import os


def run():
    db_host = os.environ.get('DB_HOST') or 'http://db:5984'
    couch = couchdb.Server(db_host)
    try:
        return couch.create('repo')
    except couchdb.http.PreconditionFailed as e:
        return couch['repo']

if __name__ == '__main__':
    run()
