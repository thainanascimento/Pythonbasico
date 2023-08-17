#estrutura condicionais
"""
imprimir aprovado ou reprovado nota maior ou menor que 7
"""
#if = si
#else = entao
#and = e
#or = ou
#: = enter, aparece as 4 bolinhas na linha de baixo
#.... = tudo que estiver ali ser excultado de acordo com o que voce pediu
idade = 26
if idade >= 18:
    print('voce é maior de idade.')
else:
    print('voce é maior de idade.')


media = float(input('informe a nota do estudante: '))
if media >= 7:
    print('voce foi aprovada(o)')
elif media >= 5:
    print ('recuperaçao')
else:
    print('voce foi reprovada(o)')

media = 5
presenca = 50

if media >= 7 and presenca >= 70:
    print('reprovada(o)!')
    print('aprovada(o)!')
else:
    print('aprovada(o)!')
    print('tente novamente')




