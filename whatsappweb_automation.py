from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import pandas as pd


data_df = pd.read_excel("data.xlsx")


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(5)

for i, message in enumerate(data_df["msg"]):
    contact = data_df.loc[i, "contact"]
    number = data_df.loc[i, "number"]
    text = urllib.parse.quote(f"Hi {contact}! {message}")
 
    link = f"https://web.whatsapp.com/send?phone={number}&text={text}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)
    enter_button = navegador.find_element(By.XPATH, "//div[contains(@title, 'Mensagem')]")
    enter_button.send_keys(Keys.ENTER)
    time.sleep(5)

menu_button = navegador.find_element(By.XPATH, "//div[contains(@title, 'Mais opções')]")
time.sleep(2)
menu_button.click()
disconnect_button = navegador.find_element(By.XPATH, "//div[contains(@aria-label, 'Desconectar')]")
time.sleep(2)
disconnect_button.click()