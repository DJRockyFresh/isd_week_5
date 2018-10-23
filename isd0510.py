richter = float(input("Enter magnitude: "))
if richter >=8:
    print("Most structures fall. R.I.P")
elif richter >=7:
    print("Many buildings destroyed")
elif richter >=6:
    print("Many buildings considerably damaged, some collapse")
elif richter >=4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction")
