browser_name = input("Enter the name of browser \n")
browser_name = browser_name.lower()
match browser_name:
    case "chrome":
        print("execute the code for chrome browser")
    case 'firefox':
        print("execute the code for firefox browser")
    case 'edge':
        print("execute the code for edge browser")
    case _:
        print("no browser defined")
