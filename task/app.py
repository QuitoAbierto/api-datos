from invoke import run, task


@task
def web():
    print('Starting App')
    run('gunicorn api:app --pythonpath app --reload -c config/gunicorn.py > /dev/null 2>&1 &')

@task
def stop_web():
    print('Stopping App')
    run('cat /tmp/gunicornpid | xargs kill -9')
