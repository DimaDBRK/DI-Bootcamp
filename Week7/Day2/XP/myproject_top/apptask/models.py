from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50) #One-to-many with Employee model: One department can have multiple employees, but each employee can only belong to one department.
    description = models.TextField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name =  models.CharField(max_length=50) #(CharField) Many-to-many with Project model: An employee can be assigned to multiple projects, and a project can have multiple employees working on it.
    email = models.EmailField(max_length=50, blank=True, null=True)#(EmailField)
    phone_number = models.CharField(max_length=50, blank=True, null=True)#(CharField)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name = 'departments' ) #(ForeignKey) Many-to-one with Department model: Each employee belongs to one department.

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50) #(CharField)
    description = models.TextField(max_length=150, blank=True, null=True) #(TextField)
    due_date = models.DateField() #(DateField)
    completed = models.BooleanField(default=False) #(BooleanField)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name = 'projects' ) #(ForeignKey) Many-to-one with Project model: Each task is associated with one project, and a project can have multiple tasks.

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=50)#(CharField) #One-to-many with Task model: A project can have multiple tasks, but each task can be associated with only one project.
    description = models.TextField(max_length=150, blank=True, null=True)#(TextField)
    start_date = models.DateField()  #(DateField)
    end_date = models.DateField() #(DateField)

    def __str__(self):
        return self.name