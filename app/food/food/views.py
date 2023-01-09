from django.shortcuts import redirect





def redirect_diet(request):
    return redirect('diet_url', permanent=True)