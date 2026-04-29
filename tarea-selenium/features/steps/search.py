# -*- coding: utf-8 -*-

from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given("I am on the Google homepage")
def open_browser(context):
    context.driver.get("https://www.google.com")


@when('I search for "{query}"')
def search_google(context, query):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


@when("I click the first Google result")
def click_first_result(context):
    wait = WebDriverWait(context.driver, 10)
    first_result_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
    first_result_title.click()


@then('I should be on the "{domain}" homepage')
def verify_homepage(context, domain):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains(domain))
    current_url = context.driver.current_url
    assert (
        domain in current_url
    ), f"Esperábamos estar en {domain}, pero estamos en {current_url}"


@when('I search for "{search_term}" within the university site')
def search_within_university(context, search_term):
    wait = WebDriverWait(context.driver, 10)
    current_url = context.driver.current_url

    if "iteso.mx" in current_url:
        search_icon = wait.until(EC.element_to_be_clickable((By.ID, "icon-search")))
        search_icon.click()
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "ipt-search")))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    elif "udg.mx" in current_url:
        # Lógica para la UdeG
        search_icon = wait.until(EC.element_to_be_clickable((By.ID, "buscar_front")))
        search_icon.click()
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "keys")))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    elif "unam.mx" in current_url:
        # Lógica para la UNAM
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.submit()

    else:
        raise Exception(
            f"No hay lógica de búsqueda definida para la URL: {current_url}"
        )


@then('the university site results should be related to "{search_term}"')
def verify_university_results(context, search_term):
    wait = WebDriverWait(context.driver, 10)
    current_url = context.driver.current_url
    term_lower = search_term.lower()

    if "iteso.mx" in current_url or "unam.mx" in current_url or "udg.mx" in current_url:
        # ITESO, UNAM y UdeG usan el mismo motor de Google, la validación es idéntica
        first_result = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.gs-title"))
        )
        result_text = first_result.text.lower()
        assert (
            term_lower in result_text
        ), f"Término no encontrado en {current_url}: {result_text}"

    else:
        raise Exception(f"No hay validación definida para la URL: {current_url}")
