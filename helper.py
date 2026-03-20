import allure
import string
import random

def generate_random_string(length):

    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters)
                            for i in range(length))
    return random_string

def random_letter():
        
    excluded_codes = {1081, 1098, 1099, 1100, 1105}
    
    while True:
        code = random.randint(1072, 1103)
        if code not in excluded_codes:
            return chr(code)

class User:

    @allure.step('Создание пользователя')
    def __init__(self):
        self.name = generate_random_string(7)
        self.surname = generate_random_string(7)
        self.username = generate_random_string(7)
        self.email = f'{generate_random_string(7)}@gmail.com'
        self.password = generate_random_string(10)

class Recipe:

    @allure.step('Создание рецепта')
    def __init__(self):
        self.title = generate_random_string(7)
        self.ingredient = 'а'
        self.amount = random.randint(1, 1000)
        self.time = random.randint(1, 60)
        self.description = generate_random_string(10)

