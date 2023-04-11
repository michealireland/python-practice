
class Unpackers:

    def __init__(self, a_list):
        self.my_list = a_list
    
    def fist_last_others(self):
        first, *others, last = self.my_list
        return first, others, last


