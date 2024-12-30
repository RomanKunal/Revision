from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from myapp.models import Student,Feedback
def home(request):
    data = [
        {'name': 'John', 'age': 23},
        {'name': 'Jane', 'age': 25},
        {'name': 'Jack', 'age': 27}
    ]
    
    return render(request, 'home.html', {'data': data})


def aboutus(request):
    return HttpResponse('About Us')

def contact(request, number):
    return HttpResponse(f'Contact Us at {number}')

def userform(request):
    data = {}
    if request.method == "POST":  # Ensure the form submission is POST
        # Safely retrieve form data from POST request
        n1 = request.POST.get('name', 'Anonymous')  # Default to 'Anonymous' if not provided
        n2 = request.POST.get('email', 'Not Provided')
        n3 = request.POST.get('password', 'Not Provided')
        n4 = request.POST.get('gender', 'Not Specified')
        
        # Store the data to display it in the template
        data = {
            'name': n1,
            'email': n2,
            'password': n3,
            'gender': n4
        }
        # Optionally, you can redirect after POST to avoid resubmission on page reload
        return render(request, 'submit.html', {'data': data})  # Pass the data to the template

    # Handle GET request or if no data is posted
    return render(request, 'userform.html', {'data': None})


def submit(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender= request.POST.get('gender')
        data={
            'name':name,
            'email':email,
            'password':password,
            'gender':gender}
    except:
        return HttpResponse('Invalid Request')
    return render(request, 'submit.html', {'data': data})



def marksheet(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject1 = int(request.POST.get('subject1', 0))
        subject2 = int(request.POST.get('subject2', 0))
        subject3 = int(request.POST.get('subject3', 0))
        
        # Calculate total and percentage
        total = subject1 + subject2 + subject3
        percentage = round((total / 300) * 100, 2)

        # Pass values back to template
        context = {
            'name': name,
            'subject1': subject1,
            'subject2': subject2,
            'subject3': subject3,
            'total': total,
            'percentage': percentage,
        }
    return render(request, 'marksheet.html', context)

def student(request):
    # data = Student.objects.all()                  show all data
    #data=Student.objects.all()[:3]      limiting
    # data=Student.objects.all().order_by('name')      ascending order
    #data=Student.objects.all().order_by('-name')     #descending order
    # data=Student.objects.all().filter(name='Manas')   #filtering
    # data=Student.objects.all().filter(name__contains='a')   #filtering
    #data=Student.objects.all().filter(name__startswith='M')   #filtering
    #data=Student.objects.all().filter(name__endswith='s')   #filtering
    # data=Student.objects.all().filter(name__icontains='a')   #filtering
    #data=Student.objects.all().filter(gender__exact='male')   #filtering
    # data=Student.objects.all().filter(age__gt=18)
    #data=Student.objects.all().filter(age__gte=18)
    # data=Student.objects.all().filter(age__lt=18)
    #data=Student.objects.all().filter(age__lte=18)
    # data=Student.objects.all().filter(age__range=(18,25))
    #data=Student.objects.all().exclude(age__range=(18,25))
    # data=Student.objects.all().exclude(name='Manas')
    #data=Student.objects.all().exclude(name__contains='a')
    # data=Student.objects.all().exclude(name__startswith='M')
    data=Student.objects.all().exclude(name__endswith='s')

    return render(request, 'student.html', {'data': data})

def feedback(request):
    data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        feedback = request.POST.get('description')
        f = Feedback(name=name, age=age, city=city, feedback=feedback)
        f.save()
        data = {
            'name': name,
            'age': age,
            'city': city,
            'feedback': feedback
        }
        return render(request, 'feedback.html', {'data': data})
    return render(request, 'feedback.html', {'data': None})