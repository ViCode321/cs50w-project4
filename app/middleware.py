from django.utils import timezone

class ActiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Actualiza la última actividad del usuario
            request.user.last_activity = timezone.now()
            request.user.save()
        response = self.get_response(request)
        return response

