'''Teste Desafio Stone Elixir
Desenvolvido por: Saulo Leite'''

#Importando o módulo com a função pedida no desafio
import Desafio 

#Lista de compras para testes
l1 = [['Ovos', 'Leite', 'Farinha', 'Fermento'], [1, 1, 1, 1], [140, 765, 540, 200]] 
#Lista de emails para testes
l2= ['zequinha@gmail.com', 'fulano@hotmail.com', 'lindo123@yahoo.com','teste', 'lindo123@yahoo.com', 'lindo123@yahoo.com','lindo123yahoo.com', 's@', 'z@', '@.', '', '´´', '..']

#Chamando a função do módulo com os dois parâmetros 
saida = Desafio.func(l1, l2) #"l1" é a lista de compras e "l2" é a de emails
print(saida)