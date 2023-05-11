from django.http import HttpResponseRedirect
from django.shortcuts import render
from first_app.models import Program, Student
from .forms import StudentForm  



def index(request) :
   fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
   my_dict = {'program_rows' : program_values,
              'student_rows' : student_values,}
   response = render(request, 'index.html', my_dict)
   return response
program_values = Program.objects.all()
student_values = Student.objects.all()

def process_form(request) :
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    print(username, password)
    response = render(request, 'form.html')
    return response   
 
def get_student(request) :
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_year = form.cleaned_data['year']
        s_dob = form.cleaned_data['dob']
        s_degree = form.cleaned_data['degree']
        s_branch = form.cleaned_data['branch']
        print(s_name, s_roll, s_year, s_dob, s_degree, s_branch)
        # Now insert into the model
        p = Program.objects.filter(title=s_degree,branch=s_branch).count()
        if p :
            q = Program.objects.get(title=s_degree,branch=s_branch)
            s = Student(program=q, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            s.save()
        else :
            np = Program(title=s_degree, branch=s_branch)
            np.save()
            s = Student(program=np, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            s.save()
    return HttpResponseRedirect('/student/')
  else:
      form = StudentForm()
      return render(request, 'StudentForm.html', {'form': form})
 


