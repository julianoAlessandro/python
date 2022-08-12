print("==================RESOLVA EQUAÇÃO DO 2 GRAU==========================")
a = int(input("Informe o valor de A :"))
b = int(input("Informe o valor de B :"))
c = int(input("Informe o  valor de C :"))
print("sua equação  é : {}X^2 + {}X + {} =  0 ".format(a,b,c))
delta = float((b*b) - 4*a*c)
x1 =( -b + delta**(1/2))/2*a
x2 =( -b - delta**(1/2))/2*a
if delta == 0 :
    print("Teremos apenas uma raiz,pois delta é igual a :{}".format(delta))
    print("Sua única raiz é {}".format(x1))
     
elif delta > 0 :
    print("Teremos 2 raizes,pois delta é {}".format(delta))
    print("Suas 2 raizes serão :  {} e {} ".format(x1,x2))
elif delta < 0:
    print("Não  teremos raizes no campo dos reias,pois meu delta é {:.2f}".format(delta))


