from math import cos, radians,sin,tan
an = float(input('Digite o angulo que deseja: '))
r = radians(an)
s = sin(r)
c = cos(r)
t = tan(r)
print('se o angulo for {}\n o SENO sera {:.3f}\n o COSENO sera {:.3f}\n e a TANGENTE sera {:.3f}'.format(an, s, c, t))
#Refazer