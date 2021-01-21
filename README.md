# Desafio Stone Elixir | Saulo Leite

Essa é a descrição do código desenvolvido, na linguagem Python, para o Teste Técnico, para o Programa de Formação em Elixir da Stone.
Segue aqui, também, a lógica usada para resolver o desafio e o guia de como melhor implementar o código.

## Como a solução foi alcançada

Foi desenvolvida uma função que recebe dois parâmetros e posteriormente trata esses dados e retorna um dicionário, conforme foi exigido no desafio. Como o desafio não especificou número máximo de linhas, o código foi desenvolvido de modo que, ao ser implementado, detecta e trata alguns prováveis erros de operação. Por exemplo, caso fosse recebido uma lista com emails duplicados, além da verificação de emails inválidos. Verificação do mesmo cumprimento dos itens/listas da lista de compras, para possíveis reajustes. Na exigência de não faltar nenhum centavo, houve um caso a ser avaliado de redistribuição dos centavos faltantes não somente no último valor, mas nos últimos, em caso de dízimas maiores. Entre outros problemas que foram solucionados e serão melhor explicados no decorrer da descrição.

## Criando a função

A função criada se chama "func". Depois de receber os dois parâmetros, sendo esses as listas de compras e de emails, é criado um dicionário para a saída dos dados desejados. Posteriormente, é realizado o tratamento dos dados recebidos da lista de emails. Esses dados são ordenados alfabeticamente, além de eliminar possíveis itens vazios e emails duplicados, conforme mostra o código abaixo:
```python
#Função que irá receber uma lista de compras e uma lista de e-mails. 
def func(listcomps, listemails): #"listcomps" é a lista de compras e "listemails" a de emails
    s = dict() #Criando dicionário da saída de dados
    #Tratando dados recebidos
    listemails = sorted(set(list(filter(None,listemails)))) #Ordenando e eliminando emails repeditos e itens vazios
#Continua...
```

## Verificador inicial

Este verificador inicial avalia se a lista de compras contém itens com listas com três itens. Em um comentário de uma dúvida de um candidato, o criador do Desafio (Victor Oliveira) respondeu que: "cada item na lista deve ter: **nome: string(); quantidade: inteiro"; preco ou preco_unitario: inteiro**". Desse modo, a "listcomps" (lista de compras) espera receber itens/listas neste formato: ['Item'(str), Quantidade(int), Preço(int)].  Nesse caso, a função espera que a lista de compras contenha listas com três itens. Em outro comentário foi dito pelo Victor que os valores de "Quantidade" e "Preço" sempre serão inteiros. Assim sendo, caso o item/lista possua um comprimento menor ou maior que 3, este item será removido da lista, pois não está em conformidade com o item esperado. Este procedimento é necessário para não atrapalhar nos cálculos que serão melhor explicados posteriormente. Sabemos que não vivemos em um mundo perfeito e um usuário poderá acidentalmente enviar a lista de compras contendo listas vazias e com tamanhos irregulares. Vejamos o código: 

```python
#Considerando que a lista de compras terá itens com listas neste formato ['Item', Quantidade, Preço], será realizada uma verificação se todos os itens estão em conformidade
invalidos = [] #Variável criada para armazenar itens inválidos
for i in range(len(listcomps)): #Varretura de itens inválidos na lista 
    if len(listcomps[i])<3 or len(listcomps[i])>3: #Verificar caso tenha algum item com uma lista maior ou menor que 3 
        invalidos.append(listcomps[i]) #Armazena este valor na lista "inválidos"
for i in invalidos:
    listcomps.remove(i) #Removendo itens considerados inválidos
```

## Verificador de emails inválidos
Antes de realizar os cálculos, são verificados possíveis emails inválidos, já que a função irá trabalhar com estes endereços de correio eletrônicos. Segundo a ITEF (Internet Engineering Task Force), um email válido deve possuir "@", no mínimo 3 e no máximo 254 caracteres (Fonte: https://tools.ietf.org/html/rfc5321#section-4.5.3). Já que não há como saber se a lista de emails já foi avaliada e tradada, essa ação se faz necessária, para que não haja itens que não são emails na lista. Deste modo, é realizada a verificação se o email está dentro destas exigências. Caso não esteja, esse é eliminado da lista de emails, conforme é mostrado no código abaixo: 

```python
#Verificador de emails inválidos
emailserro = [] #Criando lista de emails inválidos p/ removê-los posteriormente
for i in range(len(listemails)): 
    if((len(listemails[i]) < 3 or len(listemails[i]) > 254)): #Verifica se é um email válido
        emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
    elif(not(listemails[i].count('@'))): #Verifica se é um email válido
        emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
for i in emailserro: 
    listemails.remove(i) #Remoção de emails inválidos da lista de emails
```

## Calcular a soma dos valores
A soma dos valores se dá por meio da forma que é exigida no Desafio. É multiplicado o preço de cada item por sua quantidade e somado todos os itens, posteriormente, é armazenado em uma variável. Isso se dá por meio de um laço de repetição "for", que varre todos os itens das listas. Como é selecionado o item de uma lista dentro de uma lista, por esse motivo se faz necessário a verificação se a lista de compras tem itens/listas com o comprimento de três itens, pois os procedimentos aqui realizados contam com isso. Vejamos como fica o código:

```python
#Calcular a soma dos valores, multiplicar o preço de cada item por sua quantidade e somar todos os itens
somaitens = 0 #Variável criada para armazenar o valor da soma dos itens * preços
for i in range(len(listcomps[1])): 
    somaitens = listcomps[i][1]*listcomps[i][2] + somaitens #Soma de itens
```

## Ajustes para evitar uma divisão por zero
Este ajuste é inevitável, pois sem ele, caso a lista de emails recebida esteja vazia, ocorreria uma erro, já que não é possível fazer divisão por zero. Desse modo, a melhor solução foi verificar o comprimento da lista de emails e se ela for 0, mudar para 1, para que assim não ocorra esse erro catastrófico. Caso seja recebida uma lista com zero emails, é retornada uma saída "s" com um dicionário vazio, o usuário deve decidir como irá tratar da validação. Haja vista que não se pode dividir uma valor igualmente para uma quantidade de "zero" emails. Conforme mostra o código:

```python
#Ajustes para evitar uma divisão por zero
qtdemails = len(listemails) #Variável criada para evitar divisão por zero
if(qtdemails==0): #Condição criada para evitar a possibilidade de divisão por 0
    qtdemails = 1 #Atribuindo o valor de 1 para evitar divisão por zero
```

## Dividir o valor de forma igual entre a quantidade de e-mails
Isso faz parte dos requisitos do desafio. Por meio da divisão da soma dos valores pela quantidade de emails, o valor por email obtido é armazenado em uma variável, para que posteriormente possa ser tratado, para sanar as outras exigências. O valor recebe a parte inteira do resultado da divisão da "soma dos valores" sobre a "quantidade de emails". Esta é a parte do código que realiza esse cálculo:

```python
#Dividir o valor de forma igual entre a quantidade de e-mails
vpe = int(somaitens/qtdemails) #Valor por email
```
## Verificando se não faltará nenhum centavo
Para a realização dessa exigência no Desafio, foi criada uma variável para a verificação dos centavos "faltantes". Isso se dá por meio da subtração da soma dos valores, menos o valor por email, multiplicado pela quantidade de emails. Posteriormente, dentro de um laço de repetição, é realizada a verificação se há centavos faltantes ou não. Este laço é realizado conforme o tamanho do comprimento da lista de emails. A verificação avalia o "verificador", se ele for igual a "zero", então não há centavos faltantes, portanto, só é acrescentado ao dicionário a chave e o valor. Caso o valor do verificador seja maior que "zero", ele realiza o acréscimo desses centavos faltantes aos últimos valores do dicionário. Vejamos o código:

```python
#Verificando se não faltará nenhum centavo
verif = somaitens - vpe*qtdemails #Verificador de "falta" para possível redistribuição
for j in range(len(listemails)): 
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
Como exigência do Desafio é importante que não falte nenhum centavo. No guia é descrito o caso de uma dízima de ",333...", mas não é proposto o caso de outras possíveis dízimas. Uma delas é a ",6666...". Neste caso, para que não faltasse nenhum centavo, foi preciso realizar uma distribuição dos centavos faltantes para os últimos valores dos emails. Isso se dá por meio da condição já mostrada acima, onde é feita a verificação se há centavos faltantes e, enquanto houver, estes centavos serão acrescidos aos últimos valores do dicionário. **Quanto maior for a dízima, mais centavos serão redistribuídos para os valores finais, para garantir que não somente o último fique com os centavos faltantes e que não falte nenhum centavo**. Conforme o resultados obtidos abaixo: 
```python
#Exemplo com 3 emails com a dízima de 0,6666...
{'fulano@hotmail.com': 1101,
 'ciclano@yahoo.com': 1102,
 'beltrano@gmail.com': 1102}
```
Neste caso de dízimas maiores, não necessariamente sempre serão os dois últimos valores que receberão os centavos faltantes. Há casos que outros valores mais próximos dos últimos também receberão. Como o exemplo abaixo:

```python
#Exemplo com 5 emails com a dízima de 0,6666...
{'beltrano@outlook.com': 140,
 'billgates@microsoft.com': 140,
 'cilano@uol.com': 141,
 'fulano@hotmail.com': 141,
 'stevejobs@icloud.com': 141}
 ```
A maior dízima possível é a de "0,999...". No caso mostrado abaixo, de nove emails, os centavos faltantes são redistribuídos para os próximos emails posteriores ao primeiro. No entanto, em outros casos, **sempre os valores mais próximos dos últimos receberão os centavos faltantes, até que não falte nenhum centavo**. Em suma, como a maior dízima possível é de "0,999...", não haverá casos de redistribuição de centavos faltantes para além dos oito emails finais. 
 
 ```python
#Exemplo com a dízima de 0,999... (A maior possível)
{'beltrano@outlook.com': 88,
 'billgates@microsoft.com': 89,
 'cilano@uol.com': 89,
 'fulano@hotmail.com': 89,
 'lindo123@yahoo.com': 89,
 'mark@facebook.com': 89,
 'sol@vip.com': 89,
 'stevejobs@icloud.com': 89,
 'zequinha@gmail.com': 89}
```


## ⚠️Como implementar o código⚠️
Após o término de toda construção da função, salvou-se um arquivo chamado "Desafio.py". Para implementar só basta criar um código python para testes (ou usar o já criado presente no zip) na mesma pasta onde ele está e importar o "Desafio" em forma de módulo para o código onde os testes serão realizados. A sintaxe é: "Saída = NomeDoMódulo.Função". No caso deste código, o nome do módulo é "Desafio" e o da função é "func". Não podemos esquecer de importar por meio do comando "import Desafio". Vejamos o código do arquivo "Teste.py", presente na pasta:
```python
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
```
Ao execultar esse código, teremos esse dicionário gerado como resultado:
```python
{'billgates@microsoft.com': 818, 
'linustorvalds@unix.com': 818, 
'stevejobs@icloud.com': 819}
```

## Agradecimentos finais
Gostaria de deixar meus sinceros agradecimentos pela oportunidade de realizar esse desafio. Tenho plena convicção de que me tornei alguém melhor depois de ter vivenciado tudo isso. Foi de grande aprendizado para mim e para minha carreira como Dev. Muito obrigado de verdade, Stone. Espero poder fazer parte da equipe de Devs de vocês, forte abraço.
