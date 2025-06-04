from fastapi import FastAPI, Request        # стандартные либы фастапи, Request для получения инфы с ссылок
import uvicorn                              # для запуска через сам код в блоке if __name__ == "__main__"
from pathlib import Path                    # тип пути файла
import sys                                  # для просмотра внешних файлов, т. к. там либы
from urllib.parse import unquote            # для декодирования сырых ссылок

from libs.convert import compress, decompress, convertString         
from libs.interpreter import run
from libs.precompile import parseCode, findBrackets
from libs.config import Config

Config.commasInput = False

functionList = {                    
    "run":              run,              
    "decompress":       decompress,       
    "compress":         compress,     
    "convertstring":    convertString,
    "parsecode":        parseCode,
    "findbrackets":     findBrackets
}

app = FastAPI()

def createHandler(function):    # фабрика функций т. к. каждый эндпоинт нужна новая
    
    def handler(request: Request):          # request для получения ссылки, куда был совершен переход
        try:
            data = str(request.url)             # конвертация ссылки в строку 
            data = data.split("?data=")[1:]     # делит ссылку на элементы списка, срез [1:] если в введеной инфе окажется такая же строка
            data = "".join(data)                # совмещает все элементы списка в строку
            data = unquote(data)                # дешифрует значения %20 и т. п. в нормальные символы
            return function(data)
        
        except Exception as error:              # при слишком больших значениях
            return f"error: {error}"
            
    
    return handler

for funcName, funcCode in functionList.items():             
    app.get(f"/{funcName}")(createHandler(funcCode))

if __name__ == "__main__":
    uvicorn.run("api:app")