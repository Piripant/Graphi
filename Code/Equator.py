__author__ = 'Davide'
import math

functions = ["sin", "cos", "in", "log", "sqrt", "!", "-"]
multopers = ["*", "/"]

def eqint(formula=[]):
    i = 0
    while i < len(formula):
        if formula[i] is "+" or formula[i] is "" or formula[i] is None or formula[i] is " ":
            formula.pop(i)

        elif formula[i].isdigit():
            if i-1 >= 0:
                if formula[i-1] == '-':
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
    multchain = [False]
    functchain = [False]
    for i in range(0, len(formula)):
        if i+1 < len(formula):
            nextchar = formula[i+1]
        else:
            nextchar = ""
        
        # Appends if (*/
        if formula[i] is "(":
            multchain.append(False)
            functchain.append(False)
            stack.append([])
        
        elif nextchar in multopers and multchain[len(multchain)-1] is False:
            multchain[len(multchain)-1] = True
            stack.append([])

        elif formula[i] in functions:
            functchain[len(functchain)-1] = True
            if nextchar in functions:
                functchain.append(False)
            stack.append([])

        # Appends char
        if formula[i] != "(" and formula[i] != ")":
            stack[len(stack)-1].append(formula[i])
            if formula[i] in functions:
                continue

        rewhile = True
        rechecked = False
        while rewhile is True:
            rewhile = False

            # Resolves multiplication chain
            if formula[i] not in multopers and nextchar not in multopers and formula[i] is not "(" and nextchar is not "(" and multchain[len(multchain)-1] is True:
                multchain[len(multchain)-1] = False
                oper = list(stack[len(stack)-1])
                stack.pop()
                stack[len(stack)-1].append(resolve(oper))

            # Resolves functions
            if functchain[len(functchain)-1] is True and nextchar not in functions and nextchar is not "(":
                if len(functchain) > 1:
                    functchain.pop()
                else:
                    functchain[len(functchain)-1] = False

                oper = list(stack[len(stack)-1])
                stack.pop()
                stack[len(stack)-1].append(resolve(oper))
                rewhile = True
                continue

            if rechecked is True:
                break

            # Resolves if )
            if formula[i] is ")":
                oper = list(stack[len(stack)-1])
                stack.pop()
                multchain.pop()
                functchain.pop()
                stack[len(stack)-1].append(resolve(oper))
                rewhile = True

            rechecked = True

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

            elif formula[i] not in functions and type(formula[i+1]) is float:
                result = operation(formula[i], formula[i+1], result)

            i += 2

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
