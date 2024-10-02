# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:30:26 2024

@author: Rosshun
"""
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.lstrip('-').isdigit():  
            stack.append(int(token))
            
        elif token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    
    return stack[0]


exp = input("Input: ")
print("Ouput:", evaluate_postfix(exp))        
