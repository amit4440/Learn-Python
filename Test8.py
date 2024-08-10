import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok, we will create it for you")
else:
    print("Your input is not t2.micro")
