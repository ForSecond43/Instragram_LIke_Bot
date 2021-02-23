from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


#setup para usar webdriver no repl.it
#chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

#driver
path = "D:\WebBrowser_Driver\chromedriver.exe"
driver = webdriver.Chrome(path)
#aqui estou deixando o tamanho do navegador (tamanho da janela)padronizado :)
# pois se a janela for muito pequena o instagram abre a versão 'mobile' ou com layout diferente. Então apenas digo abaixo "Quero que o navegador seja 1024 x 768"
#driver.set_window_size(1024, 768)

url_ig = 'https://www.instagram.com/'
driver.get(url_ig)

sleep(3)
cookies_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
if cookies_btn.is_displayed():
    cookies_btn.click()

sleep(5)

input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

input_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

button_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

#user and pass data - and make login
input_username.send_keys('username') #put your username to login
sleep(1)
input_password.send_keys('Password') #put your password to login
sleep(1)
button_login.click()
#####################################

sleep(10)

not_save = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
if not_save.is_displayed(): # se não houver a tela das notificações vai dar false e avançar
    not_save.click()
else:
    print('dont save desligado!')

sleep(10)
#desativar notification
not_notify = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
if not_notify.is_displayed(): # se não houver a tela das notificações vai dar false e avançar
  not_notify.click()
  print('Notificações desligadas!')
else:
  print('Notificações já desligadas!')
#################################

perfil_url ='https://www.instagram.com/leemaluis/'

driver.get(perfil_url)

sleep(5)
cont = 0
post = driver.find_element_by_class_name('_9AhH0')
post.click()
print('abri o post!')
sleep(2)
next_button = driver.find_element_by_class_name('_65Bje')
while next_button.is_displayed():
    try:
        cont = cont + 1
        print(cont)
        like_button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like_button.click()
        #print('meti like numa foto!')
        sleep(2)
        next_button.click()
        sleep(2)
        next_button = driver.find_element_by_class_name('_65Bje')
        sleep(2)
    except:
        print('Insta stop community!')
        break
    
print ('todos os elementos vistos')