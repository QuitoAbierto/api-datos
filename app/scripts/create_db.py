import couchdb
import os


def run():
    db_host = os.environ.get('DB_HOST') or 'http://db:5984'
    couch = couchdb.Server(db_host)

    try:
        print('Deleting database first...')
        couch.delete('repo')
        print('Creating database now...')
        return couch.create('repo')
    except couchdb.http.ResourceNotFound as e:
        print('Database does not exist yet!')
        print('Creating database now...')
        return couch.create('repo')

if __name__ == '__main__':
    run()
