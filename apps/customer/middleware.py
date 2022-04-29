from .models import Customer


class ProfileMiddleware:  # este caso de middleware es para crear un customer cada vez que un usuario inicie la seccion
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated and not hasattr(request.user, 'customer'):
            Customer.objects.create(user=request.user)

        response = self.get_response(request)

        return response
