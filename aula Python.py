# # atribuição multipla
# a, b = 1, 2
# print('\nAntes da troca')
# print(f'o valor das variáveis: a={a}, b={b}')
#
# #primeira troca
# temp = a
# a = b
# b = temp
# print('\n primeira troca')
# print(f'o valor das variáveis: a={a}, b={b}')
#
# #segunda troca
# a, b = b, a
# print('\n segunda troca')
# print(f'o valor das variáveis: a={a}, b={b}')

# def multiplicador(numero):
#     a = 2  # esta variável tem escopo local
#     print(f"Dentro da função, a variável vale: {a}")
#     return a * numero
#
#
# a = 3  # esta variável tem escopo global
# b = multiplicador(5)
# print(f"Fora da função, a variável a vale: {a}")

def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # a global será alterado
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
