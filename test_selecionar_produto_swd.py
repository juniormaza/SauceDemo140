# 1 - Bibliotecass
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
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")       # escreve no campo user_name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")           # escreve a senha 
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click() # clique no botão login

        # transição de página

        # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text ==  "Products"
        # confirma se é a mochila
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" 
         # confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"
        # clica no botão add to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        # clica no carrinho de compras
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
        
        # transição de página

        # confima se está escrito Yoor Cart
        assert self.driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text == "Your Cart"
        # valida quantidade de produtos no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text == "1"
        # confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text == "Sauce Labs Backpack" 
        # confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text == "$29.99"
        # clica no botão remover item do carrinho
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()
        # clica o menu hamburguer 
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        # clicar no logout/encerrar seção
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='logout-sidebar-link']").click()
