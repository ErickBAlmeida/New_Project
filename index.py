import os
import re
import time

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from win10toast import ToastNotifier


class App:
    def __init__(self):
        
        load_dotenv()

        self.notifier = ToastNotifier()

        #   Configurar Navegador
        options = Options()        
        options.add_argument("--start-maximized")
        options.add_argument("--log-level=3")
        
        self.navegador = webdriver.Chrome()
        self.navegador.get(os.getenv("LINK"))
        self.navegador.maximize_window()

        self.run()
        
    def navegar(self):
        
        time.sleep(5)
        self.navegador.refresh()

        #   NAVEGA PELO MENU DO SITE
        try:
            botao_menu = WebDriverWait(self.navegador, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "botao-menu"))
            )
            botao_menu.click()
            print("\nNavegando pelo site...")
            time.sleep(1)  # Espera um pouco para garantir que o menu esteja aberto

            processo = self.navegador.find_element("partial link text", "Processo")
            processo.click()
            time.sleep(.5)

            acoes = self.navegador.find_elements(By.XPATH, "//*[contains(text(), ' Outras ações ')]")	
            acoes[0].click()
            time.sleep(.5)

            soliciar_hab = self.navegador.find_elements(By.XPATH, "//*[contains(text(), ' Solicitar habilitação ')]")
            soliciar_hab[0].click()
            time.sleep(.5)
            
        except Exception as e:

            self.notifier.show_toast("ERRO", "Erro ao navegar pelo site", duration=3)
            time.sleep(5)
            raise Exception("Erro ao navegar pelo site") from e

    def getNumPeticao(self, num_peticao):

        try:
            peticao_str = str(num_peticao)

            self.notifier.show_toast("Início", f"Buscando por: \n{peticao_str}", duration=4)
            print("====================================================================")
            print(f"Buscando por: {num_peticao}\n\n")

            peticao_str = re.sub(r'[^0-9]','', peticao_str)

            if peticao_str.isdigit() != True:
                print("\n\nPetição não é valida, indo para a proxima.\n\n")
                return False

            time.sleep(1)
            self.navegador.find_element(By.ID, "fPP:numeroProcesso:numeroSequencial").send_keys(peticao_str[0:7])
            self.navegador.find_element(By.ID, "fPP:numeroProcesso:numeroDigitoVerificador").send_keys(peticao_str[7:9])
            self.navegador.find_element(By.ID, "fPP:numeroProcesso:Ano").send_keys(peticao_str[9:13])
            self.navegador.find_element(By.ID, "fPP:numeroProcesso:NumeroOrgaoJustica").send_keys(peticao_str[-4:])
            
            # Pesquisar Processo
            time.sleep(1)
            self.navegador.find_element(By.ID, "fPP:searchProcessos").click()

            btn_link = WebDriverWait(self.navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/form/div[2]/div[2]/table/tbody/tr/td[2]/a'))
            )
            btn_link.click()

        except Exception as e:

            self.notifier.show_toast("ERRO", "Erro ao pesquisar por Petição", duration=3)
            time.sleep(5)
            print("Erro ao pesquisar petição\n")
            raise      

    def main(self):
        
        time.sleep(3)
        abas = self.navegador.window_handles
        self.navegador.switch_to.window(abas[1])
        
        print("Aba Alterada!!")

        self.navegador.find_element(By.XPATH, '//*[@id="navbar"]/ul/li').click()
        var = self.navegador.find_element(By.XPATH, f'//*[@id="navbar:j_id129"]/li/small/span/span')

        if os.getenv('NOME_DO_POLO') in var.text:
            print("TRUE")

        else:
            print("FALSE")

    def run(self):
        self.navegar()
        self.getNumPeticao("0801948-89.2024.8.19.0068")
        self.main()

try:
    print('incio')
    app = App()
    print('fim')
    
except Exception as e:
    print(f"\n\nERRO AO EXECUTAR AUTOMAÇÃO\n\n")
    print(e)
    
    time.sleep(5)