from django.shortcuts import render,redirect
from .models import Info

# def ragul(request):
#     return render(request,"N-home.html")
# Create your views here.
def home(request):
    data=Info.objects.all()
    if (data!=''):
        return render(request,"N-home.html",{'datas':data})
    else:
        return render(request,"N-home.html")
def karthi(request):
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']    
        notes=request.POST['notes']

        obj=Info()
        obj.Name=name
        obj.Age=age
        obj.Notes=notes
        obj.save()
        data=Info.objects.all()
        return  render(request,"N-home.html", {'datas':data})

    return render(request,"home.html")
def update(request,id):
    data=Info.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']    
        notes=request.POST['notes']

        
        data.Name=name
        data.Age=age
        data.Notes=notes
        data.save()
        return redirect("home")
        
    return render(request,'update.html',{'data':data})

def delete(request,id):
    data=Info.objects.get(id=id)
    data.delete()
    return redirect("home")

