from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip

app = Flask(__name__)

@app.route('/', methods=['POST'])
def execute_script():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Uncomment this line if you want to run Chrome in headless mode

    # Initialize the Chrome webdriver
    driver = webdriver.Chrome(options=options)

    # URL of the website
    url = 'https://tp.koffice.site/login/'

    # Credentials
    username = 'Splygoxo'
    password = 'Essasenha23@C'
    # Navigate to the website
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Find the username and password fields and enter the login credentials
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    menu_lateral = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/nav/button')
    menu_lateral.click()



    # Aguardar mais 5 segundos
    time.sleep(5)

    # Clicar em <span key="">Criar Teste</span>
    criar_teste_button = driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[12]/a')
    criar_teste_button.click()

    # Aguardar 2 segundos
    time.sleep(2)

    # Clicar em <a class="" href="https://painel.turboplay.link/panel.php?page=customers/form_test">IPTV</a>
    iptv_link = driver.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[12]/ul/li[2]/a')
    iptv_link.click()
    time.sleep(5)


    copy_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/button[2]')
    copy_button.click()


    # Esperar alguns segundos para a cópia ser realizada
    time.sleep(2)

    # Obter o conteúdo da área de transferência
    clipboard_content = pyperclip.paste()

    # Imprimir os dados no console
    print(clipboard_content)



    # Wait for 40 seconds
    time.sleep(40)

    # Close the browser
    driver.quit()

    return clipboard_content

if __name__ == '__main__':
    app.run()
