import os 
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_schedule.settings")
django.setup()

from core.models import Subject, Teacher, Class, Student

def add_subject():
    name = input("Введіть назву предмету: ")
    description = input("Введіть опис предмету: ")

    if Subject.objects.filter(name=name).exists():
        print("Такий предмет вже існує!")
    else:
        Subject.objects.create(name=name, description=description)
        print(f"Предмет '{name}' успішно додано.")

def add_teacher():
    name = input("Введіть ім'я вчителя: ")
    subject_name = input("Введіть назву предмету, який викладає вчитель: ")

    try:
        subject = Subject.objects.get(name=subject_name)
    except Subject.DoesNotExist:
        print("Предмет не знайдено! Спочатку додайте предмет.")
        return
    
    Teacher.objects.create(name=name, subject=subject)
    print(f"Вчитель '{name}' успішно додано.")

def add_class():
    name = input("Введіть назву класу: ")
    year = input("Введіть рік навчання: ")

    if Class.objects.filter(name=name, year=year).exists():
        print("Такий клас вже існує!")
    else:
        Class.objects.create(name=name, year=year)
        print(f"Клас '{name}' ({year}) успішно додано.")

def add_student():
    name = input("Введіть ім'я учня: ")
    class_name = input("Введіть назву класу, до якого належить учень: ")

    try:
        class_group = Class.objects.get(name=class_name)
    except Class.DoesNotExist:
        print("Клас не знайдено! Спочатку додайте клас.")
        return
    
    Student.objects.create(name=name, class_group=class_group)
    print(f"Учень '{name}' успішно додано.")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Вийти")

        choice =input("Виберіть опцію: ")

        if choice == '1':
            add_subject()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            add_class()
        elif choice == '4':
            add_student()
        elif choice == '5':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()