from application.models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'admin' not in request.path:
            a = Logger()
            a.path = request.path
            if request.method == 'POST':
                a.method = 'POST'
                a.body = request.POST
            else:
                a.method = "GET"
                a.query = request.GET
            a.save()
        response = self.get_response(request)
        return response
