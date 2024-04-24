# Стартовый угол слева
CONST_ANGLE_START = 0
# Конечный угол справа
CONST_ANGLE_END = 500
# Глубина дыры
CONST_START_HEIGHT = 0
# Высота, которой мы должны достичь 
CONST_END_HEIGHT = 22000
# Шаг поворота камеры 
DEFAULT_STEP = 50
#Текущая высота 
# TH = -3

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


def EndProgram():
    return "END"