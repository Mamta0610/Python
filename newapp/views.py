from django.shortcuts import redirect,render, get_object_or_404
from .models import Member, Student

def index(request) : 
    mem = Member.objects.all()
    return render(request, 'index.html ',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def list_page(request):
    obj=Student.objects.all()
    return render(request,'list.html',{'obj':obj})

def detail_page(request, id):
    obj=get_object_or_404(Student, pk=id)
    return render(request, 'detail.html', {'obj':obj})

def student_range_list_view(request) :
    queryset = Student.students.get_students_percentage_range(60,70)
    context={
        'object_list':queryset
    }
    return render(request,"list.html", context)

class StudentListView(request):
    queryset = Student.students.name_list()
    contextt ={
         'object_list':queryset
    }
    return render(request,"list.html",contextt)

    def get_queryset(self, *args, **kargs):
        return Student.students.name_list()