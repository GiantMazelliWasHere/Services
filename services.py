import randomizer
import searchEngine

def services():
    print('Services available:\n [1] Randomizer [2] Search Engine')
    service = int(input('What service do you wish to use? '))

    if service == 1:
        randomizer.ramdomizer()
    elif service == 2:
        searchEngine.search_engine()
    else:
        print('Service not Available')

if (__name__ == '__main__'):
    services()