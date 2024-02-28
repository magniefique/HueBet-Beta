class Delay():
    def __init__(self):
        self.ctr_value = 0
        self.return_value = None
    
    # delays an instance in the program
    def delay(self, speed:int, max_value:int):
        if self.ctr_value < max_value:
            self.ctr_value += speed
            self.return_value = False
        else:
            self.return_value = True
        
        return self.return_value
    
    # resets delay
    def reset(self):
        self.ctr_value = 0