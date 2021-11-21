note1: float  # Première note
note2: float  # Seconde note
somme_notes: float  # Somme des deux notes
coeff1: float  # Premier coefficient
coeff2: float  # Second coefficient
somme_coeffs: float  # Somme des coefficients
moyenne: float  # Moyenne finale
type_moy = int(-1)  # Type de la moyenne
ask_type = """------------------------------
Que voulez-vous calculer ?
(Entrez le caractère correspondant à votre choix)
    0 - Moyenne Simple
    1 - Moyenne Pondérée
------------------------------\n"""
wrong_char = "Le caractère saisi est incorrect."
ask_values = "Veuillez entrer {coeff}la note"
result = "Votre moyenne {type} est :"

while type_moy != 0 and type_moy != 1:
    type_moy = int(input(ask_type))

    if type_moy == 0:
        note1 = float(input(ask_values.format(coeff="") + " 1 :\n"))
        note2 = float(input(ask_values.format(coeff="") + " 2 :\n"))
        somme_notes = note1 + note2
        moyenne = round(float(somme_notes / 2), 2)
        print(result.format(type="simple"), moyenne)

    elif type_moy == 1:
        note1 = float(input(ask_values.format(coeff="") + " 1 :\n"))
        coeff1 = float(input(ask_values.format(coeff="le coefficient de ") + " 1 :\n"))
        note2 = float(input(ask_values.format(coeff="") + " 2 :\n"))
        coeff2 = float(input(ask_values.format(coeff="le coefficient de ") + " 2 :\n"))
        somme_notes = note1 * coeff1 + note2 * coeff2
        somme_coeffs = coeff1 + coeff2
        moyenne = round(float(somme_notes / somme_coeffs), 2)
        print(result.format(type="pondérée"), moyenne)

    else:
        print(wrong_char)
