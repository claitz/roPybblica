import newspaper

# repubblica = newspaper.build(url='https://www.repubblica.it/', language='it', fetch_images=False, memoize_articles=False)
# corriere = newspaper.build(url='https://www.corriere.it/', language='it', fetch_images=False, memoize_articles=False)

cache_articles = True

tpi = newspaper.build(url='https://www.tpi.it/', language='it', fetch_images=False, memoize_articles= cache_articles)
ilpost = newspaper.build(url='https://www.ilpost.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
internazionale = newspaper.build(url='https://www.internazionale.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
today = newspaper.build(url='https://www.today.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
milano_today = newspaper.build(url='https://www.milanotoday.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
fanpage = newspaper.build(url='https://www.fanpage.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
focus = newspaper.build(url='https://www.focus.it/', language='it', fetch_images=False, memoize_articles=cache_articles)
leganerd = newspaper.build(url='https://leganerd.com/', language='it', fetch_images=False, memoize_articles=cache_articles)
huffpost = newspaper.build(url='https://www.huffingtonpost.it/news/italia-tecnologia/', language='it', fetch_images=False, memoize_articles=cache_articles)
giallozafferano = newspaper.build(url='https://blog.giallozafferano.it/community/', language='it', fetch_images=False, memoize_articles=cache_articles)

sources = [tpi, ilpost, internazionale, today, milano_today, fanpage, focus, leganerd, giallozafferano]

#### USER PROMPT ####
articleNum = input('Quanti articoli desideri scaricare? [5]: ')
newsFileName = input('In quale file vuoi aggiungere gli articoli? [news.txt]: ')
if articleNum == '':
    articleNum = 5

if newsFileName == '':
    newsFileName = 'news.txt'
else:
    newsFileName = newsFileName + '.txt'

print('Ok, aggiungo ' + str(articleNum) + ' articoli al file' + newsFileName)

for source in sources:
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

# for article in wired_i.articles:
#     print(article.title)