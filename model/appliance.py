from google.appengine.ext import db

class Appliance(db.Model):
    name = db.StringProperty(indexed=False)

    @classmethod
    def create(cls, id, name):
        Appliance(key_name=id, name=name).put()

    @classmethod
    def get_by_id(cls, id):
        return cls.get_by_key_name(id)