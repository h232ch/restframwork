# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage


@csrf_exempt
def department_api(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(department_id=department_data['department_id'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)

    elif request.method == 'DELETE':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(department_id=department_data['department_id'])
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def employee_api(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employeeSerializer = EmployeeSerializer(data=employee_data)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employee_id=employee_data['employee_id'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employee_id=employee_data['employee_id'])
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['file']
    fileName = default_storage.save(file.name, file)
    return JsonResponse(fileName, safe=False)