from .api import api
from .application import ApplicationManager

class AcrosureClient:
    def __init__( self, token, product_id, application_id ):
        self.token = token
        def call_api( path, data ):
            return api( path, data, self.token )

        self.application = ApplicationManager(id = application_id, call_api = call_api)
        # self.product = ProductManager(id = product_id, call_api = call_api)
        # self.policy = PolicyManager(call_api)
        # self.data = DataManager(call_api)

    # def call( self, path ):
    #     try:
    #         resp = api(path, body = None, token = None)
    #         print("SUCCESS")
    #         print(resp)
    #     except Exception as err:
    #         print("ERROR")
    #         print(err)
    
    def call( self, path, data ):
        print("token is " + self.token)
        return api( path, data, self.token )
