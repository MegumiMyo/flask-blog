import os
import json
import random
import string
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
# Base URL of the Flask application
base_url = f"http://{os.getenv('URI')}"

username = "".join(random.choices(string.ascii_lowercase, k=8))
email = f"{username}@example.com"
password = "".join(random.choices(string.ascii_letters + string.digits, k=12))

file_path = f"{os.getcwd()}/data/form_data.json"
file_update_path = f"{os.getcwd()}/data/update_post.json"


def read_json_file(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}': {e}")
        return None


def convert_json_to_list(json_data):
    if isinstance(json_data, list):
        return json_data
    else:
        print("Error: Input JSON data is not a list.")
        return None


def register(driver):
    driver.get(f"{base_url}/register")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "confirm_password").send_keys(password)

    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver, 3).until(EC.url_changes(f"{base_url}/register"))


def login(driver):
    driver.get(f"{base_url}/login")

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")

    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_button.click()

    WebDriverWait(driver, 3).until(EC.url_changes(f"{base_url}/login"))


def create_post(driver):
    for post in convert_json_to_list(read_json_file(file_path)):
        driver.get(f"{base_url}/post/new")

        title_input = driver.find_element(By.NAME, "title")
        content_input = driver.find_element(By.NAME, "content")
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        title_input.send_keys(post["title"])
        content_input.send_keys(post["content"])
        submit_button.click()

    WebDriverWait(driver, 3).until(EC.url_changes(f"{base_url}/post/new"))


def update_post(driver):
    for post in convert_json_to_list(read_json_file(file_update_path)):
        driver.get(f"{base_url}/post/{ username }")

        driver.get(f"{base_url}/post/{ post['post_id'] }/update")

        title_input = driver.find_element(By.NAME, "title")
        content_input = driver.find_element(By.NAME, "content")
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        title_input.send_keys(post["title"])
        content_input.send_keys(post["content"])
        submit_button.click()

    WebDriverWait(driver, 3).until(
        EC.url_changes(f"{base_url}/post/{post['post_id']}/update")
    )


def main():
    driver = None  # Initialize driver to None
    try:
        driver = webdriver.Chrome()  # Initialize the driver

        print(
            f"""UserDetail:
Email: {email}
Password: {password}
              """
        )
        register(driver)
        print("Registered User")
        login(driver)
        print("Login successful.")
        create_post(driver)
        print("Post add successful.")
        update_post(driver)
        print("Post updated successful.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
