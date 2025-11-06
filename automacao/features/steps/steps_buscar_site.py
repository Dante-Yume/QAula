from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdrive_manager.microsoft import EdgeCromiumDriveMenager
from selenium.webdriver.edge.service import EdgeService
import time
from behave import given, when, then

# step 1 

@given("que o navegador esteja na pagina inicial")
def step_open_browser(context):

    options= webdriver.EdgeOptions()
    options.add_argument('--start-maximized')

    context.driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )
    context.drive.get("https:/www.google.com")
    time.sleep(3)