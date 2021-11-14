from django.http import HttpResponse

def start_view(request):
    return HttpResponse('<h1>Tu będzie moja biblioteka</h1><p>Więcej już niebawem</p>')