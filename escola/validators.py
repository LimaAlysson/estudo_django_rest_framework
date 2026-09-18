import re 

def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    # 88 99999-9999
    #regex
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    print(resposta)
    return not resposta