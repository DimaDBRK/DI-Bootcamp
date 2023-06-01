from django.db import models
# import date

# Create your models here.
class Todo(models.Model):
# model - table
    title = models.CharField(max_length=50)
    details = models.TextField()
    has_been_done = models.BooleanField(default= False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion  = models.DateField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete= models.CASCADE, related_name='todos') # one to many
    
    def __str__(self):
        return f'{self.category} | {self.title}'
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    image  = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name