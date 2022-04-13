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

str_reversed = list(str_chain.removesuffix("."))  # Premier string sans . sous forme de list
str_reversed.reverse()  # Inverse l'ordre des éléments de la list
str_reversed = "".join(str_reversed)  # Transforme la list en string
if str_reversed == str_chain.removesuffix("."):
    print("Cette suite de caractères est un palindrome.")
else:
    print("Cette suite de caractères n'est pas un palindrome.")

str_alpha = "".join(list([i for i in str_chain if i.isalpha()]))
str_con = list(str_alpha.translate(str_alpha.maketrans("", "", voyelles)))
print("Voici les consonnes que vous avez saisi :\n", str_con)
