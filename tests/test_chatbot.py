# tests/test_chatbot.py

import pytest
from tests.pages.chatbot_page import ChatbotPage

BASE_URL = "http://127.0.0.1:5000/"

test_cases = [
    "Hola",
    "¿Cómo estás?",
    "Test 123",
]

@pytest.mark.parametrize("prompt", test_cases)
def test_echo_bot(driver, prompt):
    page = ChatbotPage(driver)
    page.go_to(BASE_URL)
    page.send_prompt(prompt)
    response = page.get_last_response()

    expected = f"Bot: Echo bot: «{prompt}»"
    assert response == expected, f"Respuesta incorrecta: {response}"

