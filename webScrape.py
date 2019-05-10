from newspaper import Article

def getArticle(url):

	article = Article(url)
	article.download()
	article.parse()

	title = article.title
	body = article.text

	return (title, body)

"""article = getArticle('https://timesofindia.indiatimes.com/india/section-377-verdict-a-wrong-is-righted-now-for-the-rights/articleshow/65713180.cms')

print(type(article[0]))
print('--------------------------')
print(type(article[1]))"""


