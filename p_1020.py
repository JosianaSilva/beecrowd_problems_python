#Idade em dias
def converte_idade_em_dias(idade):
    anos = idade //365
    meses = (idade % 365)//30
    dias = (idade%365) % 30   
    print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos,meses,dias))

idade = int(input())
converte_idade_em_dias(idade)

#ACEITO! 12/12/2021