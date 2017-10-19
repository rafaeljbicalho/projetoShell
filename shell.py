# -*- coding: utf-8 -*-
from cmd import Cmd
from subprocess import call
import os
import json
import time

class MyPrompt(Cmd):
    # função de boas vindas ao usuário
    def do_ola(self, args):
        """ Da boas vindas ao usuário. Caso forneça um nome, dará boas vindas com o nome do usuário"""
        if len(args) == 0:
            name = 'estranho'
        else:
            name = args
        print "Olá, %s" % name

    # função de acesso remoto não implementado
    def do_remoto(self, args):
        """ Acesso remoto """
        print "Para fazer acesso remoto"

    # função para possibilitar o usuário sair da shell
    def do_sair(self, args):
        """ Digite sair para sair do programa"""
        print ("Saindo...")
        raise SystemExit

    # função listar conteúdo do diretório
    def do_listar(self, args):
        """ Comando para listar os arquivos do diretório"""
        call(["ls"])


    # função para realizar uma limpeza na tela
    def do_limpar(self, args):
        """ Comando para limpar as ações realizadas"""
        call(["clear"])

    # função para realizar leitura
    def do_leia(self, args):
        """ Comando para ler comando do arquivo de comandos disponível"""
        print "Abrindo arquivo e realizando leitura..."
        with open ('comando.json', 'r') as fd:
            leitura = fd.read()
            teste = json.loads(leitura)
            if teste['comandos'][0]['hello'] == "ola":
                print "Vou dar boas vindas"
                s = MyPrompt()
                s.do_ola(args)
                time.sleep(4)
                if teste['comandos'][0]['listar'] == "listar":
                    print "Vou listar arquivos"
                    s = MyPrompt()
                    s.do_listar(args)
                    time.sleep(4)
            else:
                print "Não há comandos para executar"
        print "Leitura Concluída"

    # função para exibir data e horário
    def do_data(self, args):
        """ Comando para exibir a data """
        call(["date"])

if __name__ == '__main__':
    prompt = MyPrompt()
    # abre arquivo para verificar qual o nome do prompt
    with open('prompt.txt', 'r') as fd:
        novo = fd.read().strip()
    prompt.prompt = novo
    prompt.cmdloop('Iniciando Shell...')
