import threading
from DataReader import DataReader
from SequenceFinder import SequenceFinder
from collections import Counter

# Caminho para o arquivo de resultados
result_data_path = 'resultados.xlsx'

# Cria uma instância da classe DataReader para ler os dados
reader = DataReader(result_data_path)
vectors_list = reader.data_reader()

# Lock para sincronizar a saída das threads
output_lock = threading.Lock()

# Lock para sincronizar o acesso à lista compartilhada
count2_lock = threading.Lock()

# Lista compartilhada para armazenar os valores de count2 de cada thread, para no fim fazermos uma contagem e obtermos as quantidade de cada sequencia
shared_count2 = []


# Função que será executada por cada thread
def analyze_sequence(vector):
    finder = SequenceFinder(vector)
    # Bloqueia a saída para sincronizar a impressão
    with output_lock:
        print("Vetor:", vector)
        finder.display_sequences()
        print("=" * 50)
    with count2_lock:
        shared_count2.append(finder.count2)


# Cria uma thread para cada vetor e inicia as threads
threads = []
for vector in vectors_list:
    thread = threading.Thread(target=analyze_sequence, args=(vector,))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

#Uso a bibilioteca padrao do python para realizar uma contagem das repetições dos resultados
contagem = Counter()

for vetor in shared_count2:
    contagem.update(vetor)

for numero, repeticoes in contagem.items():
    print(f"Temos {repeticoes} sequencias de  {numero} numeros nos resultados")