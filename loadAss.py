import newspaper

def loadNews(source):
    for article in range(int(articleNum)):
        current_article = source.articles[article]
        current_article.download()
        current_article.parse()
        print('Aggiunto titolo [' + current_article.title + '] dalla source [' + source.brand + '] a ' + newsFileName)
        with open('raw_text/' + newsFileName, 'a') as newsFile:
            newsFile.write(current_article.title)
            newsFile.write('\n')
            newsFile.close()
        print('Fatto.')

def loadSources():
    cache_articles = True
    print ('Carico le fonti, potrebbe volerci un attimo...')
    arstechnica = newspaper.build(url='https://arstechnica.com/', language='en', fetch_images=False, memoize_articles= cache_articles)
    scientology = newspaper.build(url='https://www.scientologynews.org/', language='en', fetch_images=False, memoize_articles= cache_articles)
    theverge = newspaper.build(url='https://www.theverge.com/', language='en', fetch_images=False, memoize_articles= cache_articles)
    cnn = newspaper.build(url='https://www.cnn.com/', language='en', fetch_images=False, memoize_articles= cache_articles)

    sources = [arstechnica, scientology, theverge, cnn]

    print('Ok, aggiungo ' + str(articleNum) + ' articoli da ' + str(len(sources)) + ' fonti al file ' + newsFileName)

    for source in sources:
        try:
            loadNews(source)
        except:
            print('Salto la fonte per mancanza di articoli nuovi')
            continue

#### USER PROMPT ####
articleNum = input('Quanti articoli desideri scaricare? [5] ')
newsFileName = input('In quale file vuoi aggiungere gli articoli? [ass.txt] ')
loadNow = input('Procedere? [Y/n] ')

if articleNum == '':
    articleNum = 5

if newsFileName == '':
    newsFileName = 'ass.txt'
else:
    newsFileName = newsFileName + '.txt'

if loadNow == '':
    loadNow = 'Y'

if loadNow == 'Y':
    loadSources()
else:
    print('Ok, quando vuoi zi')
