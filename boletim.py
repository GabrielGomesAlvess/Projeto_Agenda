"""
Uma escola necessita de um programa que armazene as informações dos alunos. Cada aluno possui os seguintes atributos: nome, disciplina, nota1, nota2, nota3, nota4
 
Desenvolva funcionalidades que: 
1) Cadastra os registros 
2) Lista as informações, nesse também deve ser informado a média e a situação desse aluno, se a média for maior ou igual a sete, deverá ser apresentar a palavra "Aprovado", 
senão "Reprovado".
3) Pesquisa pelo nome
4) Alteração. O programa solicitará o nome, se encontrar, o programa solicitará as informações (nome, disciplina, nota1, nota2, nota3, nota4)
5) Excluir. O programa também solicitará o nome para a exclusão
 
9) Sair
"""

from manipulaAluno import alterar, buscar, cadastrar, excluir, listar
from utils import menu
boletim = []

while True:
   menu()
   opcao = int(input("\nInforme a opção: "))
  
   if opcao == 1:
      cadastrar(boletim)
   elif opcao == 2:
      listar(boletim)
   
   elif opcao == 3:
      buscar(boletim)

   elif opcao == 4:
      alterar(boletim)

   elif opcao == 5:
      excluir(boletim)
            
   elif opcao == 9: 
      fechar = input('Deseja fechar o programa? ( S / N ) \n')
      if fechar == 'S' or fechar == "s":
         print("Até logo!")
         break
