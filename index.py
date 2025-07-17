import os
import time

import pandas as pd
import pyperclip as ppc
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from win10toast import ToastNotifier


class App:
    def __init__(self):
        
        load_dotenv()

        self.notifier = ToastNotifier()

        #   Configurar Navegador
        options = Options()

        user_data_dir = os.getenv("USER_DATA_DIR")
        
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--profile-directory=Default")  # ou "Profile 1", etc

        options.add_argument("--start-maximized")
        options.add_argument("--log-level=3")
        
        print("checkpoint 1")
        service = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=service, options=options)
        print("Checkpoint 2")
        self.navegador.get(os.getenv("LINK"))

    def run(self):
        pass

try:
    print('incio')
    app = App()
    print('fim')
    
except Exception as e:
    print(f"\n\nERRO AO EXECUTAR AUTOMAÇÃO\n\n")
    print(e)
    
    time.sleep(5)