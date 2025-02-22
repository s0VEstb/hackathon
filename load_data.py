import json
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')  # Замените `your_project_name` на имя вашего проекта
django.setup()

from programs.models import Place, University  # Замените `your_app` на имя вашего приложения
def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        place, created = Place.objects.get_or_create(name=item['city'])
        # Удаляем существующую запись с таким course_id (если есть)
        University.objects.filter(course_id=item['course_id']).delete()
        print(item)

        # Функция для проверки длины строки
        def validate_field(value, max_length):
            if value and len(value) > max_length:
                print(f"Строка слишком длинная: {value}. Заменяем на пустую строку.")
                return ""  # или return None, если хотите сохранить NULL в базе данных
            return value
        
         # Удаляем существующую запись с таким course_id (если есть)
        University.objects.filter(course_id=item['course_id']).delete()

       


        # Создаем объект University с проверкой длины строк
        university = University(
            place=place,
            name=validate_field(item['academy'], 500),  # Максимальная длина для name: 500
            course_id=item['course_id'],
            course_name=validate_field(item['course_name'], 500),  # Максимальная длина для course_name: 500
            tuition_fees=validate_field(item['tuition_fees'], 500),  # Максимальная длина для tuition_fees: 500
            beginning=validate_field(item['beginning'], 500),  # Максимальная длина для beginning: 500
            subject=validate_field(item['subject'], 500),  # Максимальная длина для subject: 500
            duration=validate_field(item['duration'], 500),  # Максимальная длина для duration: 500
            languages=item['languages'],  # JSONField, не требует проверки длины
            ielts_score=item['ielts_score'],
            toefl_score=item['toefl_score'],
            gmat_required=item['gmat_required'],
            gre_required=item['gre_required'],
            gpa_requirement=item['gpa_requirement'],
            deadlines=item['deadlines'],  # JSONField, не требует проверки длины
            # application_link=validate_field(item['application_link'], 500),  # Максимальная длина для application_link: 500
            # link_detail=validate_field(item['link_detail'], 500)  # Максимальная длина для link_detail: 500
        )
        university.save()
# Пример вызова функции для загрузки данных
if __name__ == "__main__":
    load_data_from_json('courses.json')  # Укажите путь к вашему JSON-файлу
    print("Данные успешно загружены в базу данных!")