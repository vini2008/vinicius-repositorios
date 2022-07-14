#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: Usar função
# TODO: Usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("devops", logging.DEBUG) 
#ch = logging.StreamHandler() # Console/terminal/stderr
#ch.setLevel(log.level)
fh = handlers.RotatingFileHandler("Meu log.log",
maxBytes=300, # 10**6
backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
 "%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"    
)
fh.setFormatter(fmt)
#ch.setFormatter(fmt)
#log.addHander(ch)
log.addHandler(fh)


"""
logging.debug("Mensagem pro dev,qe,sysadmin")
logging.info("mensagem geral para o usuario")
logging.warning("Aviso que não causa erro")
logging.error("erro que afeta uma unica execução")
logging.critical("Erro geral ex: banco de dados sumiu")
"""

print("---")

try: 
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s ",str(e))
    # stound
    # stderr
