

class ORMFinalUser(Document):
    component_version_question = StringField(required=True)
    selection = IntField((min_value=None, max_value=None)
