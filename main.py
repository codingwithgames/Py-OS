import time
SecWait = time.sleep(1)
SecWait
print("Booting From Hard Disk......")
time.sleep(5.5)
print("Booted From Hard Disk.....Starting OS")
time.sleep(4)
print("Running OS")
time.sleep(10)
SecWait
print('''               🆆 🅴 🅻 🅲 🅾 🅼 🅴
                          ''')
SecWait
print('''                           𝕋𝕆               ''')
SecWait
print('''                                      ▒█▀▀█ ▒█░░▒█ 　 ▒█▀▀▀█ ▒█▀▀▀█ 
                                      ▒█▄▄█ ▒█▄▄▄█ 　 ▒█░░▒█ ░▀▀▀▄▄ 
                                      ▒█░░░ ░░▒█░░ 　 ▒█▄▄▄█ ▒█▄▄▄█      ''')
SecWait
print("                                                                   v1.0.0")
SecWait
DisplayOSUsername = input(str("Enter your username:"))
SecWait
CMD_Prompt = input(str(DisplayOSUsername + "@cmd==:"))
if CMD_Prompt == "/?":
    print('''             -------------------HELP-----------------
          CMD                        USE
          /?                         Shows Help(CMD[s] and Uses of CMD[s])
          calc.app()                 A Calculator App
          shutdown()                     Shuts Down the OS
          even_odd_num.app()         A Application Which Checks If A Number Is Odd Or Even''')
if CMD_Prompt == "shutdown()":
    exit()
if CMD_Prompt == "calc.app()":
    print("        WELCOME")
    SecWait
    print("                  TO")
    SecWait
    print("                     CALCULATOR")
    FirstNum = float(input("Enter The First Number:"))
    SignOpen = input(str("Enter Operation:"))
    SeconNum = float(input("Enter The Second Number:"))
    if SignOpen == "+":
        print("The Sum is" , FirstNum+SeconNum)
    if SignOpen == "-":
        print("The Difference is" , FirstNum-SeconNum)
    if SignOpen == "*":
        print("The Product is" , FirstNum*SeconNum)
    if SignOpen == "x":
        print("The Product is" , FirstNum*SeconNum)
    if SignOpen == "/":
        print("The Quotient is" , FirstNum/SeconNum)
    if SignOpen == "%":
        print("The Reminder is" , FirstNum%SeconNum)
if CMD_Prompt == "even_odd_num.app()":
    InputNum = int(input("Enter A Number:"))
    if InputNum % 2 == 0:
        print("The Number You Have Entered Is A Even Number.")
    else:
        print("The Number You Have Entered Is A Odd Number.")








