from django.shortcuts import redirect

def api_view(request):
    return redirect('api-root')