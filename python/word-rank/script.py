# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

from collections import Counter

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]


def count_freq(word_list):
    words = []

    for i in word_list:
        splited_words = i.split()
        for n in splited_words:
            small_worlds = n.lower()
            words.append(small_worlds)
    counted = Counter(words).most_common(3)

    print(
        f"""\n
        Wyniki najczęstrzych wyrazów: \n 
        1. "{counted[0][0]}", wykorzystany: {counted[0][1]} razy,\n
        2. "{counted[1][0]}", wykorzystany: {counted[1][1]} razy,\n 
        3. "{counted[2][0]}", wykorzystany" {counted[2][1]} razy. \n 
        -------------------------------""")


count_freq(sentences)

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

# Good luck! You can write all the code in this file.
