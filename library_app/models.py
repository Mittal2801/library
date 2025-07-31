from django.db import models

# Create your models here.

class Book(models.Model):
    bookname = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    isbn = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.bookname
    
    
class Member(models.Model):
    membername = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Issue(models.Model):
    bookname = models.ForeignKey(Book,on_delete=models.CASCADE)
    membername = models.ForeignKey(Member,on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    rtn = models.BooleanField(default=False)
    
    def __str__(self):
        return self.bookname.bookname