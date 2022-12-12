# Liste des répertoires
# -------------------------------
# import os
# import sys 

# print(sys.argv[0])

# test=os.listdir(sys.argv[1])

# for number,i in enumerate(test):
#     print (f"{number} mon répertoire : {i}")



# Ecrire dans un fichier
# -------------------------------
# with open("text.txt", "a") as f:
#     f.write("Hello World")



#Ecrire dans un fichier
# -------------------------------
# import sys 
# import os

# test=(sys.argv[1])

# with open(test, "w") as f:
#     f.write("Hello World")



#Ecrire dans un fichier
# -------------------------------
# import sys 
# import os

# contenu=(sys.argv[1])
# contenu=contenu+"\n"
# fin=(sys.argv[2])
# try :
#     nbr=(sys.argv[3])
# except :
#     nbr=1

# with open("test.txt", "w") as f:
#     f.write(str(contenu)*int(nbr))
#     f.write(fin)
    


import os
import sys
import re

# # max_ligne=(sys.argv[1])

# fichier="test.txt"
# separateur = re.compile(r"[ \t]")
# # i=0

# with open("test.txt", "r") as f:
#     ligne = f.readline()
#     while ligne != "":
#         # i=i+1
#         decomposition_ligne = separateur.split(ligne)
#         ligne = f.readline()
#         print(ligne)
#         prenom=decomposition_ligne[0]
#         print(decomposition_ligne)
#         print(prenom)
#         nom=decomposition_ligne[1]
#         age=decomposition_ligne[2]
#         with open("test2.txt", "w") as f:
#             f.write(prenom[0]+nom[0]+age)
#         # if i == int(max_ligne) :
#         #     print("fin")

fichier="test.txt"

f = open(fichier, 'r')
text=f.readlines()

for i in text:
    print(i[0])

# for ligne in f:
#     print(ligne[0])
#     while ligne != "":
#         ligne = f.readline()
#         try :
#             print(ligne[0])
#         except :
#             print("Plus de prénom")



