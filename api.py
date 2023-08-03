import requests
url = "https://coinpedia.org/news/sec-freezes-assets-of-utah-based-debt-box-in-a-50-million-crypto-fraud-case-involving-bitcoin-and-ether/"
response = requests.get(url)
html_content = response.content
print(html_content)