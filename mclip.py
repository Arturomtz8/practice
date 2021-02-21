# | python3
# mclip.py - A multi-clipboard program

TEXT = {"de acuerdo": """Buenas tardes,
        \n¡Recibido! Comenzamos a procesarlo para su publicación en la fecha de inicio de vigencia. Muchas gracias,
        \nUn saludo,""",

        "duda": """Buenas tardes,
        \n¡Recibido! Comenzamos a procesarlo para su publicación en la fecha de inicio de vigencia, solamente una duda,
        \nUn saludo,""",

        "report": """Hola a todos,
        \nHoy realizamos control,
        \nEso es todo. Nos vemos mañana :),
        """,

        "material": """Muchas gracias, hemos recibido correctamente todo el material. Empezamos a procesarlo.
        \nUn saludo,""",

        "report carr": """Hola a todos,
        \nHoy realizamos overlays de la campaña de Carrefour,
        \nEso es todo. Nos vemos mañana :),
        """,

        "enviar enlaces": """Buenas tardes,
        \nAdjuntamos a continuación los id's de los catálogos publicados hoy en Ofertia:
        \nMuchas gracias,
        \nSaludos""",
        
        "tag" : """Hola, Leslie,
\nEspero te encuentres muy bien. Te he asignado de. Recuerda el tag de Ofertia Welcome y el de Carrefour destacado.
        \nEstaría muy bien que estuvieran listos para. Cualquier duda nos comentas.
        \nMuchas gracias.
        \nUn saludo,
        """,

        "aldi": """el link normal hasta .html 
        + ?utm_source=ofertia 
        + &utm_medium=display
        + &utm_campaign=W42_2020 (la semana que deba ir)
        + &utm_content=link_folleto_robot_aspirador (en este va cambiando de acuerdo al producto que esté)""",

        "pedir enlaces": """Buenas tardes,
        \nRecibimos la campaña de , cuya vigencia comienza el. ¿Nos mandarán enlaces a producto?
        \nNos mantenemos a la espera.
        \nMuchas gracias. Saludos,""",
        
        "cambio":"""Buenas tardes,
        \nAhora hacemos el cambio, muchas gracias por pasar el pdf unificado.
        \nUn saludo,""",

        }


import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Texto for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}.")
