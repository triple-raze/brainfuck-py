from precompile import findBrackets, parseCode
from convert import decompress
from config import Config

def checkZero(index, value):
    if value < 0:
        raise Exception(f"value cant be lower than 0, error at char with index {index}")
    return value


def setByteMode(byteModeValue=1):
    
    descriptionList = {
        0: "Strong - cell value more than 255 will throw error",
        1: "Soft - cell value more than 255 will turn into 0 and vice versa",
        2: "Unlimited - cell value has no limits" 
    }
    
    byteModeValue = int(byteModeValue)
    
    if byteModeValue == 0:
        def checkByte(index, value):    # проверка на слишком большое или маленькое значение байта (255 и 0 соответсвенно)
            if value > 255:
                raise Exception(f"value cant be higher than 255, error at char with index {index}")
            if value < 0:
                raise Exception(f"value cant be lower than 0, error at char with index {index}")
            return value

    elif byteModeValue == 1:
        def checkByte(index, value):
            return value % 256
        
    elif byteModeValue == 2:
        def checkByte(index, value):
            if value < 0:
                raise Exception(f"value cant be lower than 0, error at char with index {index}")
            return value
    
    else:
        print("Wrong bytemode value, using bytemode 1")
        def checkByte(index, value):
            return value % 256

    return [checkByte, descriptionList[Config.byteMode]]

                                    
def changeLightMode(lightModeValue):        # not true == false
    lightModeValue = not lightModeValue     # как !(condition) в js

    if lightModeValue:
        print("On - interpreter reads pairs of {num}{symbol} like {symbol * num}")
    else:           
        print("Off - light mode doesnt work and interpreter ignores numbers")
    return lightModeValue                                  


def run(code: str):

    code = decompress(code) if Config.lightMode else code  # конвертация из сокращенной формы (2а3б --> ааббб) если включен легковесный режим
    code = parseCode(code)                                 # очистка от всех ненужных символов
    brackets = findBrackets(code)                          # пары скобок для циклов
    checkByte = setByteMode(Config.byteMode)[0]            # переопределение функции в зависимости от мода (1 - строгий, 2 - байты кратные 255, 3 - пределов нет)

    cellArray = [0]    # массив клеток, но без фиксированных размеров (добавляется динамично)
    pointer = 0        # указатель (по индексу)
    output = ""        # вывод
    index = 0          # номер символа в коде (for саси жопу)

    while index < len(code): 
        char = code[index]
        
        match char:
            case ">":
                pointer += 1
                if pointer >= len(cellArray):
                    cellArray.append(0)

            case "<":
                pointer -= 1
                checkZero(index, pointer)

            case "+":
                cellArray[pointer] += 1
                cellArray[pointer] = checkByte(index, cellArray[pointer])
            
            case "-":
                cellArray[pointer] -= 1
                cellArray[pointer] = checkByte(index, cellArray[pointer])

            case ".":                                 # большие латинские буквы с кодом от 65 до 91
                output += chr(cellArray[pointer])     # маленькие латинские буквы с кодом от 97 до 123

            case ",":
                print(output)
                cellArray[pointer] = ord(input("> "))    # обращение по индексу т. к. cell это ссылка, а не само значение
            
            case "[":
                if cellArray[pointer] == 0:
                    index = brackets[index]

            case "]":
                if cellArray[pointer] != 0:
                    index = brackets[index]
            
        index += 1
       
    return output


def runFile(path: str):
    with open(path, "r") as file:
        code = file.read()
        return run(code)
    