class Borg(object):
    shared_state = {'y': 2}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls)
        
    