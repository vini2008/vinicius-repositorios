"""
Repete Vogais

Faça um programa que pede ao usuario que digite uma ou mais palavras e imprime cada uma das palavras
com vogais duplicadas.

ex:
python repete-vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

words =[]
while True:
   word = input("Digite uma palavra (ou enter para sair):").strip()
   if not word: #condição de parada
        break

   final_word = ""
   for letter in word:
     # TODO: Remover acentuação usandom função 
       
       if letter.lower() in "aeiouãêáúó":
          final_word += letter * 2 
       else:
          final_word += letter 
          """
       final_word += letter * 2  if letter.lower() in "aeiouãêáúó"else letter
       words.append(final_word)""" #---> ternario alternativo 

print(*words, sep="\n")
