from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def teacher(request):
    context = {
        'room_name': 'saturday12345kumar',
        'name': 'Mukesh kumar',
        'subject': 'physics',
    }
    return render(request, 'teacher.html', context)

def student(request):
    context = {
        'room_name': 'saturday12345kumar',
        'name': 'Mukesh kumar',
        'subject': 'physics',
    }
    return render(request, 'student.html', context)