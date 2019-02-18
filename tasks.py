from invoke import task


@task
def run(context, browser='', env='', tags=''):
    """
    Run tests without allure report generating
    :param context: invoke context object
    :param browser: run tests on specific browser (CH, CH_HL, FF, FF_HL)
    :param env: run tests on specific environment (DEV, UAT, LOCALHOST)
    :param tags: run only tests marked by specific tag
    :keyword: '$ invoke run'
    :keyword: '$ invoke run --browser=SF --env=UAT --tags=@menu'
    """
    behave_cmd = 'behave --no-capture'
    if env != '':
        behave_cmd = ' -D env='.join([behave_cmd, env])
    if browser != '':
        behave_cmd = ' -D browser='.join([behave_cmd, browser])
    if tags != '':
        behave_cmd = ' --tags='.join([behave_cmd, tags])
    context.run(behave_cmd)


@task
def run_with_allure(context, browser='', env='', tags=''):
    """
    Run tests with html allure report generating
    :param context: invoke context object
    :param browser: run tests on specific browser (CH, CH_HL, FF, FF_HL)
    :param env: run tests on specific environment (DEV, UAT, LOCALHOST)
    :param tags: run only tests marked by specific tag
    :keyword: '$ invoke run-with-allure'
    :keyword: '$ invoke run-with-allure --browser=SF --env=UAT --tags=@menu'
    """
    behave_cmd = 'behave --format allure --outfile artifacts --format pretty --no-capture --tags=~@download_file'
    if env != '':
        behave_cmd = ' -D env='.join([behave_cmd, env])
    if browser != '':
        behave_cmd = ' -D browser='.join([behave_cmd, browser])
    if tags != '':
        behave_cmd = ' --tags='.join([behave_cmd, tags])
    context.run(behave_cmd)


@task
def run_failed(context, browser='', env=''):
    """
    Rerun tests which were failed during previous run
    :param context: invoke context object
    :param browser: run tests on specific browser (CH, CH_HL, FF, FF_HL)
    :param env: run tests on specific environment (DEV, UAT, LOCALHOST)
    :keyword: '$ invoke run-failed'
    :keyword: '$ invoke run-failed --browser=SF --env=UAT'
    """
    behave_cmd = 'behave @rerun_failing.features --no-capture'
    if env != '':
        behave_cmd = ' -D env='.join([behave_cmd, env])
    if browser != '':
        behave_cmd = ' -D browser='.join([behave_cmd, browser])
    context.run(behave_cmd)
