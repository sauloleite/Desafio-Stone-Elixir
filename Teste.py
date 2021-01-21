'''Teste Desafio Stone Elixir
Desenvolvido por: Saulo Leite'''
#ATENÇÃO: o arquivo: "Desafio.py" deve estar presente na mesma pasta que esse arquivo para poder executá-lo!
#Importando o módulo com a função pedida no desafio
import Desafio 

#A l1 (lista de compras) foi construída da forma que recebe listas com: ['Item'(str), Quantidade(int), Preço(int)]

#Lista de compras para testes com valores aletórios
l1 =[['Ovo', 12, 100], ['Leite', 1, 650], [], ['.'], ['Teste 1'], ['Teste 2', 0] ,['Teste 3', 1,2,3,] ,['Farinha', 1, 375], ['Fermento', 1, 230], ['']]
#Lista de emails para testes com emails aleatórios
l2= ['stevejobs@icloud.com', 'billgates@microsoft.com', 'linustorvalds@unix.com', 'teste' , 'linustorvalds@unix.com', 'linustorvalds@unix.com','linustorvaldsunix.com', 't@', '@', '@.', ' ', '´´', '..']

#Chamando a função do módulo com os dois parâmetros 
saida = Desafio.func(l1, l2) #"l1" é a lista de compras e "l2" é a de emails
print(saida)