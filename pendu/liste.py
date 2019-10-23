# config: utf-8

# demander le nombre d'obs

n = int(input("Nombre d'obs. = "))

# créer une liste vide

lst = []

# ajouter les valeurs

for i in range(0, n):
    lst.append(float(input("Valeur = ")))

# effectuer la somme
somme = 0.0

for i in range(len(lst)):
    somme = somme + lst[i]

# affichage

print(somme)