import pandas as pd


class DataReader:
    import pandas as pd
    def __init__(self, result_data):
        self.result_data = result_data


    def data_reader(self):
        aux = pd.read_excel(self.result_data)

        features = ['Unnamed: 2','Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5',
       'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10',
       'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
       'Unnamed: 15', 'Unnamed: 16']

        result = aux[features].dropna().iloc[1:2898] #Filtro lendo somente as colunas que contem os valores dos resultados removendo os dados que constam como NAN

        vectors_list = [list(row) for _, row in result.iterrows()] #Crio uma lista de vetores, onde cada vetor é uma sequencia dos resultados da loteria

        return vectors_list




# Exemplo de uso
#if __name__ == "__main__":
    #result_data_path = 'resultados.xlsx'
    #reader = DataReader(result_data_path)
    #vectors_list = reader.data_reader()

    # Imprime cada vetor (linha) armazenado na lista
    #for vector in vectors_list:
        #print(vector)