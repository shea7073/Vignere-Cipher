from nltk import trigrams
import operator
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import tkinter as tk


ciphertext = input("Enter cipher text: ")
ciphertext = ciphertext.upper()
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.replace(".", "")
ciphertext = ciphertext.replace(",", "")
ciphertext = ciphertext.replace("'", "")
ciphertext = ciphertext.replace('"', "")
ciphertext = ciphertext.rstrip()

#print(ciphertext)
trigrams = trigrams(ciphertext)
list_trigrams = []
map_trigrams = {}
map_distance = {}
list_distance = []

for gram in trigrams:
    list_trigrams.append(gram)

index = 0

for x in list_trigrams:
    count = list_trigrams.count(x)
    index += 1
    if count > 3:
        map_trigrams[x] = count
        if x not in map_distance.keys():
            map_distance[x] = [index]
        else:
            map_distance[x].append(index)

#print(map_trigrams)
#print(map_distance)

j = 0
for key in map_distance.keys():
    distances = []
    for i in range(len(map_distance)):
        try:
            distance = map_distance[key][i+1] - map_distance[key][i]
            distances.append(distance)
        except IndexError:
            break

    list_distance.append(distances)

#print(list_distance)

possible_factors = []

for sublist in list_distance:
    for num in sublist:
        for i in range(5, 10):
            if num % i == 0:
                possible_factors.append(i)

print(possible_factors)

frequency_map = {}

k = 0

for factor in possible_factors:
    count = possible_factors.count(factor)
    frequency_map[factor] = count

#print(frequency_map)

maximum = max(frequency_map.items(), key=operator.itemgetter(1))[0]


#print(maximum)

seperated_strings = []

new_ciphertext = ciphertext

master_strings = []

for k in range(maximum):
    single_string = []
    for i in range(k, len(new_ciphertext), maximum):
        single_string.append(new_ciphertext[i])
    master_strings.append(single_string)


print(master_strings)

sorted_strings = []

for lst in master_strings:
    string = ""
    for letter in lst:
        string += letter
    new = sorted(string)
    sorted_list = sorted(new, key=lambda c: new.count(c), reverse=True)
    final_msg = "".join(sorted_list)
    sorted_strings.append(final_msg)

#print(sorted_strings)

alphabet_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
base_freq_y = [8.12, 1.49, 2.71, 4.32, 12.02, 2.3, 2.03, 5.92, 7.31, .1, .69, 3.98, 2.61, 6.95, 7.68, 1.82, .11, 6.02, 6.28, 9.1, 2.88, 1.11, 2.09, .17, 2.11, .07]


size = len(sorted_strings)

frequencies = []

for string in sorted_strings:
    freq = {}
    for letter in alphabet_x:
        counter = string.count(letter)
        freq[letter] = counter/len(string)*100
    frequencies.append(freq)

#print(frequencies)

fig, axs = plt.subplots(4, 2)
axs[0, 0].bar(alphabet_x, base_freq_y)
axs[0, 0].set_title('Base')
axs[0, 1].bar(alphabet_x, frequencies[0].values())
axs[0, 1].set_title('Letter 1')
axs[1, 0].bar(alphabet_x, frequencies[1].values())
axs[1, 0].set_title('Letter 2')
axs[1, 1].bar(alphabet_x, frequencies[2].values())
axs[1, 1].set_title('Letter 3')
axs[2, 0].bar(alphabet_x, frequencies[3].values())
axs[2, 0].set_title('Letter 4')
axs[2, 1].bar(alphabet_x, frequencies[4].values())
axs[2, 1].set_title('Letter 5')
axs[3, 0].bar(alphabet_x, frequencies[5].values())
axs[3, 0].set_title('Letter 6')
axs[3, 1].bar(alphabet_x, frequencies[6].values())
axs[3, 1].set_title('Letter 7')
#text_box = TextBox(axs[4, 0], 'Enter key once analyzed')

for ax in axs.flat:
    ax.set(xlabel='Letters', ylabel='Frequency')

fig.tight_layout()
plt.show()

key = input('Please enter key: ')

to_decode = master_strings

decoded_strings = []

alphabet_decode = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L' : 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
count = 0
for string in to_decode:
    decoded_string = ''
    current = key[count]
    current = current.upper()
    offset = alphabet_decode.get(current) - 1
    for letter in string:
        if alphabet_decode.get(letter) - offset >= 26:
            new_letter = alphabet_x[alphabet_decode.get(letter) - offset - 26]
        else:
            new_letter = alphabet_x[alphabet_decode.get(letter) - offset - 1]
        decoded_string += new_letter
    decoded_strings.append(decoded_string)
    count += 1

print(decoded_strings)

final_string = ''


for i in range(0, len(decoded_strings[0])):
    for string in decoded_strings:
        try:
            final_string += string[i]
        except IndexError:
            continue


print(final_string)
