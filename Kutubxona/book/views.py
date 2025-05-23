from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, 'book/home.html')

def book_list(request):
    books=Book.objects.all()
    return render(request,"book/books.html",{'books':books})

def create_book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'book/home.html',{'form':form})
    else:   
        form=BookForm()
    return render(request,'book/create_book.html',{'form':form})

def book_detail(request, id):
    book_detail=Book.objects.get(id=id)
    return render(request,'book/book_detail.html',{'book':book_detail})

def edit_book(request, id):
    book=get_object_or_404(Book, id=id)
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return render(request,'book/book_detail.html',{'book':book})
    else:
        form=BookForm(instance=book)
    return render(request,'book/edit_book.html',{'form':form,'book':book})

def delete_book(request,id):
    book=get_object_or_404(Book,id=id)
    if request.method=="POST":
        book.delete()
        return redirect('books')
    return render(request,'book/delete_book.html',{'book':book})
