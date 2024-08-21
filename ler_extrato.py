
import tabula
import pandas as pd
import cgi, cgitb

data = cgi.FieldStorage()



# Extraindo todas as tabelas de um PDF para um DataFrame do Pandas
# lista_tabela =  tabula.read_pdf("extrato.pdf", pages="all")
lista_tabela =  tabula.read_pdf("extrato.pdf", pages="all")
print("Len tabela" , len(lista_tabela))
nomearq = 1


for tabela in lista_tabela:      
    arq = 'minha_tabela'+str(nomearq)+'.csv'
    arqj = 'minha_tabela'+str(nomearq)+'.json'
    tabela.to_json(arqj, index=True)
    nomearq = nomearq + 1
    # tabela.to_csv(arq, index=True)
        
    