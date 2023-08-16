from newsletter import NewsLetter
from blockchain.models import Subscribers
def SendToSubscribers():
    #모델에서 subscribers끌어와서 리스트로 대치
    subscribers = Subscribers.objects.all() 
    for subscriber in subscribers:
        NewsLetter(subscriber.email)
        print(subscriber + " send")

