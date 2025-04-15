from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options # Used for headless mode; an object that allows me to customize how I want to start the browser
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


#  Run Behave tests with Allure results
#  behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/SEARCH_HIGH_DEMAND.feature

def browser_init(context, scenario_name):

    """
    :param context: Behave context
    32?.,'l0kk
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### OTHER BROWSERS ###
    # service = Service(executable_path='C:/Users/Owner/internship_project/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("window-size=1920,1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)

    ### BROWSER STACK ### in order to connect remotely
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #https://www.browserstack.com/docs/automate/capabilitieshttps://www.browserstack.com/docs/automate/capabilities
    # bs_user = 'tracyarispe_Z6z07g'
    # bs_key = 'gAWUTkUZbmoJSfwuego7'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #  'os': 'Windows',
    #  'osVersion': '10',
    #  'browserName': 'Chrome',
    #  'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    #context.driver.implicitly_wait(4)

    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #logger.info(f'Started scenario: {scenario.name}')###When running this line for logger, comment out the above print line
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger.info(f'Started step: {step}')###When running this line for logger, comment out the above print line


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        #logger.error(f'Step failed: {step}')###When running this line for logger, comment out the above print line


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
