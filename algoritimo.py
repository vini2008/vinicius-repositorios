#PSEUDO CODIGO
import ir, pegar, pedir, tem, comer, ficar

# Premissas 
today = "Segunda"
hora = 15
natal = False
chovendo = False 
frio = True
nevando = False
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriados = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12,
}

#E -> and (condicao composta com porta lógica AND)
#OU -> or (condicao composta com porta lógica OR)
#NÃO -> not (sinal de negação)

#Se -> If (condicao)
#Senão -> elif (condicao) / else

# A padaria está aberta?

if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora_atual < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora_atual < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda chuva")
        
    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6, "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "pao integral ou baguete")
    else:
        pedir(6, "qualquer pao")
else:
    ficar("casa")
    comer("bolacha")
