import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())
menor = min(a, b, c, d)
maior = max(a, b, c, d)

print(f'A média aritimética é: {(a + b + c + d) / 4}')
print(f'A diferença entre o menor e o maior valor é: {maior - menor}')