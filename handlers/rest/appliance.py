import webapp2
import json
import logging
from handlers.request_handler import RequestHandler
from model.appliance import Appliance

class AddApplianceHandler(RequestHandler):
    def post(self):
        id = self['id']
        name = self['name']
        Appliance.create(id, name)

class GetApplianceHandler(RequestHandler):
    def post(self):
        id = self['id']
        appliance = Appliance.get_by_id(id)
        if appliance:
        	self.write(json.dumps({'id': id, 'name':appliance.name}), 200, 'application/json')

app = webapp2.WSGIApplication([
    ('/api/appliance/add', AddApplianceHandler),
    ('/api/appliance/get', GetApplianceHandler)
])