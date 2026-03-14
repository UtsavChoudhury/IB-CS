import requests
from seq_search_hw import seq_search
from bin_search_hw import bin_search
import random, time
url = 'https://websites.umich.edu/~jlawler/wordlist'
word = 'medium'

def test_time(algo, key, data):
    start = time.process_time()
    algo(key, data)
    end = time.process_time()

    return end - start


def read_words_from_url(url):

    response = requests.get(url, stream=True)
    words = [word for line in response.iter_lines()
             if (word := line.decode('utf-8').strip()).isalpha()]

    return words

lst = read_words_from_url(url)

print(f'Sequential Search: {test_time(seq_search, word, lst)}')

print(f'Binary Search time: {test_time(bin_search, word, lst)}')



