from libs.convert import compress, decompress, convertString
from libs.interpreter import run, runFile, setByteMode, changeLightMode
from libs.config import Config

def cmd_lightMode():
    Config.lightMode = changeLightMode(Config.lightMode)

def cmd_byteMode(byteModeValue):
    Config.byteMode = int(byteModeValue)
    print(setByteMode(Config.byteMode)[1])    # [1] это второй аргумент в return, который возвращает описнаие (первый возвращает функцию)
    
def cmd_open(path):
    print(runFile(path))

def cmd_run(code):
    print(run(code))

def cmd_decompress(code): 
    print(decompress(code))

def cmd_compress(code):
    print(compress(code))

def cmd_convertString(string):
    print(convertString(string))

def cmd_help():
    print(commands.keys())

def cmd_exit():
    exit()

commands = {
    "open":       cmd_open,          # открытие файла
    "run":        cmd_run,           # запуск введенного кода 
    "decompress": cmd_decompress,    # конвертация из краткой формы в длинную
    "compress":   cmd_compress,      # конвертация из длинной форму в краткую
    "convert":    cmd_convertString, # конвертация строки в код brainfuck
    "lightmode":  cmd_lightMode,     # включение/выключение краткой формы
    "bytemode":   cmd_byteMode,      # смена режима ограничений
    "help":       cmd_help,          # (не доделано) вывод помощи по командам
    "exit":       cmd_exit           # выход из консоли
}


print("Brainfuck interpreter v0.1\nMade by triple-raze yo\n")

while True:
    userInput = input(">>> ").split()

    if userInput == []:     # [] т. к. из-за метода .split() ввод пользователя превращается в список, пустой ввод будет пустым списком
        print()             # вывод новой строки для читабельности
        continue

    userCommand = userInput[0]
    userArgs = []
    
    if len(userInput) > 1:
        userArgs = " ".join(userInput[1:])

    if userCommand in commands: 
        try:
            if userArgs == []:
                commands[userCommand]()
            else:
                commands[userCommand](userArgs)
        except Exception as error:
            print(f"An error occured: {error}")
        
    else:
        print("Unknown command, write help for more")

    print()