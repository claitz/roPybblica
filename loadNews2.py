import newspaper

repubblica = newspaper.build(url='https://www.repubblica.it/', language='it', fetch_images=False, memoize_articles=False)
corriere = newspaper.build(url='https://www.corriere.it/', language='it', fetch_images=False, memoize_articles=False)

papers = [repubblica, wired_i]
# news_pool.set(papers, threads_per_source=2)
# news_pool.join()

#### USER PROMPT ####
articleNum = input('Quanti articoli desideri scaricare? [5]: ')
newsFileName = input('In quale file vuoi aggiungere gli articoli? [news.txt]: ')
if articleNum == '':
    imgNum = 5

if newsFileName == '':
    newsFileName == 'news.txt'

print('Ok, aggiungo ' + str(articleNum) + ' articoli al file' + newsFileName)


for article in range(int(articleNum)):
    current_article = wired_i.articles[article+21]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a ' + newsFileName)
    with open('raw_text/'+newsFileName, 'a') as newsFile:
        newsFile.write(current_article.title)
        newsFile.write('\n')
        newsFile.close()
    print('Fatto.')

for article in range(int(articleNum)):
    current_article = repubblica.articles[article]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a ' + newsFileName)
    with open('raw_text/'+newsFileName, 'a') as newsFile:
        newsFile.write(current_article.title)
        newsFile.write('\n')
        newsFile.close()
    print('Fatto.')

for article in range(int(articleNum)):
    current_article = corriere.articles[article]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a ' + newsFileName)
    with open('raw_text/'+newsFileName, 'a') as newsFile:
        newsFile.write(current_article.title)
        newsFile.write('\n')
        newsFile.close()
    print('Fatto.')


# for article in wired_i.articles:
#     print(article.title)