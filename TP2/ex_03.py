str_chain = ""

while not str_chain.endswith('.'):
    str_chain += input("Entrer des char (. à la fin pour terminer) :\n")

print("Vous avez saisi : " + str_chain)
print(list(str_chain))

voy_counts = {}
con_counts = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
voyelles = "aeiouy"
consonnes = alphabet.translate(alphabet.maketrans("", "", voyelles))

for voy in voyelles:
    count = str_chain.lower().count(voy)
    voy_counts[voy] = count

for con in consonnes:
    count = str_chain.lower().count(con)
    con_counts[con] = count

print("Il y a {nb_voy} voyelle(s) et {nb_con} consonne(s) dans votre saisie."
      .format(nb_voy=sum(voy_counts.values()), nb_con=sum(con_counts.values())))
