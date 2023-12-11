def cadastrar(boletim):
    aluno = {}
    aluno["nome"] = input("Informe o seu nome: ")
    aluno["disciplina"] = input("Informe a disciplina: ")
    aluno["nota1"] = float(input("Informe a nota do 1° bimestre: "))
    aluno["nota2"] = float(input("Informe a nota do 2° bimestre: "))
    aluno["nota3"] = float(input("Informe a nota do 3° bimestre: "))
    aluno["nota4"] = float(input("Informe a nota do 4° bimestre: "))
    boletim.append(aluno)

def listar(boletim):
    for cadastro in boletim:
      print (cadastro)
      media = (cadastro["nota1"] + cadastro["nota2"] + cadastro["nota3"] + cadastro["nota4"]) / 4
      if media >= 7: 
          print("\nAprovado!")
          print(f"A sua nota final é {media:.1f}\n") 
      else:
         print("Reprovado!")
         print(f"A sua nota final é {media:.1f}\n") 
    
def buscar(boletim):
      pesquisa = input ("Informe o nome do aluno: ")
      for i in boletim:
        if i ["nome"].lower() == pesquisa.lower():
         print(i)
        else:
           print("Não encontrado")   
    
def alterar(boletim):
      alterar = input ("Informe o nome do aluno para alterar os dados: ")
      for p in boletim:
        if p ["nome"].lower() == alterar.lower():
         p["nome"] = str(input("Informe o seu nome: "))
         p["disciplina"] = str(input("Informe a disciplina: "))
         p["nota1"] = float(input("Informe a nota do 1° bimestre: "))
         p["nota2"] = float(input("Informe a nota do 2° bimestre: "))
         p["nota3"] = float(input("Informe a nota do 3° bimestre: "))
         p["nota4"] = float(input("Informe a nota do 4° bimestre: "))
        
def excluir(boletim):
      excluir = input("Informe o nome do aluno para excluir os dados: ")   
      for p in boletim:
        if excluir == p["nome"]:
           boletim.remove(p)
           print("Excluido")
           break