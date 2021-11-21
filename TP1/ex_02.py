choix = int(-1)
borne_inf: int
borne_sup: int
ask_borne = "Entrer la valeur de la borne {value} :\n"
ask_choix = """0 - Quitter le programme
1 - Afficher les valeurs comprises entre les bornes
2 - Afficher les valeurs paires comprises entre les bornes
3 - Afficher les valeurs impaires comprises entre les bornes
Entrer votre choix :\n"""
result = "Valeurs{type} entre les bornes :\n"
wrong_char = "Caractère saisi incorrect"
exit = "Arrêt du programme..."


def list_result(inf, sup, type):
    list_borne = list(range(inf + 1, sup))
    if (inf + 1) % 2 == 0:
        list_paire = [i for i in list_borne[::2]]
        list_impaire = [i for i in list_borne[1::2]]
    else:
        list_paire = [i for i in list_borne[1::2]]
        list_impaire = [i for i in list_borne[::2]]
    switcher = {
        0: exit,
        1: result.format(type="") + str(list_borne) + "\n",
        2: result.format(type=" paires") + str(list_paire) + "\n",
        3: result.format(type=" impaires") + str(list_impaire) + "\n"
    }
    return switcher.get(type, wrong_char)


while choix != 0:
    borne_inf = int(input(ask_borne.format(value="inférieure")))
    borne_sup = int(input(ask_borne.format(value="supérieure")))
    choix = int(input(ask_choix))
    print(list_result(borne_inf, borne_sup, choix))
