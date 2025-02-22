import json
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')
django.setup()

from programs.models import Place, University

def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        # Получаем или создаём объект города
        place, _ = Place.objects.get_or_create(name=item['city'])

        # Если курс с таким course_id уже существует – удаляем его
        University.objects.filter(course_id=item['course_id']).delete()

        # Функция для проверки длины строк
        def validate_field(value, max_length):
            if value and len(value) > max_length:
                print(f"Строка слишком длинная: {value}. Заменяем на пустую строку.")
                return ""
            return value

        # Создаём объект University с учетом всех полей из JSON
        university = University(
            place=place,
            name=validate_field(item['academy'], 500),
            course_id=item['course_id'],
            course_name=validate_field(item['course_name'], 500),
            tuition_fees=validate_field(item['tuition_fees'], 500),
            beginning=validate_field(item['beginning'], 500),
            subject=validate_field(item['subject'], 500),
            duration=validate_field(item['duration'], 500),
            languages=item.get('languages', []),
            ielts_score=item.get('ielts_score'),
            toefl_score=item.get('toefl_score'),
            gmat_required=item.get('gmat_required', False),
            gre_required=item.get('gre_required', False),
            gpa_requirement=item.get('gpa_requirement'),
            deadlines=item.get('deadlines', []),
            application_link=validate_field(item.get('application_link'), 10000),
            link_detail=validate_field(item.get('link_detail'), 10000),
            english_language_level=validate_field(item.get('english_language_level'), 500),
            german_language_level=validate_field(item.get('german_language_level'), 500)
        )
        university.save()
        print(f"Сохранён курс: {university}")

if __name__ == "__main__":
    load_data_from_json('courses.json')  # Укажите корректный путь к вашему JSON-файлу
    print("Данные успешно загружены в базу данных!")
