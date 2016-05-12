from marshmallow import Schema, fields, pprint

class PartySchema(Schema):
    children = fields.String()
    value = fields.String()

class MainSchema(Schema):
    select_party = fields.Nested(PartySchema, many=True)
    

class Party(object):
    def __init__(self, children, value):
        self.children = children
        self.value = value
