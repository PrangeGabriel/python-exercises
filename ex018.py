from math import tan,cos, sin, pi
ang=(float(input('digite um angulo para ver seus valores no circulo trigonometrico: \n')))*pi/180

print('Angulo digitado foi de {:.2} radianos\n,o Seno do angulo é {:.2}\n o Cosseno do angulo é {:.2}\n e a Tangente é {:.2}'.format (ang, sin(ang),cos(ang),tan(ang)))
