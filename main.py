import psutil
import time
import os
import turtle
import math
import datetime
import random
import webbrowser

appinstall1 = False
appinstall2 = False
appinstall3 = False
appinstall4 = False
wait = time.sleep
username = ""
password = ""


def urlopen(url):
    webbrowser.open_new(url)
    print(f"Attempting to Open {url}")


def browser():
    cls()
    while True:
        print("Welcome to the browser!")
        mode = input("Search an URL or a query? ")
        if mode == "query":
            request = input("Search Something: ")
            urlopen("https://www.google.com/search?q=" + request)

            request = input("Search More? y/n: ")
            if request == "y":
                browser()

            else:
                homescreen()
                break

        else:
            request = input("Enter an URL: ")
            urlopen(request)

            request = input("Search More? y/n: ")
            if request == "y":
                browser()

            else:
                homescreen()
                break


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def _datetime():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d"))


def turtleapp():
    cls()
    counter = 1

    size = input("Size: ")
    turtle.up()
    turtle.clearscreen()

    while True:
        X = math.cos(counter) * float(size)
        Y = math.sin(counter) * float(size)
        counter += 1

        turtle.goto(X, Y)
        turtle.hideturtle()

        if counter > 100:
            homescreen()
            break


def appstore():
    global appinstall1
    global appinstall2
    global appinstall3
    global appinstall4
    cls()
    install = ""
    print("Welcome to the app store, " + username +
          "!\nType 'Exit' to exit the app store.\n")

    if not appinstall2:
        print("Dice Roller ❌")

    else:
        print("Dice Roller ✅")

    if not appinstall1:
        print("Turtle ❌")

    else:
        print("Turtle ✅")

    if not appinstall3:
        print("UNKNOWN ❌")

    else:
        print("UNKNOWN ✅")

    if not appinstall4:
        print("Browser ❌")

    else:
        print("Browser ✅")

    while True:
        install = input("Install: ")
        if install == "Turtle" and not appinstall1:
            appinstall1 = True
            print("Installing...")
            wait(1)
            print("Installed!")
            appstore()
        elif install == "Turtle" and appinstall1:
            print("Already Installed")

        if install == "Dice Roller" and not appinstall2:
            appinstall2 = True
            print("Installing...")
            wait(1)
            print("Installed!")
            appstore()
        elif install == "Dice Roller" and appinstall2:
            print("Already Installed")

        if install == "UNKNOWN" and not appinstall3:
            appinstall3 = True
            print("Installing...")
            wait(1)
            print("Installed!")
            appstore()

        elif install == "UNKNOWN" and appinstall3:
            print("Already Installed")

        if install == "Browser" and not appinstall4:
            appinstall4 = True
            print("Installing...")
            wait(1)
            print("Installed!")
            appstore()
        else:
            print("Already Installed")

        if install == "Exit":
            cls()
            homescreen()
            break


def setup():
    global appinstall1
    global username
    global password

    password = input("Create a password: ")
    username = input("Create a username: ")
    print("Setup complete! System will now start installing...")
    time.sleep(5)
    print("Successfully installed PyOS and data")
    lockscreen()


def lockscreen():
    cls()

    print("Welcome " + username + "!")
    while True:
        ipassword = input("Please enter your password: ")

        if ipassword == password:
            print("Logging in...")
            time.sleep(2)
            homescreen()
            break

        else:
            cls()
            print("Wrong password")


def diceapp():
    cls()
    command = input("Roll? (y/n): ")

    if command == "y":
        _random = random.randint(1, 12)
        print("You rolled a " + str(_random) + "!")
        answer = input("Roll again? (y/n): ")

        if answer == "y":
            diceapp()

        else:
            homescreen()

    else:
        homescreen()


def homescreen():
    cls()

    print("Welcome " + username + "!")
    _datetime()
    print("")
    if appinstall1:
        print("Turtle")

    if appinstall2:
        print("Dice Roller")

    if appinstall3:
        print("UNKNOWN")

    if appinstall4:
        print("Browser")

    print("Calculator")
    print("App Store")
    print("Options")
    while True:
        inputed = input("Select: ")
        if inputed == "Calculator":
            calculator()
            break

        if inputed == "Turtle" and appinstall1:
            turtleapp()
            break

        if inputed == "App Store":
            appstore()
            break

        if inputed == "Options":
            commands()
            break

        if inputed == "Dice Roller" and appinstall2:
            diceapp()
            break

        if inputed == "UNKNOWN" and appinstall3:
            urlopen('https://justpaste.it/1v4bk')
            print("G̷L̵I̵T̵C̸H̸ ̶U̶N̸K̸N̵O̷W̵N̵")
            break

        if inputed == "Browser" and appinstall4:
            browser()


def calculator():
    print("Operators: +, -, *, /")
    num1 = input("Number: ")
    num2 = input("Number: ")
    operator = input("Operator: ")

    if operator == "+":
        print(int(num1) + int(num2))

    if operator == "-":
        print(int(num1) - int(num2))

    if operator == "*":
        print(int(num1) * int(num2))

    if operator == "/":
        print(int(num1) / int(num2))

    time.sleep(1)

    homescreen()


def commands():
    print("Commands: shutdown, restart, gsi, lockscreen, factory reset (FR)")

    while True:
        command = input("Command: ")
        if command == "shutdown":
            print("Shutting Down...")
            time.sleep(1)
            print("Shut Down")
            exit()

        if command == "restart":
            cls()
            print("Restarting...")
            time.sleep(1)

            if not psutil.virtual_memory().percent > 60:
                print("RAM: OK (" + str(psutil.virtual_memory().percent) + "%)")

            else:
                print("RAM: WARNING")

            if not psutil.cpu_percent(interval=1) > 70:
                print("CPU: OK (" + str(psutil.cpu_percent(interval=1)) + "%)")

            else:
                print("CPU: WARNING")

            time.sleep(1)

            lockscreen()

        if command == "gsi":
            cls()
            time.sleep(0.5)
            print("CPU Usage: " + str(psutil.cpu_percent(interval=1)))
            time.sleep(0.5)
            print("RAM Usage: " + str(psutil.virtual_memory().percent))
            time.sleep(0.5)
            print("Disk Usage: " + str(psutil.disk_usage("/").percent))
            time.sleep(0.5)
            print("Network Usage: " + str(psutil.net_io_counters().bytes_sent))
            time.sleep(3)
            homescreen()

        if command == "FR":
            FR()

        if command == "lockscreen":
            lockscreen()


def FR():
    cls()
    reset = ""
    print("NO / YES")

    while True:
        reset = input("Reset: ")

        if reset == "NO":
            print("Reset cancelled")
            time.sleep(1)
            homescreen()

        if reset == "YES":
            cls()
            print("Resetting...")
            time.sleep(3)
            print("Reset complete")
            time.sleep(1)
            setup()


print("Welcome to PyOS! \nPlease standby while we get things ready!")
time.sleep(3)
cls()
print("Hello")
time.sleep(1)
cls()
print("Hola")
time.sleep(1)
cls()
print("Halò")
time.sleep(1)
cls()
print("Bonjour")
time.sleep(1)
cls()
setup()
