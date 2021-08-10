# standard, don't need to install!
import argparse
# this object will hold all arguments the user passes in
parser_mcgee= argparse.ArgumentParser(description="Describe Chad in one word.")
# acceptable values
acc_adj= ["awesome","stunning","intelligent"]
# add some arguments!
parser_mcgee.add_argument("adj", choices=acc_adj, help="This is the word that describes Chad.")
# add an optional argument
parser_mcgee.add_argument("-a", metavar="ADVERB", default="so", help="'Helper' words, like 'really, very, extremely', etc.")
# have the parser obj turn all those arguments into variables
arglebargle= parser_mcgee.parse_args()
print(f"Chad is {arglebargle.a} {arglebargle.adj}!")

# Lab 50 args parse
