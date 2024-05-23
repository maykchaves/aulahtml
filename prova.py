moeda = str(input('Informe a moeda, considere ((e)euro, (d)dolar, (m)peso americano, (a) peso argentino, (l)libra)'))

reais = float(input('Quantos reais deseja converter?'))

if moeda == 'e':
   euros1 = reais / 5.94
   print('euros:', euros1)

elif moeda == 'd':
   dolar1 = reais / 4.97
   print('dolar:', dolar1)

elif moeda == 'm':
   peso = reais / 0.25
   print('peso americano:',peso)

elif moeda == 'a':
   messi = reais / 0.052
   print('peso argentino:', messi)

elif moeda == 'l':
   rony = reais / 6.92
   print('Libras:', rony)

else:
   print('ERRO!!! RENICIE O PROGRAMA')