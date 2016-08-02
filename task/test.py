from invoke import run, task
from task.helpers import task_message


@task
def integration():
    task_message('Integration Tests')
    run('nosetests test/integration --with-xunit --xunit-file=test_reports/integration.xml')

@task
def functional():
    task_message('Functional Tests')
    run('nosetests test/functional --with-xunit --xunit-file=test_reports/functional.xml')

@task
def unit():
    task_message('Unit Tests')
    run('nosetests test/unit --with-xunit --xunit-file=test_reports/unit.xml')

@task(default=True, pre=[unit, integration, functional])
def all():
    task_message('Running all tests')
    pass

@task
def coverage():
    task_message('Running tests with coverage. See cover directory for details.')
    run('nosetests --with-coverage --cover-package=app --cover-html test/')
