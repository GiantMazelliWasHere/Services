import random
import os

def ramdomizer():
    def word_generator(archive):
        word = open(archive, 'r')
        words = []

        for line in word:
            line = line.strip()
            words.append(line)

        word.close()

        number = random.randrange(0, len(words))
        band = words[number].title()
        return band

    print('Randomizers Available:')
    print('[1] Bands [2] Movies')

    choice = int(input('What can I randomize today? '))

    if choice == 1:
        listen = word_generator(os.path.join("C:\\", "Users", "edu_m", "PycharmProjects", "PersonalRandomizer", "services", "bands.txt"))
        print(listen)
    if choice == 2:
        watch = word_generator(os.path.join("C:\\", "Users", "edu_m", "PycharmProjects", "PersonalRandomizer", "services", "movies.txt"))
        print(watch)
    elif choice != choice:
        print('Randomization not Available')


if (__name__ == '__main__'):
    ramdomizer()