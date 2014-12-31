from statement import Statement
'''Sample schema ''' 
schema = '\
    {\
        "db_name": "db",\
        "tables":  {\
                    "address":{\
                        "streetAddress": "TEXT ",\
                        "city":"VARCHAR"\
                    },\
                    "phoneNumber": \
                    { \
                        "ext":"INT", \
                        "number":"INT" \
                    } \
        } \
    }'
o=Statement(schema)
o.NLStatement = "give addresses from  city xyz" 
print o.convert2SQL()# one way
print o.convert2SQL("give addresses from  city xyz") # 2nd way
print o.schema['tables'],'\n',o.tables