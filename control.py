from pathlib import Path
from re import compile as cp

busca = cp('\d\d\d\d-\d\d-\d\d')
busca1 = cp('\d\d\d\d')
busca2 = cp('\d\d')
pasta = Path('dados\kp')
indice = [''.join(busca.findall(str(i)))[:4] for i in pasta.glob('*')]    
indice = set(indice)

indice = sorted(indice)

kp_in = ['0+', '1-', '1+', '2-', '2+', '3-', '3+','4-', '4+', '5-', '5+', '6-', '6+', '7-', '7+', '8-', '8+', '9-']
kp_deci = [0.33, 0.67, 1.33, 1.67, 2.33, 2.67, 3.33, 3.67, 4.33, 4.67, 5.33, 5.67, 6.33, 6.67, 7.33, 7.67, 8.33, 8.67]


from calendar import monthrange as mr


def dias(ano):

    """
    Recebe um valor de ano, e retorna os valores dos dias, dos respectivos meses
    ano = 2005
    print(dias(ano))
    Retorna = [..., [...], [335, 336, 337, ...]] equivale aos dias 1, 2 e 3 de dezembro
    """
    
    dia_m = [mr(year=ano, month=i)[1] for i in range(1, 13)]
    dia_a = list(range(1, sum(dia_m)+1))

    e = 0
    sep_dia_mes = []
    for i in dia_m:
        di = dia_a[e:i+e]
        sep_dia_mes.append(di)
        e += i
    return sep_dia_mes

if __name__=='__main__':
    s = dias(2008)
    print(s)
    