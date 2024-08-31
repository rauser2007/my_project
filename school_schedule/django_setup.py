import os 
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_schedule.settings")
django.setup()

from core.models import Subject, Teacher, Class, Student, Schedule, Grade

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

def add_schedule():
    day_of_week = input("Введіть день тижня (наприклад, Monday): ")
    start_time = input("Введіть час початку (у форматі HH:MM): ")
    end_time = input("Введіть час закінчення (у форматі HH:MM): ")
    subject_name = input("Введіть назву предмету: ")
    class_name = input("Введіть назву класу: ")
    teacher_name = input("Введіть ім'я вчителя: ")

    try:
        subject = Subject.objects.get(name=subject_name)
    except Subject.DoesNotExist:
        print("Предмет не знайдено! Спочатку додайте предмет.")
        return

    try:
        class_group = Class.objects.get(name=class_name)
    except Class.DoesNotExist:
        print("Клас не знайдено! Спочатку додайте клас.")
        return

    try:
        teacher = Teacher.objects.get(name=teacher_name, subject=subject)
    except Teacher.DoesNotExist:
        print("Вчителя не знайдено або він не викладає цей предмет!")
        return

    Schedule.objects.create(
        subject=subject,
        class_group=class_group,
        teacher=teacher,
        day_of_week=day_of_week,  # Додаємо день тижня
        date=datetime.now().date(),  # Можна ввести свою дату або використовувати поточну
        start_time=start_time,
        end_time=end_time
    )
    print(f"Заняття для '{class_group}' з предмету '{subject}' додано до розкладу на {day_of_week}.")


def add_grade():
    student_name = input("Введіть ім'я учня: ")
    subject_name = input("Введіть назву предмету: ")
    grade_value = input("Введіть оцінку: ")
    date = input("Введіть дату оцінки (у форматі YYYY-MM-DD): ")

    try:
        student = Student.objects.get(name=student_name)
    except Student.DoesNotExist:
        print("Учня не знайдено! Спочатку додайте учня.")
        return
    
    try:
        subject = Subject.objects.get(name=subject_name)
    except Subject.DoesNotExist:
        print("Предмет не знайдено! Спочатку додайте предмет.")
        return
    
    Grade.objects.create(
        student=student,
        subject=subject,
        grade=grade_value,
        date=date
    )

    print(f"Оцінку '{grade_value}' для учня '{student}' з предмету '{subject}' успішно додано.")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вийти")

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
            add_schedule()
        elif choice == '6':
            add_grade()
        elif choice == '7':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()