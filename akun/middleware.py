from django.shortcuts import redirect
from django.urls import path, reverse

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and path == reverse('akun:login'):
            return redirect('akun:home')
        response = self.get_response(request)
        return response