from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Tiffany Lindy Adisuryo',
        'npm' : '2206025136',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)