
from .models import Department, Employee, Task, Project
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Department
        fields = ('name', 'description')
        
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('name', 'email','phone_number','department')

class TaskSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = Task
        fields = ('name', 'description','due_date', 'completed', 'project')
        

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('name', 'description','start_date', 'end_date')