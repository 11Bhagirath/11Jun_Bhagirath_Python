import requests

class internet:
    def __init__(self):
        try:
            url = input("Enter A Url To Check Internet Connection: ")
            if requests.get(url,timeout=5):
                print("Internet Connection Established!")
        except Exception as e:
            print(e)

i = internet()