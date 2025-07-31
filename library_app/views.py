from django.shortcuts import render, redirect
from .models import Book,Member,Issue
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

def dashboard(request):
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    return render(request, 'dashboard.html', {'total_books': total_books,'total_members': total_members})

def books(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        category = request.POST.get('category')
        isbn = request.POST.get('isbn')
        price = request.POST.get('price')
        
        b = Book(bookname = bookname,category = category,isbn = isbn,price = price)
        b.save()


        return redirect('book') 

    showbook = Book.objects.all() 
    return render(request, 'books.html', {'showbook': showbook})

def member(request):
    if request.method == 'POST':
        membername = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        m = Member(membername = membername,email = email,phone = phone,address = address)
        m.save()

        
        return redirect('member')  

    showmember = Member.objects.all()
    return render(request, 'member_form.html', {'showmember': showmember})

def issue(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        membername = request.POST.get('membername')
        issue_date = request.POST.get('issue_date')
        due_date = request.POST.get('due_date')
        rtn = request.POST.get('rtn') == 'on' 

        book = Book.objects.get(id=bookname)
        print(book)
        member = Member.objects.get(id=membername)
    
        i = Issue(bookname = book,membername = member,issue_date = issue_date, due_date = due_date,rtn = rtn)
        i.save()

        return redirect('issue') 

    books = Book.objects.all()
    members = Member.objects.all()
    issues = Issue.objects.all()

    return render(request, 'issue.html', {'books' : books,'members':members,'issues':issues})
      
def search_page(request):
    if request.method == 'POST':
        book_data = request.POST.get('search')
        book_result = Book.objects.filter(bookname__icontains = book_data)
        print(book_result)
            
        return render(request,'available_book.html',{'book_result':book_result})
    
def register_user(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect(register_user)

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect(register_user)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request,'Account created successfully! Please log in.')
        return redirect(login_user)
    return render(request,'registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('/') 
        else:
            messages.error(request, "Invalid username or password!")
            messages.error(request,"or register your account....")
            return redirect(login_user)
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')
