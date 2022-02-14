from functions.Functions import Functions as Selenium


def after_scenario(self, scenario):
    Selenium.tearDown(self)


def after_step(self, step):
    print(u'Verifica tu localizador.')
    if step.status == 'failed':
        Selenium.capture(self, "screenShot")