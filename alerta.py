"""
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

se temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

"ALERTA!!! 🥵 ♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

"ALERTA!!! 🥵 ♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."
"""
import logging

log = logging.Logger("alerta") 


def is_completely_filled(dict_of_inputs):
  """Return a boolean telling if a dict is completely filled. """
  info_size = len(dict_of_inputs)
  filled_size = len(
    [value for value in dict_of_inputs() if value is not None]
    )
  return  info_size == filled_size

        
info = {
    "temperatura": None,
    "umidade": None}

while True:
    
    if is_completely_filled(info):
        break

    for key in info.keys(): # ["temperatura", "umidade"]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%S Invalida, digite numeros", key)
            break # para o for

temp, umidade = info.values() # unpacking [30, 90]

if temp > 45: 
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp >30 and temp * 3 >= umidade:
    print("ALERTA!!! 🥵 ♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10 :
    print("🥶 Frio")
elif temp < 0:
    print( "ALERTA!!! ⛄ Frio Extremo.")
