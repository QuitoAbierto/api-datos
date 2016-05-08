from invoke import run, task


@task
def integration():
    run('nosetests test/integration')

@task
def functional():
    run('nosetests test/functional')

@task(default=True, pre=[integration, functional])
def all():
    pass
