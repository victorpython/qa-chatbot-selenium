import csv
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta al chromedriver
CHROMEDRIVER_PATH = r"D:\Documentos\Data scientist\Stratis\chromedriver.exe"
BASE_URL = "http://127.0.0.1:5000/"

# Prompts de prueba
prompts = [
    "Hola",
    "¿Cómo estás?",
    "Test 123",
]

# Lista para almacenar los fallos
failures = []

# Configurar WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--remote-allow-origins=*")
service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get(BASE_URL)
    for prompt in prompts:
        try:
            # Esperar a que el input esté presente y visible
            input_box = wait.until(EC.presence_of_element_located((By.ID, "messageInput")))
            driver.execute_script("arguments[0].scrollIntoView(true);", input_box)
            input_box.clear()
            input_box.click()
            input_box.send_keys(prompt)
            driver.find_element(By.ID, "sendButton").click()

            # Esperar y capturar la última respuesta del bot
            bot_messages = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#chat .bot")))
            bot_msg = bot_messages[-1].text

            # Validar la respuesta
            expected = f"Bot: Echo → {prompt}"
            assert bot_msg == expected, f"Respuesta inesperada: {bot_msg}"
            print(f"✅ OK: '{prompt}' → '{bot_msg}'")

        except Exception as e:
            # Registrar el fallo para este prompt
            failures.append({
                "prompt": prompt,
                "error": str(e),
            })

finally:
    driver.quit()

    # Si hubo fallos, guardarlos en CSV y JSON
    if failures:
        # Guardar CSV
        keys = failures[0].keys()
        with open("failures.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(failures)

        # Guardar JSON
        with open("failures.json", "w", encoding="utf-8") as jsonfile:
            json.dump(failures, jsonfile, ensure_ascii=False, indent=2)

        print(f"❌ Fallos registrados: {len(failures)}. Revisa 'failures.csv' y 'failures.json' para más detalles.")
    else:
        print("🎉 Todas las pruebas pasaron correctamente.")
