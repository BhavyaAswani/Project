while(True):
    s = input("Welcome to the calculator !! \n").strip()
    if s == "exit" or s == "stop" or s == "quit":
        break
    try:
        l = s.split("+")
        print(int(l[0]) + int(l[1]))
    except:
        try:
            l = s.split("-")
            print(int(l[0]) - int(l[1]))
        except:
            try:
                l = s.split("*")
                print(int(l[0]) * int(l[1]))
            except:
                try:
                    l = s.split("//")
                    print(int(l[0]) // int(l[1]))
                except:
                    try:
                        l = s.split("/")
                        print(int(l[0]) / int(l[1]))
                    except:
                        try:
                            l = s.split("%")
                            print(int(l[0]) % int(l[1]))
                        except:
                            try:
                                l = s.split()
                                op = l[0].lower()
                                a = int(l[1])
                                b = int(l[3])
                                if op == "add":
                                    print(a,"+",b,"=",a+b)
                                elif op == "multiply":
                                    print(a,"*",b,"=",a*b)
                                elif op == "subtract":
                                    print(b,"-",a,"=",b-a)
                                elif op == "divide":
                                    print(a,"/",b,"=",a/b)
                                elif op == "remainder" or op == "modulo":
                                    print(a,"%",b,"=",a%b)
                                elif op == "floordivide" or op == "quotient":
                                    print(a,"//",b,"=",a//b)
                            except:
                                print("Wrong Format,\nEither \nWrite like \na + b, a - b, a*b, a//b, a / b,\nor \nWrite like \nAdd a and b or \nDivide a by b or \nMultiply a and b or \nSubtract a from b or \nRemainder a by b or \nQuotient a by b\nType exit/quit/stop to stop the calculator")

