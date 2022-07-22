from django.shortcuts import render
from core.forms import BookForm
from core.models import Book 


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'partials/bookform.html', {'form': BookForm()})
            response['HX-Trigger'] = 'bookAdded'
            return response
        return render(request, 'partials/bookform.html', {'form': form})
    context = {'form': BookForm(), 'books': Book.objects.all()}
    return render(request, 'index.html', context)


def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'partials/booklist.html', context)