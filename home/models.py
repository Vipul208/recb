from django.db import models

# Create your models here.

class introbanner(models.Model):
    name = models.CharField(max_length=100)
    designation = models.DateField()
    image = models.ImageField(upload_to="slider")
    link = models.URLField(max_length=400)

    def __str__(self):
        return self.name

class noticeboard(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to="notice")

    def __str__(self):
        return self.subject

class event(models.Model):
    heading = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to="event")

    def __str__(self):
        return self.heading

class lslider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slider")

    def __str__(self):
        return self.title

    
class faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class gallerie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Gallery")

    def __str__(self):
        return self.title

class word(models.Model):
    word = models.CharField(max_length=30)
    meaning = models.CharField(max_length=50)
    example = models.CharField(max_length=500)

    def __str__(self):
        return self.word