from flask import Flask, render_template, redirect, request
import os
import tabula
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/importar_extrato")
def importar_extrato():
    return render_template('importar_extrato.html')

@app.route("/servicos")
def servicos():
    return render_template('servicos.html')

@app.route('/upload',
 methods=['POST'])
def upload_file():
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo foi enviado'
    file = request.files['arquivo']
    if file.filename == '':
        return 'Nenhum arquivo selecionado'
    if file:
        file.save(os.path.join('uploads', file.filename))
        # Chamar sua função Python aqui
        # Exemplo:
        minha_funcao_python(os.path.join('uploads', file.filename))
        return 'Arquivo enviado com sucesso!'

def minha_funcao_python(caminho_arquivo):
    # Aqui você colocaria o código da sua função para processar o arquivo
    lista_tabela =  tabula.read_pdf(caminho_arquivo, pages="all")
    print("Len tabela" , len(lista_tabela))
    colunas_desejadas_remuneracao = ['Competência','Remuneração','Competência.1','Remuneração.1','Competência.2','Remuneração.2']  # Substitua pelos nomes das suas colunas
    colunas_1 = ['Relações Previdenciárias']
    df_final = pd.concat(lista_tabela, ignore_index=True)
    df_final.to_json('json_completo.json', orient='records')
    
    df_filtrado = df_final[colunas_desejadas_remuneracao]
    df_filtrado.to_json('json_remuneracao.json', orient='records')
    
    df_1 = df_final[colunas_1]
    df_1.to_json('json_rem.json', orient='records')


    
    # Análise exploratória
    print(df_final.head())
    print(df_final.describe())

    # for tabela in lista_tabela:              
    #     arqj = 'minha_tabela'+str(nomearq)+'.json'
    #     tabela.to_json(arqj, index=True)
    #     nomearq = nomearq + 1
    # # tabela.to_csv(arq, index=True)
        
    

    print(f"Arquivo processado: {caminho_arquivo}")    

if __name__ == '__main__':
    app.run(debug=True)