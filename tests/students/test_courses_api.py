import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture  # Фикстуры - специальные функции, которые возвращают некоторое значение. И мы их можем использовать в
# качестве аргументов в нашу тестирующую функцию.
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)


# Тест на получение первого курса
@pytest.mark.django_db
def test_course(client, course_factory):
    # Arrange - подготовка данных
    course = course_factory(_quantity=1)

    # Act - непосредственно тестирование
    response = client.get('/courses/')

    # Assert - проверка, что действие прошло корректно
    assert response.status_code == 200
    data = response.json()
    assert data[0].id == course[0].id

    #
    # index = course[0].id
    #
    # from django.urls import reverse
    # url = reverse(f'{courses}-detail', args=[index])
    # response = client.get(url)
    #
    # # response = client.get(f'/api/v1/courses/{index}/')
    # data = response.json()
    #
    # assert response.status_code == 200
    # assert data['id'] == index