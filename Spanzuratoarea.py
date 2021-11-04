# cuvant = "a _ _ a _ _ t"
# alfabet
# word = "address"
import random
from randon_word import list_of_random_words
# list_of_random_words = ["papagal", "caiet", "calculator"]
word = random.choice(list_of_random_words)
word_list = []
unique_letter = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item)
        # if item in unique_letter:
        #     unique_letter.remove(item)


word_length = len(unique_letter) - 2
print(" ".join(word_list))
count_nr = 1
tried_letters = []
new_word = " ".join(word_list)
while count_nr <= word_length:
    user_letter = input("Alege o litera : ").lower()
    if user_letter == "":
        print("Introdu o litera : ")
        continue
    if user_letter in word_list:
        print("Litera este deja afisata")
    elif user_letter in tried_letters:
        print(f"Litera a fost deja incercata. Literele incercate sunt : {''.join(tried_letters)}")
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))


        else:
            count_nr += 1
        if '_' not in "".join(word_list):
            print("Felicitari ! Ai castigat !")
            break
        elif count_nr > word_length:
            print(f"Ai pierdut ! Cuvantul este : {word}")
        tried_letters.append(user_letter)
