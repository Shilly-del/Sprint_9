from pathlib import Path

class Url:
    BASE = 'https://foodgram-frontend-1.prakticum-team.ru'
    SIGN_IN = f'{BASE}/signin'
    SIGN_UP = f'{BASE}/signup'
    RECIPES = f'{BASE}/recipes'

class Path:
    ASSET = Path(__file__).parent / "assets" / "image.jpeg"

