import math
l1,a1,b1,l2,a2,b2,l3= list(map(int,input().split(' ')))

theta1= math.atan((a1/b1)**(1./3.))
theta2= math.atan((a2/b2)**(1./3.))

h1= a1/math.sin(theta1)+b1/math.cos(theta1)
h2= a2/math.sin(theta2)+b2/math.cos(theta2)

print("%.2f" % min(h1,h2,l2+a2+b1))