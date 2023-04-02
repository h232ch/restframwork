from rest_framework import serializers
from company.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'department_name')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'employee_name', 'department',
                  'date_of_joining', 'photo_file_name')


class EmployeeGetSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(required=False)
    # ep_department_name = serializers.CharField(source='department.department_name')

    class Meta:
        model = Employee
        fields = ('employee_id', 'employee_name', 'department',
                  'date_of_joining', 'photo_file_name')