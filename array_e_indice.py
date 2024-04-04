def imprimir_nomes():
  nomes = ["João", "Maria", "Fulano", "Ciclano"]
  print("1 -", nomes[0])
  print("2 -", nomes[1])
  print("3 -", nomes[2])
  print("4 -", nomes[3])

imprimir_nomes()


def imprimir_primeiro_ultimo():
  nomes = ["João", "Maria", "Fulano", "Ciclano"]
  print("1 -", nomes[0])
  print("4 -", nomes[-1])

imprimir_primeiro_ultimo()

def imprimir_segundo_terceiro():
  nomes = ["João", "Maria", "Fulano", "Ciclano"]
  print("2 -", nomes[1])
  print("3 -", nomes[2])

imprimir_segundo_terceiro()

def substituir_alimentos():

  alimentos = ["Macarrão", "Pepino", "Batata"]

  alimentos[0] = input("Digite o primeiro alimento: ")
  alimentos[1] = input("Digite o segundo alimento: ")
  alimentos[2] = input("Digite o terceiro alimento: ")
  
  print("1 -", alimentos[0])
  print("2 -", alimentos[1])
  print("3 -", alimentos[2])

substituir_alimentos()