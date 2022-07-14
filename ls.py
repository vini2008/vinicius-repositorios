#!user/bin/env python3
"""
EXIBE Relatorio de pacientes que estão estão precisam de pouca ajuda do medico,
alunos que precisam de muita ajuda do medico,
e alunos que precisa de ajuda urgente do medico.
"""
__version__ = "0.1.0"

sala1 = {"João", "Derik","Maria","Pedro","Manuel","Sofia"}
sala2 = {"vinicius", "Jamira", "janaina","jose" }

pacientes_pouca_ajuda ={"João", "Jamira", "manuel"}
pacientes_muita_ajuda = ["Derik", "janaina", "Pedro"]
pacientes_ajuda_urgente = ["Vinicius", "Maria", "sofia", "jose"] 

atividades = [
    ("pouca", 'pacientes_pouca_ajuda'),
    ("muita", 'pacientes_muita_ajuda'),
    ("Urgente", 'pacientes_ajuda_urgente'),
]

#listar pacientes em cada atividade por sala

for nome_atividade,  atividade in atividades :

 # sala1 que tem interseção com a atividade
 print(f"pacientes da atividades {nome_atividade}\n")
 print("-" * 40) 

 atividade_sala1 = set(sala1) & set(atividade)
 atividade_sala2 = set(sala2).intersection(atividade)

print("consultorio1", atividade_sala1)
print("consultorio2", atividade_sala2)


print()
print("#" * 40)
