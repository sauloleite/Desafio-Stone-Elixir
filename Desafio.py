#Função que irá receber uma lista de compras e uma lista de e-mails. 
def func(listcomps, listemails): #"listcomps" é a lista de compras e "listemails" a de emails
    s = dict() #Criando dicionário da saída de dados
    #Tratando dados recebidos
    listemails = sorted(set(list(filter(None,listemails)))) #Ordenando e eliminando emails repeditos e vazios
    
    #Considerando que a lista de compras terá itens com listas neste formato ['Item', Quantidade, Preço], será realizada uma verificação se todos os itens estão em conformidade
    invalidos = [] #Variável criada para armazenar itens inválidos
    for i in range(len(listcomps)): #Varretura de itens inválidos na lista 
        if len(listcomps[i])<3 or len(listcomps[i])>3: #Verificar caso tenha algum item com uma lista maior ou menor que 3 
           invalidos.append(listcomps[i]) #Armazena este valor na lista "inválidos"
    for i in invalidos:
        listcomps.remove(i) #Removendo itens considerados inválidos
                      
    #Verificador de emails inválidos
    emailserro = [] #Criando lista de emails inválidos p/ removê-los posteriormente
    for i in range(len(listemails)): 
        if((len(listemails[i]) < 3 or len(listemails[i]) > 254)): #Verifica se é um email válido
            emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
        elif(not(listemails[i].count('@'))): #Verifica se é um email válido
            emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
    for i in emailserro: 
        listemails.remove(i) #Remoção de emails inválidos da lista de emails

    #Calcular a soma dos valores, multiplicar o preço de cada item por sua quantidade e somar todos os itens
    somaitens = 0 #Variável criada para armazenar o valor da soma dos itens * preços
    for i in range(len(listcomps)): 
        somaitens = listcomps[i][1]*listcomps[i][2] + somaitens #Soma de itens
    
    #Ajustes para evitar uma divisão por zero
    qtdemails = len(listemails) #Variável criada para evitar divisão por zero
    if(qtdemails==0): #Condição criada para evitar a possibilidade de divisão por 0
        qtdemails = 1 #Atribuindo o valor de 1 para evitar divisão por zero
        
    #Dividir o valor de forma igual entre a quantidade de e-mails
    vpe = int(somaitens/qtdemails) #Valor por email

    #Verificando se não faltará nenhum centavo
    verif = somaitens - vpe*qtdemails #Verificador de "falta" para possível redistribuição
    for j in range(len(listemails)): 
        if(verif == 0): #Condição para verificar se não faltará nenhum centavo
            s[listemails[j]]=vpe
        else: #Caso falte algum centavo, será acrescentado aos últimos valores do dicionário.
            if(j==(qtdemails-verif)): #Verificação do último elemento da lista
                verif -= 1 #Diminui o valor acrescido do verificador
                s[listemails[j]]=vpe+1 #Acréscimo do valor de verificação (1)
            else: #Caso não seja o último, ele segue até chegar a ele e acrescenta o valor 
                s[listemails[j]]=vpe
    return s #retorna o dicionário gerado pela função