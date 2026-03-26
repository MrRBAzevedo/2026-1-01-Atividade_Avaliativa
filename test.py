n1, n2, n3, n4, nome = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    situacao = 'Aprovado'
elif 4 <= 4 < 6:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

aluno = {'n1' : n1, 'n2' : n2, 'n3' : n3, 'n4' : n4, 'media' : media, 'situacao' : situacao, 'nome' : nome}

print(f'{aluno['n1']};{aluno['n2']};{aluno['n3']};{aluno['n4']};{aluno['media']};{aluno['situacao']};{aluno['nome']}')