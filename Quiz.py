#sier velkommen og spør hva du heter og lagrer og bruker det for å si velkommen.
print("Velkommen til dette Quiz-spillet!")
navn = input("Hva heter du? ")
print("Så kjekt at du vil være med " + navn + "!")
poeng = 0

#spør deg spørsmål hvis du får riktig gir deg + 1 poeng og ingen ting hvis du svarer feil.
svar1 = input("Første spørsmål: Hva er hovedstaden i Norge? ")
if svar1.lower() == "oslo":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

svar2 = input("Hva heter Norges nest største by? ")
if svar2.lower() =="bergen":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

svar3 = input("Hva heter det beste fotballaget i Bergen? ")
if svar3.lower() == "brann":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

#her får du en beskjed som vil variere dersom du har mindre eller mere poeng.
print(f"Gratulerer {navn}! Du fikk {poeng} poeng!")
if poeng == 3:
    print("Godt jobbet! Du fikk full pott :)")
elif poeng == 2:
    print("Nokså bra jobbet. Nesten alt riktig :)")
elif poeng == 1:
    print("Du fikk 1 poeng riktig. Neste gang klarer du nok mer :)")
elif poeng == 0:
    print("Du fikk ingen riktige, men du har forhåpetligvis lært litt :)")