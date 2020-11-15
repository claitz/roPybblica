import newspaper
from newspaper import news_pool

repubblica = newspaper.build(url='https://www.repubblica.it/', language='it', fetch_images=False, memoize_articles=False)
corriere = newspaper.build(url='https://www.corriere.it/', language='it', fetch_images=False, memoize_articles=False)
tpi = newspaper.build(url='https://www.tpi.it/', language='it', fetch_images=False, memoize_articles=False)

papers = [repubblica, corriere, tpi]
news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
news_pool.join()

print(repubblica.articles[10].title)
print(corriere.articles[10].title)
print(tpi.articles[10].title)