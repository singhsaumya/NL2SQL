import json

class Statement:
    tables = []
    NLStatement = ""
    schema = {}
    
    def typeQuery(self):
        self.keywords =['SELECT']
        return
    
    def comparisonOperator(self):
        return
    
    def preprocessor(self):
        self.typeQuery()
        self.comparisonOperator()
        return
    
    def postprocessor(self):
        return 
    
    def generateSQL(self):
        return
     
    
    def convert2SQL(self, nls=None):
        if not nls:
            self.NLStatement = nls
        
        self.prepocessor()
        self.postprocessor()
        self.generateSQL()
        
        return "SELECT * from Table"
    
    
    def getSchema(self, schema):
        if isinstance(schema, str):
            schema = json.loads(schema)
        
        self.tables = schema['tables'].keys()
        return schema
    
    def __init__(self, schema={}):
        self.schema = self.getSchema(schema)
            
