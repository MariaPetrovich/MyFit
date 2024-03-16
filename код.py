Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Импортирование необходимых модулей
import datetime

# Класс пользовательского профиля
class UserProfile:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        # Расчет индекса массы тела
        bmi = self.weight / (self.height ** 2)
        return bmi

# Класс упражнения
class Exercise:
    def __init__(self, name, intensity):
        self.name = name
        self.intensity = intensity

# Класс тренировки
class Workout:
    def __init__(self, exercises, duration):
        self.exercises = exercises
        self.duration = duration

    def calculate_calories_burned(self, user):
        # Расчет потраченных калорий
        calories_burned = 0
        for exercise in self.exercises:
            calories_burned += exercise.intensity * user.weight * self.duration
        return calories_burned

# Создание пользовательского профиля
user_profile = UserProfile("John Doe", 25, 70, 1.75)

# Создание упражнений
exercises = [
    Exercise("Push-ups", 5),
    Exercise("Squats", 4),
    Exercise("Plank", 3)
]

# Создание тренировки
workout = Workout(exercises, 30)

# Расчет индекса массы тела пользователя
bmi = user_profile.calculate_bmi()

# Расчет потраченных калорий пользователя во время тренировки
calories_burned = workout.calculate_calories_burned(user_profile)

# Вывод результатов
print("User:", user_profile.name)
print("BMI:", bmi)
print("Calories Burned:", calories_burned)