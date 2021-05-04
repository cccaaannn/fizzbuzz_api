class api_response:
    def __init__(self, status, info, data):
        self.status = status
        self.info = info
        self.data = data
        
    def get_api_response(self):
        return {
                "status": self.status,
                "info": self.info,                    
                "data": self.data
                }