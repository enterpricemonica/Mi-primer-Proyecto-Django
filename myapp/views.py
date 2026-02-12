from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

# 2. Mantenemos la versión de about que pasa el contenido al template
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant..."} 
    return render(request, "about.html", {'content': about_content})

# 3. Mantenemos la versión de menu que usa el template
def menu(request):
    # Aquí puedes personalizar el contenido del menú si lo deseas
    return render(request, "menu.html")

# 4. Actualizamos book para que use el archivo book.html
def book(request):
    return render(request, 'book.html')

# 5. Esta función es vital si estás trabajando con formularios de reserva
def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)