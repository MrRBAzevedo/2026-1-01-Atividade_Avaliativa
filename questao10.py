a = int(input())
b = int(input())
c = int(input())
d = int(input())
media = (a + b + c + d) / 4

print(f'A média é: {media}')

if media >= 6:
    print('Situação: Aprovado(a)!')
else:
    print('Situação: Reprovado(a)!')