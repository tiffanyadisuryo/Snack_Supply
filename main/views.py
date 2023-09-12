from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Tiffany Lindy Adisuryo',
        'class': 'PBP D',
        'snacks' : [{'name' : "Chitato", 'amount' : "1", 'description' : "Chitato is a popular Indonesian brand of potato chips known for its wide range of bold and flavorful snack offerings."},
                    {'name' : "Beng Beng", 'amount' : "20", 'description' : "Beng Beng is a well-known Indonesian chocolate snack that combines layers of crispy wafer and creamy chocolate filling, offering a delightful and satisfying treat."},
                    {'name' : "Oreo", 'amount' : "5", 'description' : "Oreo is a globally recognized sandwich cookie brand known for its iconic combination of two chocolate-flavored wafers with a sweet cream filling."}]
    }

    return render(request, "main.html", context)