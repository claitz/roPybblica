import newspaper

def loadNews(source):
    for article in range(int(articleNum)):
        current_article = source.articles[article]
        current_article.download()
        current_article.parse()
        print('Aggiunto titolo [' + current_article.title + '] dalla source [' + source.brand + '] a ' + newsFileName)
        with open('raw_text/' + newsFileName, 'a') as newsFile:
            newsFile.write('\n')
            newsFile.write(current_article.title)
            newsFile.close()
        print('Fatto.')

def loadSources():
    cache_articles = True
    print ('Carico le fonti, potrebbe volerci un attimo...')
    tpi = newspaper.build(url='https://www.tpi.it/', language='it', fetch_images=False, memoize_articles= cache_articles)
    ilpost = newspaper.build(url='https://www.ilpost.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    internazionale = newspaper.build(url='https://www.internazionale.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    huffpost = newspaper.build(url='https://www.huffingtonpost.it/news/italia-tecnologia/', language='it', fetch_images=False, memoize_articles=cache_articles)
    today = newspaper.build(url='https://www.today.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    milano_today = newspaper.build(url='https://www.milanotoday.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    fanpage = newspaper.build(url='https://www.fanpage.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    focus = newspaper.build(url='https://www.focus.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    leganerd = newspaper.build(url='https://leganerd.com/', language='it', fetch_images=False, memoize_articles=cache_articles)
    giallozafferano = newspaper.build(url='https://blog.giallozafferano.it/community/', language='it', fetch_images=False, memoize_articles=cache_articles)
    techprincess = newspaper.build(url='https://techprincess.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
    mysecretcase = newspaper.build(url='https://www.mysecretcase.com/blog/', language='it', fetch_images=False, memoize_articles=cache_articles)
    
    # repubblica = newspaper.build(url='https://www.repubblica.it/', language='it', fetch_images=False, memoize_articles=False)
    # corriere = newspaper.build(url='https://www.corriere.it/', language='it', fetch_images=False, memoize_articles=False)

    sources = [tpi, ilpost, internazionale, today, milano_today, fanpage, focus, huffpost, leganerd, giallozafferano, techprincess, mysecretcase]

    print('Ok, aggiungo ' + str(articleNum) + ' articoli da ' + str(len(sources)) + ' fonti al file ' + newsFileName)

    for source in sources:
        try:
            loadNews(source)
        except:
            print('Salto la fonte per mancanza di articoli nuovi')
            continue

#### USER PROMPT ####
articleNum = input('Quanti articoli desideri scaricare? [5] ')
newsFileName = input('In quale file vuoi aggiungere gli articoli? [titoli.txt] ')
loadNow = input('Procedere? [Y/n] ')

if articleNum == '':
    articleNum = 5

if newsFileName == '':
    newsFileName = 'titoli.txt'
else:
    newsFileName = newsFileName + '.txt'

if loadNow == '':
    loadNow = 'Y'

if loadNow == 'Y':
    loadSources()
else:
    print('Ok, quando vuoi zi')
