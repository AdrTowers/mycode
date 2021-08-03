#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }

char_name = input("Which character do you want to know about? (Starlord, Mystique, She-Hulk)").title()

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)").lower()

print(marvelchars[char_name],"'s ", marvelchars[char_name][char_stat], " is: " )
