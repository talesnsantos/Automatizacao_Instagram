#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
nomes = ['@arruda_dayy',
     '@kawamuracarol',
      '@sleitefelipe',
       '@jucimarams',
       '@lee.silva___',
       '@elizatay01',
       '@raffa_goo',
       '@josewillians16',
       '@lucas.tardellii', 
       '@mandynasciment', 
       '@_anamaartins_ ', 
       '@julianafllor__ ', 
       '@mandinharamospvd', 
       '@nath.bartolo', 
       '@bruna.barbieri', 
       '@prazeryara', 
       '@cintiam_santos', 
       '@cintia_marah ', 
       '@franciele3858', 
       '@freitas.cgms', 
       '@ygor_gois',
       '@feleite97']

#url = input(str('digite a url do sorteio: '))
nome_user = input(str('digite nome de usuario do instagram: '))
senha_user = input(str('digite a senha do instagram: '))

class sorteio_bot:
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.driver = webdriver.Firefox()

    def nome_marcacao (arroba):
        quant = int(input('digite a quantidade de pessoas que deseja adicionar a lista'))

        


    @staticmethod
    def digitar(usuarios, campo_comentario):

        for letra in usuarios:
            campo_comentario.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def digitar_login(self,usuarios, campo_usuario):
    
        for letra in usuarios:
            campo_usuario.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def digitar_senha(self,senhas, campo_senha):
    
        for letra in senhas:
            campo_senha.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?hl=pt-br')
        time.sleep(random.randint(2,5))

        usuario = driver.find_element_by_xpath('//input[@name="username"]')
        usuario.click()
        usuario.clear()
        self.digitar_login(nome_user, usuario)

        senha = driver.find_element_by_xpath("//input[@name='password']")
        senha.click()
        senha.clear()
        self.digitar_senha(senha_user,senha)
        
        senha.send_keys(Keys.RETURN)
        time.sleep(random.randint(3,6))

        i = input(str('deseja continuar ?'))
        if i == 's':
            print('continuando')

        driver.get('https://www.instagram.com/p/CGDyK7kgyb6/')

        time.sleep(random.randint(3,6))


    def comentario(self, nomes):

        driver = self.driver
        driver.find_element_by_class_name("Ypffh").click()
        comentario = driver.find_element_by_class_name("Ypffh")
        comentario.clear()
        time.sleep(random.randint(2,5))
        self.digitar(random.choice(nomes),comentario)
        driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()

        #comentario.send_keys(random.choice(nomes))
    def sair(self):
        self.driver.quit()


instagram = sorteio_bot(nome_user, senha_user)
instagram.login()
while True:
    for tempo in range(0,3):
        instagram.comentario(nomes)
        time.sleep(4)
    #instagram.sair()    
    time.sleep(300)
    
 
    # //input[@name="username"]
    # //input[@name="password"]
    # //button[@class="sqdOP  L3NKy   y3zKF"]
    # or
    #//class="Igw0E IwRSH eGOV_ _4EzTm"