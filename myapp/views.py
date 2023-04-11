from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm


def index(req):
    books = Book.objects.all()
    return render(req, "myapp/index.html",{'books':books})

def create(req):
    if req.method == "POST":
        form = BookForm(req.POST, req.FILES)
        if form.is_valid():
            books = form.save(commit=False)
            books.save()
            return redirect('myapp:index')
    else:
        form = BookForm()
    return render(req, 'myapp/create.html', {'form': form})

def update(req,pk):
    books = get_object_or_404(Book, pk=pk)
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES, instance=books)
        if form.is_valid():
            books = form.save(commit=False)
            books.save()
            return redirect('myapp:index')
    else:
        form = BookForm(instance=books)
    return render(req, 'myapp/update.html', {'form':form})

def delete(req,pk):
    books = Book.objects.get(pk=pk)
    books.delete()
    return redirect("myapp:index")









