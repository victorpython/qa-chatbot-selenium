import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = r"D:\Documentos\Data scientist\Stratis\chromedriver.exe"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-allow-origins=*")
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)  # opcional
    yield driver
    driver.quit()
