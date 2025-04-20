from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChatbotPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to(self, base_url):
        self.driver.get(base_url)

    def send_prompt(self, prompt):
        input_box = self.wait.until(EC.presence_of_element_located((By.ID, "messageInput")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_box)
        input_box.clear()
        input_box.click()
        input_box.send_keys(prompt)

        send_button = self.driver.find_element(By.ID, "sendButton")
        send_button.click()

    def get_last_response(self):
        bot_messages = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#chat .bot")))
        return bot_messages[-1].text
