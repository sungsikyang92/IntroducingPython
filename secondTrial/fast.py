from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]

def pick(): # 아래에 docstring이 있다.
    """임의의 패스트푸드점을 반환한다."""
    return choice(places)




