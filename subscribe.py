from newsletter import NewsLetter

def SendToSubscribers():
    #모델에서 subscribers끌어와서 리스트로 대치
    subscribers = []
    for subscriber in subscribers:
        NewsLetter(subscriber)
        print(subscriber + " send")

