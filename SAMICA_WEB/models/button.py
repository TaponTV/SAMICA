class button:
    
    def __init__(self, **kwargs):
        self.listButtons = {}
        for (key, button) in kwargs.items():
            self.listButtons[key] = button
    

    