import couchdb

def run():
    couch = couchdb.Server()

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
