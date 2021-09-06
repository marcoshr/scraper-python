from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from countdown import countdown
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

options = Options()
prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "ENTER THE URL HERE"
}

options.add_experimental_option("prefs",prefs)

print("\n-- START: Abriendo navegador")
driver = webdriver.Chrome(options=options)

print("\n- Entrando a gamedesign.jp")
driver.get("https://www.gamedesign.jp/flash/dice/dice.html")

print("\n- Esperando la descarga de JS")
countdown(30)

print("- Pulsando para descargar")
driver.find_element_by_css_selector('body>div:first-child').click()

print("- Esperando la alerta")
countdown(5)

print("- Aceptando manualmente la alerta")


print("-- END: Cerrando navegador")
countdown()
driver.quit()

#search_box = driver.find_element_by_name('q')  # Find search input box.
#search_box.send_keys('selenium')               # Type in selenium.
#search_box.send_keys(Keys.RETURN)              # Press ENTER.