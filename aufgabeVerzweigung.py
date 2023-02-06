# Ich erstelle das Bankkonto 
balance = 0
# ich erstelle den Input und Output des Kontos über Input
depositionInput = input('Einzahlen: ')
balance = depositionInput
print(depositionInput)
withdrawingInput = input('Abheben: ')
balanceminuswithdraw = balance - int(withdrawingInput)

# Ich gebe an was Ausgegeben werden soll<<
if withdrawingInput > balance: 
    print('sorry but you cant withdraw right now, your request is higher than your deposit, Youve got ' + balanceminuswithdraw + "on youre account")
else: print('you"ve withdrawed youre money, thanks for your visit')
print(f'du hast ' + balance + '€ auf dem Konto')

