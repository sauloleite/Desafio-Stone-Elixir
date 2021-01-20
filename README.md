# Desafio Stone Elixir | Saulo Leite

Essa é a descrição do código desenvolvido na linguagem Python para o Teste Técnico para o Programa de Formação em Elixir.
Segue aqui, também, o guia de como melhor implementar o código.

## Como a solução foi alcançada

Foi desenvolvida uma função que recebe dois parâmetros e posteriormente trata esses dados e retorna um dicionário, conforme foi exigido no desafio. Como o desafio não especificou número máximo de linhas, foi desenvolvida uma função que detecta e trata alguns prováveis erros de operação. Por exemplo, caso fosse recebido uma lista com emails duplicados, além da verificação de emails inválidos. Verificação do mesmo cumprimento da lista de "Quantidade de cada item" e "Preço por unidade/peso/pacote de cada item", para possíveis reajustes. Na exigência de não faltar nenhum centavo, houve um caso a ser avaliado de redistribuição dos centavos faltantes não somente no último valor, mas nos últimos, em caso de dízimas maiores. Entre outros problemas que foram solucionados e serão melhor explicados no decorrer da descrição.

## Criando a função

A função criada se chama "func". Depois de receber os dois parâmetros, sendo esses as listas de compras e de email, é criado um dicionário para a saída dos dados desejados. Posteriormente, é realizado o tratamento dos dados recebidos da lista de emails. Esses dados são ordenados alfabeticamente, além de eliminar possíveis itens vazios e emails duplicados, conforme mostra o código abaixo:
```python
#Função que irá receber uma lista de compras e uma lista de e-mails. 
def func(listcomps, listemails): #"listcomps" é a lista de compras e "listemails" a de emails
    s = dict() #Criando dicionário da saída de dados
    listemails = sorted(set(list(filter(None,listemails)))) #Ordenando e eliminando emails repeditos e vazios
#Continua...
```

## Verificador inicial

Este verificador inicial avalia se a lista de compras contém três itens/listas. Nas instruções do desafio é descrito que serão recebidas duas listas e que a lista de compras contará com três listas, não serão enviados valores nulos, mas que poderiam ser enviadas listas vazias. Nesse caso, a função espera que a lista de compras contenha três listas/itens, mesmo que sejam possíveis listas vazias. Caso a lista contenha menos que três itens/listas, ela não irá realizar os outros procedimento e imprimirá uma mensagem dizendo que são necessários três itens/listas na lista. Isso se faz necessário para que não haja erros na realização dos cálculos das somas dos valores, além de que não sejam mostradas mensagens de erros para o usuário, caso ocorra um equívoco. Vejamos o código: 

```python
if(len(listcomps) == 3): #Verificador se a lista contém pelo menos 3 itens/listas
    #Continua...
else:
    print("A lista de compras deve conter 3 itens/listas.")
```

## Verificador das listas de quantidade de itens e preços

Após verificar se a lista de compras possui três itens/listas, é realizada a verificação do comprimento da lista de "quantidade de cada item" e a de "Preço por unidade/peso/pacote de cada item". Caso haja alguma incoformidade, por exemplo, a comprimento da lista de quantidade é mair que a de preços, é acrescido itens a lista com o valor zero, até que o comprimento das listas seja igual. Como o valor acrescido em listas com o comprimento menor é zero, não interfere no cálculo do resultado. Isto só é essencial para que não interfira no processo de multiplicação realizado posteriormente (será melhor explicado depois). Sabemos que não vivemos em um mundo perfeito e um usuário pode enviar uma lista de preços maior que a de quantidade de itens e virse-versa. Vejamos a parte do código que implementa isso:

```python
#Verficador de tamanho das listas "Quantidade de cada item" e "Preço por unidade/peso/pacote de cada item"
if(len(listcomps[1])!=len(listcomps[2])):
    if(len(listcomps[1]) < len(listcomps[2])):
        medida = len(listcomps[2]) - len(listcomps[1])
        for i in range(0, medida):
          listcomps[1].append(0)
     else:
        medida = len(listcomps[1]) - len(listcomps[2])
        for i in range(0, medida):
            listcomps[2].append(0)
```

## Verificador de emails inválidos

Antes de realizar os cálculos, são verificados possíveis emails inválidos, já que a função irá trabalhar com estes endereços de correio eletrônicos. Segundo a ITEF (Internet Engineering Task Force), um email válido deve possuir "@", no mínimo 3 e no máximo 254 caracteres (Fonte: https://tools.ietf.org/html/rfc5321#section-4.5.3). Como não há como saber se a lista de emails já foi avaliada e tradada, essa ação se faz necessária, para que não haja itens que não são emails na lista. Deste modo, é realizada a verificação se o email está dentro destas exigências, caso não esteja, esse é eliminado da lista de emails, conforme é mostrado no código abaixo: 

```python
#Verificador de emails inválidos
emailserro = [] #Criando lista de emails inválidos p/ removê-los posteriormente
for i in range(0, len(listemails)): 
    if((len(listemails[i]) < 3 or len(listemails[i]) > 254)): #Verifica se é um email válido
        emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
    elif(not(listemails[i].count('@'))): #Verifica se é um email válido
        emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
for i in emailserro: 
    listemails.remove(i) #Remoção de emails inválidos da lista de emails
```

## Calcular a soma dos valores
A soma dos valores se dá da forma que é exigida no Desafio. É multiplicado o preço de cada item por sua quantidade e somado todos os itens, posteriormente armazenado em uma variável. Como é selecionado o item de uma lista dentro de uma lista, por esse motivo se faz necessário a verificação se a lista de compras tem três itens/listas, pois os procedimentos aqui realizados contam com isso. Vejamos como fica o código:

```python
#Calcular a soma dos valores, multiplicar o preço de cada item por sua quantidade e somar todos os itens
somaitens = 0 #Variável criada para armazenar o valor da soma dos itens * preços
for i in range(0, len(listcomps[1])): 
    somaitens = listcomps[1][i]*listcomps[2][i] + somaitens #Soma de itens
```

## Ajustes para evitar uma divisão por zero
Este ajuste é inevitável, pois sem ele, caso a lista de emails recebida esteja vazia, ocorreria uma erro, pois não é possível fazer divisão por zero. Desse modo, a melhor solução foi verificar o comprimento da lista de emails e se ela for 0, mudar para 1, para que assim não ocorra esse erro catastrófico. Além disso, é mostrada uma mensagem para o usuário do porquê de um valor retornado vazio. Haja visto que não se pode dividir uma valor igualmente para uma quantidade de "zero" emails. Conforme mostra o código:

```python
#Ajustes para evitar uma divisão por zero
qtdemails = len(listemails) #Variável criada para evitar divisão por zero
if(qtdemails==0): #Condição criada para evitar a possibilidade de divisão por 0
    qtdemails = 1 #Atribuindo o valor de 1 para evitar divisão por zero
    print("Lista sem emails para realização") #Mensagem para avisar o porquê de um S "Vazio"
```

## Dividir o valor de forma igual entre a quantidade de e-mails
Isso faz parte dos requisitos do desafio. É armazenado em uma variável o valor por email obtido por meio da divisão da soma dos valores pela quantidade de emails, para que posteriormente seja tratado para sanar as outras exigências. Esta é a parte do código que realiza esse cálculo:

```python
#Dividir o valor de forma igual entre a quantidade de e-mails
vpe = int(somaitens/qtdemails) #Valor por email
```
## Verificando se não faltará nenhum centavo
Para a realização dessa exigência no Desafio, foi criada uma variável para a verificação dos centavos "faltantes", que se dá por meio da subtração da soma dos valores, menos o valor por email, multiplicado pela quantidade de emails. Posterirmente, dentro de um laço de repetição, é realizada a verificação de se há centavos faltantes ou não. Este laço é realizado conforme o tamanho do comprimento da lista de emails. A verificação avalia o "verificador", se ele for igual a "zero", então não há centavos faltantes, portanto só é acrescentado ao dicionário a chave e o valor. Caso o valor do verificador seja maior que "zero", ele realiza o acréscimo desses centavos faltantes aos últimos valores do dicionário. Vejamos o código:

```python
#Verificando se não faltará nenhum centavo
verif = somaitens - vpe*qtdemails #Verificador de "falta" para possível redistribuição
for j in range(0, len(listemails)): 
    if(verif == 0): #Condição para verificar se não faltará nenhum centavo
       s[listemails[j]]=vpe
     else: #Caso falte algum centavo, será acrescentado ao(s) último(s) valor(es) do dicionário.
          if(j==(qtdemails-verif)): #Verificação do/dos últimos elemento da lista
                verif -= 1 #Diminui o valor acrescido do verificador
                s[listemails[j]]=vpe+1 #Acréscimo do valor de verificação (1)
           else: #Enquanto não chega ao último(s), ele segue até chegar a ele(s) e acrescenta o valor 
                s[listemails[j]]=vpe
 return s #retorna o dicionário gerado pela função
```
## Caso da outras dízimas
Como exigência do Desafio é importante que não falte nenhum centavo. No guia é descrito o caso de uma dízima de ",333..", mas não é proposto de outras possíveis dízimas. Uma delas é a ",6666...". Neste caso, para que não faltasse nenhum centavo, foi preciso realizar uma distribuição dos centavos faltantes para os últimos valores dos emails. Isso se dá por meio da condição já mostrada acima, onde é feita a verificação de se há centavos faltantes e, enquanto houver, estes centavos serão acrescidos aos últimos valores do dicionário. **Quanto maior for a dízima, mais centavos serão redistribuídos para os valores finais, para garantir que não somente o último fique com os centavos faltantes e que não falte nenhum centavo**. Conforme o resultado obtido abaixo: 
```python
{'fulano@hotmail.com': 1101,
 'ciclano@yahoo.com': 1102,
 'beltrano@gmail.com': 1102}
```
## ⚠️Como implementar o código⚠️
Após o término de toda construção da função, salvou-se um arquivo chamado "Desafio.py". Para implementar só basta criar um código python para testes (ou usar o já criado presente no zip) na mesma pasta onde ele está e importar o "Desafio" em forma de módulo para o código onde os testes serão realizados. A sintaxe é: "Saída = NomeDoMódulo.Função". No caso deste código, o nome do módulo é "Desafio" e o da função é "func". Não podemos esquecer de importar por meio do comando "import Desafio". Vejamos o código do arquivo "Teste.py", presente na pasta:
```python
'''Teste Desafio Stone Elixir
Desenvolvido por: Saulo Leite'''

#Importando o módulo com a função pedida no desafio
import Desafio 

#Lista de compras para testes
l1 = [['Ovos', 'Leite', 'Farinha', 'Fermento'], [12, 1, 1, 1], [150, 765, 540, 200]] 
#Lista de emails para testes
l2= ['zequinha@gmail.com', 'fulano@hotmail.com', 'lindo123@yahoo.com','teste', 'lindo123@yahoo.com', 'lindo123@yahoo.com','lindo123yahoo.com', 's@', 'z@', '@.', '', '´´', '..']

#Chamando a função do módulo com os dois parâmetros 
saida = Desafio.func(l1, l2) #"l1" é a lista de compras e "l2" é a de emails
print(saida)
```
Ao execultar esse código, teremos esse dicionário gerado como resultado:
```python
{'fulano@hotmail.com': 3333,
 'lindo123@yahoo.com': 3333,
 'zequinha@gmail.com': 3334}
```

## Por hoje é só, pessoal
Gostaria de deixar meus sinceros agradecimentos pela oportunidade de realizar esse desafio. Tenho plena convicção de que me tornei alguém melhor depois de ter vivênciado tudo isso. Foi de grande aprendizado para mim e para minha carreira como Dev. Muito obrigado de verdade, Stone. Espero poder fazer parte da equipe de Devs de vocês, forte abraço.
