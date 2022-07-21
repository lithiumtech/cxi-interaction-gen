import boto3
class DynoDb(object):
    def __init__(self,client, resource): 
        self.__resource = resource
        self.__client =client

        return

    def execute_query(self): 
        # make query executoin
        return

    def put_item(self, tablename,item):
        self.__client.put_item(
            TableName=tablename,
            Item=item
        )
        return

    def create_item(self): 
        return