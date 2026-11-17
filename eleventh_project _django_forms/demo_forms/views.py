from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def register_employee(request):
    if request.method == "POST":
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            try:
                Employee.objects.create(
                    name=forms.cleaned_data["name"],
                    email=forms.cleaned_data["email"],
                    mobile=forms.cleaned_data["mobile_number"],
                    department=forms.cleaned_data["department"],
                    salary=forms.cleaned_data["salary"],
                    city=forms.cleaned_data["city"],
                )
                return render(request, "register.html", {"form":EmployeeForm(),"success":"User registred successfully"})
            except Exception as e:
                return render(request, "register.html", {"db_error":str(e)})
        else:
            return render(request, "register.html", {"form":forms})
    else :
        form=EmployeeForm()
        print(form)
        return render(request, "register.html", {"form":form})