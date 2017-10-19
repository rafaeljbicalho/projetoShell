import json

with open('comando.json', 'r') as fd:
    leitura = fd.read()
    teste = json.loads(leitura)
    print teste['comandos'][0]['hello']
    print teste['comandos'][0]['listar']
    print type(teste)
    if teste['comandos'][0]['hello'] == "ola":
        print "AQUIIIIIIII"
    elif teste == "listar":
        print "LISTAR"
