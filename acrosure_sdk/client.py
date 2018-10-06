from .api import api

class Client:
    def call(path):
        try:
            resp = api(path)
            print("SUCCESS")
            print(resp)
        except Exception as err:
            print("ERROR")
            print(err)
