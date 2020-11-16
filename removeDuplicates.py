import os

def removeDuplicate(file):
    try:
        lines_seen = set() # holds lines already seen
        with open('raw_text/' + file + '2.txt', 'w') as output_file:
            for each_line in open('raw_text/' + file + '.txt', 'r'):
                if each_line not in lines_seen: # check if line is not duplicate
                    output_file.write(each_line)
                    lines_seen.add(each_line)
        os.rename('raw_text/' + file + '2.txt','raw_text/' + file + '.txt')
    except:
        print('File non trovato')
        os.remove('raw_text/' + file + '2.txt')


fileName = input('Da quale file vuoi rimuovere i duplicati? [titoli] ')

if fileName == '':
    fileName = 'titoli'

removeDuplicate(fileName)