import boto3
class DynoDb(object):
    def __init__(self,client, resource): 
        self.__resource = resource
        self.__client =client

        return

    def execute_query(self): 
        # make query executoin
        return
