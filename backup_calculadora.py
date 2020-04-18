# coding: utf-8

print ("""\
    Escolha uma das operacoes:
    +: Para somar.           -: para subtrair.
    /: para dividir.         *: para multiplicar.
    r: para calcular raiz de equacao do segundo grau.    
    """)

ope = raw_input('Escolha uma operacao: ')

if ope == '+':
    valor1 = int(input('Difite o primeiro numero: '))
    valor2 = int(input('Digite o segundo numero: '))
    resultado = valor1 + valor2
    print ('o resultado: ')
    print (resultado)
elif ope == '-':
    valor1 = int(input('Digite o primeiro numero: '))
    valor2 = int(input('Digite o segundo numero: '))
    resultado = valor1 - valor2
    print ('o resultado: ')
    print (resultado)
elif ope == '*':
    print('Na multiplicacao de numeros que nao sao inteiros usasse o "." no lugar da virgula')
    valor1 = float(input('Digite o primeiro numero: '))
    valor2 = float(input('Digite o segundo numero: '))
    resultado = valor1 * valor2
    print ('o resultado: ')
    print resultado
elif ope == '/':
    valor1 = float(input('Digite o primeiro numero: '))
    valor2 = float(input('Digite o segundo numero: '))
    resultado = valor1 / valor2
    print ('o resultado: ')
    print resultado
else:
    print('')
if ope == 'r' :
  valora = int(input('valor de A:  '))
  valorb = int(input('valor de B:  '))
  valorc = int(input('valor de C:  '))
  delta = (valorb ** 2) + ((-4) * valora * valorc)
if delta >= 0 :
      x1 = ((-1) * (valorb) + (delta ** 0.5)) / ((2) * (valora) * (valorb))
      x2 = ((-1) * (valorb) - (delta ** 0.5)) / ((2) * (valora) * (valorb))
      print('Valor de x1 igual a: ')
      print x1
      print('valor de x2 igual a: ')
      print x2
      repetir = raw_input('Deseja fazer outra operacao?')
else :
    print ('Delta e negativo, nao tem raiz!')
    repetir = raw_input('Deseja fazer outra operacao?')

#(delta - ((-1) * delta)) == 0: