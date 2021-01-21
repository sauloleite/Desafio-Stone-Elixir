#Função que irá receber uma lista de compras e uma lista de e-mails. 
def func(listcomps, listemails): #"listcomps" é a lista de compras e "listemails" a de emails
    s = dict() #Criando dicionário da saída de dados
    listemails = sorted(set(list(filter(None,listemails)))) #Ordenando e eliminando emails repeditos e vazios
    
    if(len(listcomps) == 3): #Verificador se a lista contém pelo menos 3 itens/listas
        #Verficador de tamanho das listas "Quantidade de cada item" e "Preço por unidade/peso/pacote de cada item"
        if(len(listcomps[1])!=len(listcomps[2])): #Verifica se o comprimento da lista é diferente
            if(len(listcomps[1]) < len(listcomps[2])): #Caso a lista de itens seja maior, a lista de preço será ajustada
                medida = len(listcomps[2]) - len(listcomps[1]) #Esta variável será usada para fazer o ajuste
                for i in range(0, medida): #Laço de repetição para ajustar a lista de itens
                    listcomps[1].append(0) #Serão acrescentados a zeros até que as listas tenham o mesmo comprimento
            else: #Caso a lista de preço seja maior, a lista de itens será ajustada
                medida = len(listcomps[1]) - len(listcomps[2]) #Variável de ajuste
                for i in range(0, medida): #Laço de repetição para ajustar a lista de preços
                    listcomps[2].append(0) #Serão acrescentados a zeros até que as listas tenham o mesmo comprimento

        #Verificador de emails inválidos
        emailserro = [] #Criando lista de emails inválidos p/ removê-los posteriormente
        for i in range(0, len(listemails)): 
            if((len(listemails[i]) < 3 or len(listemails[i]) > 254)): #Verifica se é um email válido
                emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
            elif(not(listemails[i].count('@'))): #Verifica se é um email válido
                emailserro.append(listemails[i]) #Adicionando estes emails a lista de emails inválidos
        for i in emailserro: 
            listemails.remove(i) #Remoção de emails inválidos da lista de emails

        #Calcular a soma dos valores, multiplicar o preço de cada item por sua quantidade e somar todos os itens
        somaitens = 0 #Variável criada para armazenar o valor da soma dos itens * preços
        for i in range(0, len(listcomps[1])): 
            somaitens = listcomps[1][i]*listcomps[2][i] + somaitens #Soma de itens
        
        #Ajustes para evitar uma divisão por zero
        qtdemails = len(listemails) #Variável criada para evitar divisão por zero
        if(qtdemails==0): #Condição criada para evitar a possibilidade de divisão por 0
            qtdemails = 1 #Atribuindo o valor de 1 para evitar divisão por zero
            print("Lista sem emails para realização") #Mensagem para avisar o porquê de um S "Vazio"
        
        #Dividir o valor de forma igual entre a quantidade de e-mails
        vpe = int(somaitens/qtdemails) #Valor por email

        #Verificando se não faltará nenhum centavo
        verif = somaitens - vpe*qtdemails #Verificador de "falta" para possível redistribuição
        for j in range(0, len(listemails)): 
            if(verif == 0): #Condição para verificar se não faltará nenhum centavo
                s[listemails[j]]=vpe
            else: #Caso falte algum centavo, será acrescentado ao(s) último(s) valore(s) do dicionário.
                if(j==(qtdemails-verif)): #Verificação dos últimos elementos da lista
                    verif -= 1 #Diminui o valor acrescido do verificador
                    s[listemails[j]]=vpe+1 #Acréscimo do valor de verificação (1)
                else: #Enquanto não chega ao último(s), ele segue até chegar a ele(s) e acrescenta o valor 
                    s[listemails[j]]=vpe
        return s #retorna o dicionário gerado pela função
    else:
        print("A lista de compras deve conter 3 itens/listas.")