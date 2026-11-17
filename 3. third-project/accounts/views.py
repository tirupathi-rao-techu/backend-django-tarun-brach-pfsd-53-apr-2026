from django.shortcuts import render

# Create your views here.
def homePage(request):
    content = {
        "name":"rehman singh",
        "age":26,
        "qualification":"MCA",
        "courses": ["HTML", "CSS", "Bootstrap", "JavaScript", "React"],
        "is_active":True,
        "salary":35000
    }
    return render(request, "index.html", content)

def coursesPage(request):
    return render(request, "courses.html")