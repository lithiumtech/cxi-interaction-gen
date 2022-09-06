import uuid

class Base:
    # cuz I'm lazy
    def __init__(self,**kwargs): 
        self.uuid = uuid.uuid4()
        for (key,value) in kwargs.items():
            self.__dict__[key] = value

class Chat(Base): 
    pass

class Survey(Base):
    pass

class ProductReview(Base): 
    pass