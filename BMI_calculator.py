poids = input("Indiquez votre poids : ")
taille = input("Indiquez votre taille en mètre : ")

poids = int(poids)
taille = float(taille)

IMC = poids / taille**2
IMC = int(IMC)

print (f"Votre IMC est de {IMC}")

if IMC < 18.4:
  print("Votre IMC est en dessous de 18.4, vous êtes trop maigre.")
elif 18.5 <= IMC <= 24.9:
  print("Votre IMC est compris entre 18.5 et 24.9, vous avez le poids idéal.")
elif 25 <= IMC <= 29.9:
  print("Votre IMC est compris entre 25 et 29.9, vous êtes en surpoids.")
elif 30 <= IMC <= 34.9:
  print("Votre IMC est compris entre 30 et 24.9, vous êtes en obésité modérée.")
elif 35 <= IMC <= 39.9:
  print("Votre IMC est compris entre 35 et 39.9, vous êtes en obésité sévère.")
else:
  print("Votre IMC est au dessus de 40, vous êtes en obésité morbide.")
  
  
