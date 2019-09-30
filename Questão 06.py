ida1=ida2=0
total=0
saida=1
while(saida!=0):
    idade=int(input('Informe a idade: '))
    total += 1
    if idade < 18:
        ida1+=1
    if idade == 18 or idade > 18:
        ida2+=1
    saida=int(input('0 sai e 1 continua [0/1]: '))
por1=(ida1*100)/total
por2=(ida2*100)/total
print('Total de pessoas cadatradas: {}, sendo {}% menores de 18 e {}% com ou maiores de 18.'.format(total,por1,por2))