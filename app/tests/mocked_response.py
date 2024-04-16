class MockedResponse:
    
    def __init__(self, json_data, status_code) -> None:
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data