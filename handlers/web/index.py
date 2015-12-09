import webapp2
import logging

from handlers.web import WebRequestHandler

class ScanQRCodePage(WebRequestHandler):
    def get(self):
        path = 'scan_qr_code.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

class GenerateQRCodePage(WebRequestHandler):
    def get(self):
        path = 'generate_qr_code.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

class QRCodePage(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

app = webapp2.WSGIApplication(
    [
        ('/scan_qr_code', ScanQRCodePage),
        ('/generate_qr_code', GenerateQRCodePage),
        ('/', QRCodePage)
    ]
)