from cmd import Cmd
from subprocess import call

class MyPrompt(Cmd):

    def do_remoto(self, args):
        """Para fazer acesso remoto"""

    def do_sair(self, args):
        """Para sair da Shell digite sair"""
        print ("Saindo...")
        raise SystemExit

    def do_listar(self, args):
        """Para listar um diretorio"""
        call(["ls"])

    def do_limpar(self, args):
        """Para limpar a tela"""
        call(["clear"])

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'Teste@Shell> '
    prompt.cmdloop('Iniciando Shell...')
def do_listar(self, args):
        """Para listar um arquivo..."""
