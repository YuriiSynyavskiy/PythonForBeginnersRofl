import random
class Ghost(object):
    
    def __init__(self):
        self.color = ['white','yellow','purple','red'][random.randint(0,3)]