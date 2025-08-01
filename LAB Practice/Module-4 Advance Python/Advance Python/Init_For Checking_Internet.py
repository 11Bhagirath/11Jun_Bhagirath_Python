import requests

class internet:
    def __init__(self):
        url = "https://www.instagram.com/"
        '''if requests.get(url):
            print("Internet Connection Is ON!")
        else:
            print("No Internet Connection Found!")'''
        
        try:
            requests.get(url,timeout=10)
            print("Internet Connection Established!")

        except Exception as e:
            print(e)

i=internet()
    