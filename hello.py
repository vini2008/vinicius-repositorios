#!/usr/bin/env python3
"""Hello world Multi Linguas.

 dependendo da lingua configurada no ambiente o programa exibe a mensagem
 correspondente.

 como usar : 

 tenha a variavel LANG devidamente configurada ex:

       export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
""" 
__version__ = "0.1.3"
__author__ = "Marcus Vinicius"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("devops", logging.DEBUG) 
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
 "%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"    
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
   try: 
      key, value = arg.split("=")
   except ValueError as e:
       # TODO: Logging
       log.error(
          "you need to use '=', you passed %s, try --key=value: %s",
          arg.
          str(e)
       )
       sys.exit(1)

       key = key.lstrip("-").strip()
       value = value.strip()

       # validação
       if key not in arguments:
          print("Invalid Option '{key}'")
          sys.exit()
          
          arguments[key] = value
      
current_language = arguments["lang"]
print(f"{current_language=}")
if current_language is None:
  #TODO: Usar repetição
   if "LANG" in os.environ:
       current_language = os.getenv("LANG")
   else:
      current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello,World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao, mondo",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde",
}

"""
# try com valor default
message = msg.get(current_language,msg["en_US"])
"""

# EAFP
try:
      message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] str(e)")
    print(f"Languge is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
     message * int(arguments["count"])
)
 

