class ApplicationManager:
    def __init__( self, id, call_api ):
        self.id = id
        self.call_api = call_api

    def set_id(self, id):
        self.id = id

