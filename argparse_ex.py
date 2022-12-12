import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme',
                    description = 'Ecrit dans un fichier souhaité',
                    )

# parser.add_argument('emoji')           # positional argument
parser.add_argument('-n', '--nombre', type=int, default=5, choices=range(3,15))      # option that takes a value

args = parser.parse_args()

print(int(args.nombre))

print("\U0001F642\n"*int(args.nombre))
