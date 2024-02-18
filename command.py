# Стартовый угол слева
CONST_ANGLE_START = 30
# Конечный угол справа
CONST_ANGLE_END = 150
# Глубина дыры
CONST_START_HEIGHT = -3
# Высота, которой мы должны достичь 
CONST_END_HEIGHT = 0
# Шаг поворота камеры 
defaul_step = 30

# Словарь с описаниями функций

commands = {
    "l": "Переместить объект влево на указанное количество градусов.",
    "r": "Переместить объект вправо на указанное количество градусов.",
    "u": "Переместить объект вверх на указанное количество градусов.",
    "b": "Переместить объект вниз на указанное количество градусов.",
    "help": "Показать список доступных команд и их описания.",
    "photo": "Сделать фото"
}

def Up_step(level):
    return f"u,{level}"

def Bottom_step(level):
    return f"b,{level}"

def Left_step(angle):
    return f"l,{angle}"

def Right_step(angle):
    return f"r,{angle}"

def Photo():
    return "photo"

def CheckResponse(respones):
    if(respones == "OK"):
        return "OK"
    else:
        return "error"
