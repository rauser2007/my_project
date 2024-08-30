import django_setup
from core.models import Student, Subject, Teacher, Class

studs = Student.objects.filter(name = "")






if __name__ == "__main__":
    for s in studs:
        print(f"{s}")