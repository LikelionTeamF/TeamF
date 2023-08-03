from newspaper import Article


def GetNewsContent(url):
    #크롤링할 url 주소 입력
    #url = 'https://coinpedia.org/news/ethereums-security-status-remains-uncertain-making-xrp-the-only-crypto-with-legal-clarity/'
    #언어가 한국어이므로 language='ko'로 설정
    a = Article(url, language='en')
    a.download()
    a.parse()

    #기사 내용 가져오기(150자)
    print(a.text[:1000])
    return a.text[:1000]