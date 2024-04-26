# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que entro no site Sauce Demo')
@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome() # instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()    # maximizar a janela do navegador 
    context.driver.implicitly_wait(10)  # esperar até 10 segundos por qualquer elmento
    # Passo em si 
    context.driver.get("https://www.saucedemo.com") # abrir o navegador no endereço do site alvo

# Preencher com usuário e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # preencher o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)    # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()         # cliclar no botão login

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2) # espera por 2 segundos - remover depois = alfinete

    # validar se esta na pagina Products
@given(u'que estou na pagina de Products')
def step_impl(context):
     assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    

@when(u'clico no botão Add to cart para adicionar um produto no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()    # clicar no botão add to cart
    

@when(u'clico no icone do carrinho')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() # clicar no icone do carrinho 


@when(u'valido a quantidade de produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "div.cart_quantity[data-test='item-quantity']").text == "1"


@when(u'valido o nome do produto')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "div.inventory_item_name[data-test='inventory-item-name']" ).text == "Sauce Labs Backpack"
   

@when(u'valido o preco do produto')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "div.inventory_item_price[data-test='inventory-item-price']").text == "$29.99"
    


@when(u'clico no botão remover')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']").click()
   

@then(u'clico no menu hamburger e clico em logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()

    # teardown / encerramento 
    context.driver.quit()

# Preencher com usuário em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # não preenche o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)    # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()         # cliclar no botão login

# Preencher com o usuário mais deixar a senha em branco 
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # preencher o usuário
    # não preencho a senha 
    context.driver.find_element(By.ID, "login-button").click()         # cliclar no botão login

# Clica no botão de login sem ter preenchido o usuario e a senha 
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    # não preencho o usuário 
    # não preencho a senha 
    context.driver.find_element(By.ID, "login-button").click()         # cliclar no botão login


# Preencher com usuário e senha através da decisão (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario) # preencher o usuário
        # se o usuário estiver em <branco> não há ação de preenchimento
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)    # preencher a senha
        # se a senha estiver em <branco> não há ação de preenchimento

    context.driver.find_element(By.ID, "login-button").click()         # cliclar no botão login


@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento 
    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    # validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento 
    context.driver.quit()