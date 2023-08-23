class SequenceFinder:
    def __init__(self, arr):
        self.arr = arr  # Armazena o array fornecido como atributo da classe
        self.count2 = []


    def find_sequences(self):
        sequences = []  # Lista para armazenar as sequências encontradas
        current_sequence = []  # Lista temporária para construir sequências

        for num in self.arr:  # Percorre cada número no array
            if not current_sequence or num == current_sequence[-1] + 1:
                # Se a lista está vazia ou o número é o próximo na sequência
                current_sequence.append(num)  # Adiciona o número à sequência atual
            else:
                if len(current_sequence) > 1:
                    sequences.append(current_sequence.copy())  # Adiciona sequência à lista de sequências
                current_sequence = [num]  # Começa uma nova sequência

        if len(current_sequence) > 1:
            sequences.append(current_sequence)  # Adiciona a última sequência à lista

        return sequences  # Retorna a lista de sequências encontradas

    def display_sequences(self):
        result = self.find_sequences()  # Encontra as sequências no array
        length_count = {}  # Dicionário para contar quantas vezes cada comprimento ocorre

        for sequence in result:
            sequence_length = len(sequence)
            if sequence_length in length_count:
                length_count[sequence_length].append(sequence)  # Adiciona a sequência ao comprimento correspondente
            else:
                length_count[sequence_length] = [sequence]  # Cria uma nova entrada para o comprimento

        for length, sequences in length_count.items():
            count = len(sequences)  # Conta quantas vezes ocorre o mesmo comprimento
            self.count2.append(count)
            # Exibe a mensagem formatada com a contagem, comprimento e sequência
            print(f"{count} sequências de {length} {'números' if length > 1 else 'número'}")