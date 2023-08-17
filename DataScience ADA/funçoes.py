#Criação de Funções

#Função inicial

def saudacao():
    print('Seja bem-vinda(o)!') 
    print('Olá, é um prazer ter você fazendo parte desse curso')


saudacao()
saudacao() 
saudacao()


#Função com parámetros
def saudacao (nome, curso):
    print(f'Seja bem-vinda(o), (nome)!') 
    print(f'olá, é um prazer ter você fazendo parte do curso de (curso)!')

saudacao ('Thaina', 'Python')

saudacao ('Aline', 'JavaScript')

# default
def saudacao(nome, curso='Python'):
    print('seja bem-vinda(o), (nome)!')
    print(f'olá, é um prazer ter você fazendo parte do curso de (curso)!')
saudacao('Thaina', 'C++')

#retorno
def soma (num1,num2):
    return num1+num2

resultado = soma (5, 7)

print('o resultado da soma é', resultado)

def calculadora (num1, num2, operacao='+'):
    if operacao =='+':
        return num1 + num2
    elif operacao=='-':
        return num1 - num2
