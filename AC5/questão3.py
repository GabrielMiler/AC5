try:
  num1 = int(input("Informe um número inteiro: "))
except ValueError:
    print("Erro na digitação do valor númerico")
else:    
  try:
    num2 = int(input("Informe um segundo número inteiro: "))
  except ValueError:
    print("Erro na digitação do valor númerico")
  else:
    try:  
      divisao = num1 / num2
    except ZeroDivisionError:
      print("Não se pode dividir por 0")   
    else:    
      print("Quociente = ", divisao)  
finally:
    print("Conta encerrada")
