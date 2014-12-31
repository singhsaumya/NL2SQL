import json

class Statement:
    tables = []
    NLStatement = ""
    schema = {}
    
                     
    def getSchema(self, schema):
        if isinstance(schema, str):
            schema = json.loads(schema)
        
        self.tables = schema['tables'].keys()
        return schema
    
    def __init__(self, schema={}):
        self.schema = self.getSchema(schema)
    def convert2SQL(self, nls=None):
        if not nls:
            self.NLStatement = nls
        
        return "SELECT * from Table"
        
