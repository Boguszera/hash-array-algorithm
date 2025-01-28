import random
import time

class HashTable:
    def __init__(self, size):
        # Inicjalizujemy tablicę o zadanym rozmiarze
        self.size = size
        self.table = [[] for _ in range(size)]  # każda komórka to lista (łańcuch)

    def hash_function(self, key):
        A = 0.6180339887
        fractional_part = (key * A) % 1
        return int(self.size * fractional_part)

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

# Pomiar czasu działania
def measure_performance(num_companies, table_size):
    hash_table = HashTable(table_size)

    # Generowanie danych dla firm
    companies = [
        (random.randint(1000, 9999), random.randint(1, 100000000))
        for _ in range(num_companies)
    ]

    # Wstawianie elementów i pomiar czasu
    start_insert = time.time()
    for company_id, financial_result in companies:
        hash_table.insert(company_id, financial_result)
    end_insert = time.time()

    # Znajdowanie min i max i pomiar czasu
    start_find = time.time()
    min_element, max_element = hash_table.find_min_max()
    end_find = time.time()

    return {
        "num_companies": num_companies,
        "table_size": table_size,
        "insert_time": end_insert - start_insert,
        "find_time": end_find - start_find,
        "min_element": min_element,
        "max_element": max_element,
    }

# Przeprowadzanie testów
def run_tests():
    test_results = []
    for num_companies in [100, 1000, 10000, 100000]:
        for table_size in [10, 101, 1009, 10007]:  # Różne rozmiary tablicy (liczby pierwsze)
            result = measure_performance(num_companies, table_size)
            test_results.append(result)
            print(f"Liczba firm: {num_companies}, Rozmiar tablicy: {table_size}")
            print(f"Czas wstawiania: {result['insert_time']:.6f}s, Czas znajdowania min/max: {result['find_time']:.6f}s")
            print(f"Najmniejszy element: {result['min_element']}, Największy element: {result['max_element']}")
            print("-" * 50)
    return test_results

# Uruchamianie testów
if __name__ == "__main__":
    results = run_tests()
