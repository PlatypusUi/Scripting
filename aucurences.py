import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme',
                    description = 'Ecrit dans un fichier souhaité',
                    )

parser.add_argument('file')           # positional argument
parser.add_argument('-rech', '--rechercher')      # option that takes a value
parser.add_argument('-remp', '--remplacer')      # option that takes a value

args = parser.parse_args()

# Fichier d'entrée
fin = open(args.file, "r")
# Ficher de sortie
fout = open("f2.txt", "w")
# Regarde chaque ligne
for line in fin:
	# remplace les auccurrences
	fout.write(line.replace(args.rechercher, (args.remplacer)))
#ferme les fichiers
fin.close()
fout.close()
