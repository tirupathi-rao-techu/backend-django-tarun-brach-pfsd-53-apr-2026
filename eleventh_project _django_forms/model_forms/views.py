from django.shortcuts import render
from .forms import EmployeeForm
def register_employee(request):
    # GET Request
    if request.method == "GET":
        form = EmployeeForm()
        return render(
            request,
            "registration.html",
            {
                "form": form
            }
        )
    # POST Request
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        # Form Validation
        if form.is_valid():
            try:
                # Automatic Database Saving
                form.save()
                return render(
                    request,
                    "registration.html",
                    {
                        "form": EmployeeForm(),
                        "success": "Employee Registered Successfully."
                    }
                )
            except Exception as e:
                return render(
                    request,
                    "registration.html",
                    {
                        "form": form,
                        "db_error": str(e)
                    }
                )
        else:
            return render(
                request,
                "registration.html",
                {
                    "form": form
                }
            )
