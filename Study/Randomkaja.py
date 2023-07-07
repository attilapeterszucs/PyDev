import random

leves = ["Tojás leves", "Paradicsom leves", "Hús leves", "Zöldség leves", "Gyümölcs leves"]
foetel = ["Kentucky csirkeszarny", "S.R.CS krumpli", "Mexicoi", "Gyros", "Töltött krumpli", "Csirke nuggets", "Teszta"]
desszert = ["Melegszendvicses almás pite", "F/K csiga", "Muffin", "Cream Brüüle", "Rakott pancake", "Finn pancake"]

print(f"Leves: {random.choice(leves)}\n"
      f"Főétel: {random.choice(foetel)}\n"
      f"Desszert: {random.choice(desszert)}")