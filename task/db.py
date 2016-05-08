from invoke import run, task


@task
def init():
    print('Creating DB')
    run('python3 app/scripts/create_db.py')
