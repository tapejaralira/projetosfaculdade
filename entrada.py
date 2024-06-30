""" Microatividade 5 """

from datetime import datetime
name = input('\nDigite seu nome:')
idade = int(input('Digite sua idade:'))

current_year = datetime.now().year
ano_nascimento = current_year-idade

print(f'\nOlá, {name}. Você tem {idade} anos.')
print(f'Você nasceu em {ano_nascimento}.\n')
