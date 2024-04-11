# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Clase (opcional)
class Teste_produtos():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"

    # 2.2 Funções e Métodos 
    def setup_method(self, method):                 # método de inicialização dos testes
        self.driver = webdriver.Chrome()            # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)             # define o tempo de esperar padrão por elementos em 10 segundos 

    def teardown_method(self):              # método de finalização
        self.driver.quit()                  # encerra / destrói o objeto do Selenium WebDriver da memória 

    def test_selecionar_produto(self):      # método de teste
        self.driver.get(self.url)           # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")     # escreve no campo user_name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")     # escreve a senha 
