from .api import api
from .application import ApplicationManager
from .product import ProductManager
from .policy import PolicyManager
from .data import DataManager

class AcrosureClient:
    """
    Represents an Acrosure API client

    ...

    Attributes
    ----------
    application : class
        A class for application api
    product : class
        A class for product api
    policy : class
        A class for policy api
    data : class
        A class for data api
    token : str
        An access token

    Methods
    -------
    call_api( token = token, path = path, data = data )
        Call Acrosure API with corresponding url & current API key.
    """

    def __init__( self, token, application_id, product_id ):
        """
        Parameters
        ----------
        token : str
            An access token
        application_id : str
            A application id
        product_id : str
            A product id
        """

        self.token = token
        call_api = self.call_api
        # def call_api( path, data = None ):
        #     return api( path, data, self.token )

        self.application = ApplicationManager(id = application_id, call_api = call_api)
        self.product = ProductManager(id = product_id, call_api = call_api)
        self.policy = PolicyManager(id = None, call_api =call_api)
        # self.policy = PolicyManager(call_api = call_api)
        self.data = DataManager(call_api = call_api)
    
    def call_api( self, path, data = None ): # TODO make data mandatory / not callable
        """
        Call Acrosure API with corresponding url & current API key.

        Parameters
        ----------
        path : str
            An API path.
        data : dict
            A data object which is specified by Acrosure.
        """

        return api( path, data, self.token )
