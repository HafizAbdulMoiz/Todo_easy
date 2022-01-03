from django.shortcuts import redirect, render
from home.models import Todo
# Create your views here.

def home(request):
    todo = Todo.objects.all()
    if request.method=='POST':
        title = request.POST.get('title')
        new_todo=Todo(title=title)
        new_todo.save()
        return redirect('/')
    return render(request,'index.html', {"todos":todo})


def delete(reuqest, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')