# Tipo de Combustível
entrada = int(input())
alcool,gasolina,diesel = 0,0,0
while(entrada!=4):
    if(entrada==1):
        alcool += 1
    elif(entrada==2):
        gasolina +=1
    elif(entrada==3):
        diesel += 1
    entrada = int(input())
    
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(alcool,gasolina,diesel))