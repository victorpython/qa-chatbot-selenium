# 🤖 QA Chatbot con Selenium y PyTest

Este repositorio contiene un proyecto completo de pruebas automatizadas para un chatbot simulado desarrollado en Flask. Las pruebas están diseñadas con **Selenium**, **PyTest** y el patrón **Page Object Model (POM)** para asegurar la mantenibilidad y escalabilidad del sistema.

## 📌 Tecnologías utilizadas

- Python 3.9+
- Selenium
- PyTest
- PyTest-HTML
- Flask (stub de chatbot)
- HTML + CSS (interfaz base del bot)

## 🧪 Funcionalidades del sistema de pruebas

- Pruebas automatizadas a respuestas del chatbot
- Validación de contenido de respuesta
- Generación de reporte HTML con `pytest-html`
- Estructura desacoplada mediante Page Object Model
- Manejo de errores y documentación de fallos (CSV y JSON)

## 📂 Estructura del proyecto

qa-chatbot-selenium/
├── stub_chatbot_flask/               # Mini servidor Flask (chatbot)
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── tests/                            # Tests automatizados
│   ├── __init__.py
│   ├── conftest.py                   # Fixture con WebDriver
│   ├── test_chatbot.py               # Casos de prueba
│   └── pages/
│       ├── __init__.py
│       └── chatbot_page.py           # Page Object
│
├── failures.csv                      # Registro estructurado de fallos
├── failures.json                     # Registro alternativo de fallos
├── report.html                       # Reporte generado por pytest-html
└── README.md                         # Este archivo

## 🚀 Instrucciones para ejecutar

1. Asegúrate de tener Chrome y el `chromedriver` en tu sistema.
2. Instala dependencias:
   ```bash
   pip install selenium pytest pytest-html flask
   ```
3. Corre el servidor Flask (desde otra terminal):
   ```bash
  cd stub_chatbot_flask
  python app.py
   ```
4. Ejecuta los tests:
 ```bash
  cd ..
  pytest -v tests/test_chatbot.py --html=report.html --self-contained-html
   ```

## 📬 Contacto
📧 victorcf.92@gmail.com
🔗 github.com/victorpython

