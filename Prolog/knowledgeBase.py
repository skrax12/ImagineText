from pyswip import Prolog
import readandwrite

#from imagineText import search_images_on_google

#https://www.youtube.com/watch?v=1jwAHIz8WXc

prolog = Prolog()
prolog.consult("Prolog_PeopleAndPlaces.pl")

#truth = bool(list(prolog.query("place(home)")))
#facts = (list(prolog.query('connection(City1, City2, Distance)')))

readandwrite.read('Prolog_PeopleAndPlaces.pl')

def facttostringold():
    predicate = str(input_data).split('(')[0]
    data = ''
    for item in output_data:
        count = 1
        for x, y in item.items():
            if count % 2:
                data = data + ';' + predicate + ': ' + x + '. ' + y
                count += 1
            else:
                data = data + ': ' + x + '. ' + y

while(True):
    input_data = input('Prolog command: ')

    output_data = list(prolog.query(input_data))

    output_data = str(output_data)

    print(output_data)

    output_data = output_data.replace('\'','')
    output_data = output_data.replace(']','')
    output_data = output_data.replace('[','')
    output_data = output_data.replace(',','')
    #output_data = output_data.replace('\'','')
    print(output_data)

#   data = []
#   data = ''
#
#   for item in output_data:
#       for x, y in item.items():
#           data = data + ': ' + x + ', ' + y
#   print(data)
        
    #for fact in output_data:
    #    fact1 = []
    #    print(fact)
    #    for atom in fact:
    #        print(atom)
    #        fact1.append(atom)
    #    data.append(fact1)
    #print(data)