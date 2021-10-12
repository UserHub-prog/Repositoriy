slovar = {"Egor": "1234", "Misha": "123", "Alexander": "12345", "Masha": "565456",
          "Lev": "948579", "Alice": "54254635", "Vito": "4562258", "Katya": "54842355"}
info = {"Egor": "loves basketball", "Misha": "loves tennis", "Alexander": "loves football", "Masha": "loves chess",
        "Lev": "loves volleyball", "Alice": "loves banana", "Vito": "loves apple", "Katya": "loves pears"}

a = True

while a:
    Login = str(input("Login: "))
    for i in range(len(slovar)):
        if Login != list(slovar.keys())[i]:
            continue
        Password = slovar[Login]
        InputPassword = input("Password: ")
        if InputPassword == Password:
            print(list(slovar.keys())[i], info[Login])
            if Login == list(slovar.keys())[i]:
                Rename_password = input("You want to rename password?(Y/N): ")
                if Rename_password == "Y":
                    Retry_password = input("Retry password: ")
                    if InputPassword == Retry_password:
                        New_password = input("New password: ")
                        Password = New_password
                        del slovar[Login]
                        slovar[Login] = New_password
                        print("Password changes!")
                        print("New Password:", Password)
                        b = True
                        Exit = str(input("You want to exit?(Y/N): "))
                        if Exit == "Y":
                            a = False
                            break
                        elif Exit == "N":
                            pass
                        else:
                            print("I don't understand!")
                            continue
                    else:
                        print("Not right!")
                        break
                elif Rename_password == "N":
                    continue
                else:
                    print("I don't understand!")
            elif Login != list(slovar.keys())[i]:
                pass