from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
           "name": "Employee Name",
            "email": "Employee Email",
            "mobile": "Mobile Number",
            "gender": "Gender",
            "department": "Department",
            "salary": "Salary",
            "city": "City",
            "joining_date": "Joining Date",
            "is_active": "Employee Active Status"
        }
        help_texts = {
            "salary": "Minimum salary should be ₹10,000.",
            "mobile": "Enter exactly 10 digits.",
           "joining_date": "Select employee joining date."
        }
        error_messages = {
            "name": {
                "required": "Employee name is required."
            },
            "email": {
                "required": "Email is mandatory.",
                "invalid": "Enter a valid email address."
            },
            "mobile": {

                "required": "Mobile number is required."
            }
       }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Employee Name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Email"
                }
            ),
            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Mobile Number"
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "department": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "salary": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Salary"
                }
            ),
            "city": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "joining_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            )
        }
   #########################################################
    # Name Validation
    #########################################################
    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError(
               "Name should contain at least 3 characters."
           )
        if len(name) > 50:
            raise forms.ValidationError(
               "Name cannot exceed 50 characters."
           )
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Name should contain only alphabets."
            )
        return name
    #########################################################
    # Email Validation
    #########################################################
    def clean_email(self):
        email = self.cleaned_data["email"]
        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists."
            )
        return email
    #########################################################
    # Mobile Validation
    #########################################################
    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        if not mobile.isdigit():
            raise forms.ValidationError(
                "Mobile should contain only numbers."
            )
        if len(mobile) != 10:
            raise forms.ValidationError(
                "Mobile number should contain exactly 10 digits."
           )
        if Employee.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError(
                "Mobile number already exists."
            )
        return mobile
    #########################################################
    # Salary Validation
    #########################################################
    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        if salary < 10000:
            raise forms.ValidationError(
                "Minimum salary should be ₹10,000."
            )
        if salary > 500000:
            raise forms.ValidationError(
                "Maximum salary should not exceed ₹5,00,000."
            )
        return salary
    #########################################################
    # Joining Date Validation
    #########################################################
    def clean_joining_date(self):
        joining_date = self.cleaned_data["joining_date"]
        from datetime import date
        if joining_date > date.today():
            raise forms.ValidationError(
                "Joining date cannot be a future date."
            )
        return joining_date
    #########################################################
    # Department Validation
    #########################################################
    def clean_department(self):
        department = self.cleaned_data["department"]
        if department == "":
            raise forms.ValidationError(
                "Please select department."
            )
        return department
    #########################################################
    # City Validation
    #########################################################
    def clean_city(self):
        city = self.cleaned_data["city"]
        if city == "":
            raise forms.ValidationError(
                "Please select city."
            )
        return city
    #########################################################
    # Complete Form Validation
    #########################################################
    def clean(self):
        cleaned_data = super().clean()
        department = cleaned_data.get("department")
        salary = cleaned_data.get("salary")
        city = cleaned_data.get("city")
        if department == "HR" and salary:
            if salary < 30000:
                raise forms.ValidationError(
                    "HR employees must have minimum salary of ₹30,000."
                )
        if department == "React" and city:
            if city == "Chennai":
                raise forms.ValidationError(
                    "React department is currently unavailable in Chennai."
                )
        return cleaned_data
