#shebang serve pra manda mesagem pra sistema operaciona
#!/usr/bin/env python3
"""Hello Wold Linguas.
dependeo da lingua cofigurada no ambiente o programa a correpondente.

como user:
export LANG=pt_BR

Execução python3 hello.py
"""
__version__ = "0.0.1"            
__licence__ = "Unlicense" 
__author__ = "Adriano Sales"

import os # trazer modulo de fora pra dentro do programa ou biblioteca externa

current_language = os.getenv("LANG", "en_US")[:5] #procura a variavel LANG dentro DO env e escreve na variavel 
#snake case                               fatiamento --> [:] --> caso a variavel nao exista use a padrao "en_US"

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Olá Mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"   

print(msg)