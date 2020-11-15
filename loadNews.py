import newspaper

repubblica = newspaper.build(url='https://www.repubblica.it/', language='it', fetch_images=False, memoize_articles=False)
wired_i = newspaper.build(url='https://www.wired.it/', verbose=True, language='it', fetch_images=False, memoize_articles=False)
corriere = newspaper.build(url='https://www.corriere.it/', language='it', fetch_images=False, memoize_articles=False)

papers = [repubblica, wired_i]
# news_pool.set(papers, threads_per_source=2)
# news_pool.join()

articleNum = 5

for article in range(int(articleNum)):
    current_article = wired_i.articles[article+21]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a news.txt')
    with open('raw_text/news.txt', 'a') as newsFile:
        newsFile.write(current_article.text)
        # newsFile.write('\n')
        newsFile.close()
    print('Fatto.')

for article in range(int(articleNum)):
    current_article = repubblica.articles[article]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a news.txt')
    with open('raw_text/news.txt', 'a') as newsFile:
        newsFile.write(current_article.text)
        # newsFile.write('\n')
        newsFile.close()
    print('Fatto.')

for article in range(int(articleNum)):
    current_article = corriere.articles[article]
    current_article.download()
    current_article.parse()
    print('Titolo: ' + current_article.title)
    print('Aggiungo il testo a news.txt')
    with open('raw_text/news.txt', 'a') as newsFile:
        newsFile.write(current_article.text)
        # newsFile.write('\n')
        newsFile.close()
    print('Fatto.')


# for article in wired_i.articles:
#     print(article.title)