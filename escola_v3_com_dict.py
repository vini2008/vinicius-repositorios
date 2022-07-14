#!/user/bin/env
"""  Exibe relatorio de crianças por atividade.


Inprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""

__version__ = "0.1.1" 

sala1 = {"João", "Derik","Maria","Pedro","Manuel","Sofia"}
sala2 = {"vinicius", "Jamira", "janaina","jose" }

Aula_ingles ={"João", "Jamira", "manuel"}
Aula_musica = ["Derik", "janaina", "Pedro"]
Aula_danca = ["Vinicius", "Maria", "sofia", "jose"] 

atividades = [
    ("Inglês", 'aula_ingles'),
    ("Música", 'aula_musica'),
    ("Dança", 'aula_danca'),
]

#listar alunos em cada atividade por sala

for nome_atividade,  atividade in atividades :

 # sala1 que tem interseção com a atividade
 print(f"alunos da atividades {nome_atividade}\n")
 print("-" * 40) 

 atividade_sala1 = set(sala1) & set(atividade)
 atividade_sala2 = set(sala2).intersection(atividade)

print("Sala1", atividade_sala1)
print("Sala2", atividade_sala2)


print() 
print("#" * 40)
