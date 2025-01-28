import random


class HashTable:
    def __init__(self, size):
        # Inicjalizujemy tablicę o zadanym rozmiarze
        self.size = size
        self.table = [[] for _ in range(size)]  # każda komórka to lista (łańcuch)

    def hash_function(self, key):
        # Funkcja haszująca (modulo), oblicza indeks
        return key % self.size

    def insert(self, key, value):
        # Wstawianie elementu do tablicy
        index = self.hash_function(key)
        self.table[index].append((key, value))  # Wstawiamy parę (klucz, wartość)

    def find_min_max(self):
        # Inicjalizacja zmiennych
        min_key, min_value = None, float('inf')
        max_key, max_value = None, float('-inf')

        # Iteracja przez tablicę
        for chain in self.table:
            for key, value in chain:
                # Porównujemy wartość z najmniejszą i największą
                if value < min_value:
                    min_value = value
                    min_key = key
                if value > max_value:
                    max_value = value
                    max_key = key

        return (min_key, min_value), (max_key, max_value)


# Generowanie losowych danych (id_firmy, wynik_finansowy)
num_companies = random.randint(100, 1000)  # Liczba firm

# Tworzymy tablicę haszującą o rozmiarze 10
hash_table = HashTable(10)

# Generujemy dane dla firm
for _ in range(num_companies):
    company_id = random.randint(1000, 9999)  # Losowy identyfikator firmy (np. NIP)
    financial_result = random.randint(1, 100000000)  # Losowy wynik finansowy
    print(company_id, financial_result)
    hash_table.insert(company_id, financial_result)

# Znajdujemy najmniejszy i największy wynik finansowy
min_element, max_element = hash_table.find_min_max()

print(f"Najmniejszy wynik finansowy: Firma {min_element[0]} z wynikiem {min_element[1]} zl")
print(f"Najwiekszy wynik finansowy: Firma {max_element[0]} z wynikiem {max_element[1]} zl")
