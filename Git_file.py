slovo = int(input())
simbol = input()
slovo2 = int(input())
if simbol == '+':
    print(slovo + slovo2)
elif simbol == '*':
    print(slovo * slovo2)
elif simbol == '/' and slovo != 0 and slovo2 != 0:
    print(slovo / slovo2)
elif simbol == '%' and slovo != 0 and slovo2 != 0:
    print(slovo % slovo2)
elif simbol == '-':
    print(slovo - slovo2)
elif simbol == '//' and slovo != 0 and slovo2 != 0:
    print(slovo // slovo2)