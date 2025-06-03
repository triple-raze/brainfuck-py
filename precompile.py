def parseCode(code):
    
    parsedCode = ""     # вывод
    
    for char in code:
        if char in ["+", "-", ">", "<", "[", "]", ",", "."]:
            parsedCode += char

    return parsedCode


def findBrackets(code):
    
    stack = []          # нахождение ближайших пар
    bracketPairs = {}   # пары для использования в интерпретаторе

    for index, char in enumerate(code):
        if char == "[":
            stack.append(index)
        
        if char == "]":
            lastBracket = stack.pop()           # я хз как называть такие переменные
            bracketPairs[lastBracket] = index
            bracketPairs[index] = lastBracket
    
    return bracketPairs
