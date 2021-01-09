valor =  float(input('Qual o valor da boca dos ape?'))
sal = float(input('qual o seu salário ?'))
tempo = int(input('em quanto tempo (anos) quer pagar?'))
prest = valor / (tempo *12)
if prest <= 0.3 * sal:
    print('o valor das prestações será de {:.2f} mensais durante {} anos '.format(prest, tempo))
else:
    print('infelizmente o capitalismo é uma merda e nao pode te garantir o direito a moradia')
