import os


def search_engine():
    print('[1] Bands [2] Movies')

    choice = int(input('Where do you want to search? '))

    def archive(file):
        doc = open(file, 'r')
        word = []

        for line in doc:
            lines = line.strip().title()
            word.append(lines)
        return word

    def search(file):
        search = input('What band you want to know? ').title()

        if search in archive(file):
            print('You already have that on your list')
        else:
            print('You do not have that on your list')

    if choice == 1:
        search(os.path.join("C:\\", "Users", "edu_m", "PycharmProjects", "PersonalRandomizer", "services", "bands.txt"))
    if choice == 2:
        search(os.path.join("C:\\", "Users", "edu_m", "PycharmProjects", "PersonalRandomizer", "services", "movies.txt"))


if (__name__ == '__main__'):
    search_engine()
