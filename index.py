import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from win10toast import ToastNotifier
from dotenv import load_dotenv

class App:
    def __init__(self):
        
        load_dotenv()

        self.notifier = ToastNotifier()

        #   Configurar Navegador
        self.navegador = webdriver.Chrome()
        self.navegador.get(...)
        self.navegador.maximize_window()

    def run(self):
        pass

try:
    app = App()
    app.run()
    
except Exception as e:
    print(f"\n\nERRO AO EXECUTAR AUTOMAÇÃO\n\n")
    time.sleep(5)