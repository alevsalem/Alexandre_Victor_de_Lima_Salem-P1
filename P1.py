# Definição : Calcular as raízes de uma equação do 2 grau.

print('Calculadora de equações do segundo grau')
a = float(input('Insira um valor para a variável "a" da equação')
  if(a < 0):
    print('ERRO') # A equação deixará de ser do segundo grau.
  else:
b = float(input('Insira um valor para a variável "b" da equação')
c = float(input('Insira um valor para a variável "c" da equação')

delta_i = (b ** 2) - (4 * a * c)
delta_f = delta_i ** 1/2
  if(delta_f >= 0):
    return 0
    raiz_1 = ( b * -1 + delta_f)/2 * a
    raiz_2 = ( b * -1 - delta_f)/2 * a
      print('Para a equação:',a,'xˆ2',b,'x',c,'\n raiz 1 =',raiz_1,'\n raiz 2 =',raiz_2)
   else:
    return 1
     print('Para estes valores o delta da equação resultará complexo')
