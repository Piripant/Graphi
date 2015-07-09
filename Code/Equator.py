__author__ = 'Davide'
import math

functions = ["sin", "cos", "in", "log", "sqrt", "!", "-"]


def eqint(formula=[]):
    i = 0
    while i < len(formula):
        if formula[i] is "+" or formula[i] is "" or formula[i] is None or formula[i] is " ":
            formula.pop(i)

        elif formula[i].isdigit():
            if i-1 > 0:
                if formula[i-1] == "-":
                    formula[i] = -float(formula[i])
                    formula.pop(i-1)

                else:
                    formula[i] = float(formula[i])
                    i += 1

            else:
                formula[i] = float(formula[i])
                i += 1

        else:
            i += 1


def operation(operator="", number=0, result=0):
    if operator == '*':
        return result * number

    elif operator == '/':
        return result / number

    elif operator == '^':
        return result ** number

    else:
        return result + number


def deparenter(formula=[]):
    stack = [[]]
    for i in range(0, len(formula)):
        if formula[i] != "(" and formula[i] != ")":
            stack[len(stack)-1].append(formula[i])

        elif formula[i] is "(":
            stack.append([])

        elif formula[i] is ")":
            oper = list(stack[len(stack)-1])
            stack.pop()
            stack[len(stack)-1].append(resolve(oper))

    return stack[0]


def resolve(formula=[]):
    result = 0.0
    i = 0
    while i < len(formula):
        if type(formula[i]) is float:
                result = operation("", formula[i], result)
                i += 1

        if i+1 < len(formula):
            if formula[i] in functions and type(formula[i+1]) is float:
                result = operation(formula[i], functioner(formula[i], formula[i+1]), result)
                i += 3

            elif formula[i] not in functions and type(formula[i+1]) is float:
                result = operation(formula[i], formula[i+1], result)
                i += 2

        if i+2 < len(formula):            
            if formula[i] not in functions and formula[i+1] in functions and type(formula[i+2]) is float:
                result = operation(formula[i], functioner(formula[i], functioner(formula[i+1], formula[i+2])), result)
                i += 3
				
        if i+3 < len(formula):
            if formula[i] not in functions and formula[i+1] in functions and formula[i+2] in functions and type(formula[i+3]) is float:
                result = operation(formula[i], functioner(formula[i+1], functioner(formula[i+2], formula[i+3])), result)
                i += 4

    return result


def functioner(function="", parameter=0.0):
    if function == "sin":
        return math.sin(parameter)

    elif function == "cos":
        return math.cos(parameter)

    elif function == "in":
        return 1/parameter

    elif function == "!":
        return math.factorial(parameter)

    elif function == "sqrt":
        return math.sqrt(parameter)
        
    elif function == "-":
        return -parameter
        
    else:
        return parameter
