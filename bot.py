#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


nome_user = input('digite nome de usuario do instagram: ')
senha_user = input('digite a senha do instagram: ')
URL_Sorteio = input('cole o link do sorteio')

class sorteio_bot:
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.driver = webdriver.Firefox()

    def nome_marcacao(self):

        x = input('deseja adicionar algum @ a lista ? (s/n)')
        if x.lower() == 's':
            cont = int(input('digite a quantidade de pessoas que deseja adicionar a lista'))

            for cont in range(0,cont):
                arroba = input('digite')
                try:
                    arquivo = open('usuarios_instagram.txt', 'a')
                except FileNotFoundError:
                    arquivo = open('usuarios_instagram.txt', 'a')
                arquivo.writelines(arroba + '\n')

            arquivo.close()
        else:
            print('iniciando....')
            
        
    def ler_nomes(self):

        arquivo = open('usuarios_instagram.txt', 'r')
        arroba_insta = arquivo.readlines()
        return arroba_insta

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

        driver.get(URL_Sorteio)

        time.sleep(random.randint(3,6))


    def comentario(self, nomes):

        driver = self.driver
        driver.find_element_by_class_name("Ypffh").click()
        comentario = driver.find_element_by_class_name("Ypffh")
        comentario.clear()
        time.sleep(random.randint(2,5))
        self.digitar(random.choice(instagram.ler_nomes()),comentario)
        driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()

        
    def sair(self):
        self.driver.quit()

        
instagram = sorteio_bot(nome_user, senha_user)
instagram.nome_marcacao()
instagram.login()
while True:
    for tempo in range(0,3):
        instagram.comentario(nomes)
        time.sleep(4)
    time.sleep(300)