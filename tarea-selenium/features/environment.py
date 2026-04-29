# features/environment.py
from selenium.webdriver.chrome.options import Options

from selenium import webdriver


def before_scenario(context, scenario):
    """Abre un nuevo navegador Chrome antes de cada escenario."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    """Cierra el navegador después de cada escenario, pase o falle."""
    if hasattr(context, "driver"):
        context.driver.quit()
