balance = 0
depositionInput = input('Einzahlen: ')
balance = depositionInput
withdrawingInput = input('Abheben: ')
kreditwuerdig = None

with open("creditworthy.py", "r")  as file:
    ergebnis == file.read()
    if ergebnis == True:
        kreditwuerdig = True

if withdrawingInput > balance and ergebnis == False: 
    print('sorry but you cant withdraw right now, your request is righer than your deposit')
elif 
else: print('you"ve withdrawed youre money, thanks for your visit')
print(f'du hast ' + balance + '€ auf dem Konto')

