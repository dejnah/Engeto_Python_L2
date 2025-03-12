# BMI = vaha v kg / vyska v m ** 2

#  < 18,5	Podvýživa
#  18,5 – 25	Zdravá váha
#  25 – 30	Mírná nadváha
#  30 – 40	Obezita
#  40 <	Těžká obezita

jmeno = "Martin"
Martin_vaha = 80 # kg
Martin_vyska = 200 # cm

bmi = Martin_vaha / (Martin_vyska / 100) ** 2


if bmi < 18.5:	
 kategorie = "podvýživa"
elif bmi < 25:
  kategorie = "zdravá váha"
elif bmi < 30:
    kategorie = "mírná nadváha"
elif bmi < 40:
    kategorie = "obezita"
elif bmi > 40:
    kategorie = "těžká obezita"
else: 
  kategorie = "špatně zadaná data"

print(jmeno, " má BMI: ", bmi, ", což spadá do kategorie ", kategorie, ".", sep="")
 
# nebo
print(f"{jmeno} tvé BMI je {bmi}, což spadá do kategorie {kategorie}.")
