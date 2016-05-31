from invoke import run, task
from task.helpers import task_message


@task
def integration():
    task_message('Integration Tests')
    run('nosetests test/integration')

@task
def functional():
    task_message('Functional Tests')
    run('nosetests test/functional')

@task(default=True, pre=[integration, functional])
def all():
    task_message('Running all tests')
    pass
