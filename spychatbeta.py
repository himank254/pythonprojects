def welcome():
    print("WELCOME TO SPYCHAT. LEADING CHAT SERVICE FOR A SPY ")
    print("----------------------------------------------------")
    print("Guidelines: ")
    print("1. USERNAME SHOULD BE UNIQUE AND LENGTH GREATER THEN 3 \n2. PASSWORD SHOULD BE OF ATLEAST 8 CHARACTERS. \n3. 18 YEARS AND ABOVE ARE ELGIBLE.")
    print("")
def mainmenu():
    f = input("Login(L) or Sign Up(S) user: ")
    if (f == "l" or f == "L"):
        old()
    elif (f == "s" or f == "S"):
        welcome()
        new()
    else:
        print("Please Select a valid choice.")
        print("")
        print("")
        mainmenu()
def new():
  f = open('userlist', 'r')
  list = f.readlines()
  a = input("Enter Spy Name: ")
  if(list.__contains__(a+"\n")):
      print("Username already exist.")
      new()
  else:
    if (len(a) > 3):
        if (a.isalpha() == True):
            password = input("Enter new password: ")
            if password.isnumeric() == False and password.isalpha() == False:
                if len(password) >= 8:
                    b = input("Select Gender (M or F): ")
                    if (b == "m" or b == "M"):
                        gend = "MR. "
                    elif (b == "f" or b == "F"):
                        gend = "MS. "
                    else:
                        print("Please Select A valid Gender")
                        new()
                    c = input("Enter Spy Age: ")
                    if (c.isnumeric() == True):
                        c = int(c)
                        if (c > 17):
                            d = input("Enter Spy Rating(Out of 10): ")
                            if (d.isnumeric() == True):
                                d = int(d)
                                if (d < 11):
                                    e = input("Enter Spy Experience: ")
                                    if (e.isnumeric() == True):
                                        e = int(e)
                                        f = c - 18
                                        if (e <= f):
                                            print("           -------------------")
                                            print("           WELCOME TO SPYCHAT")
                                            print("           -------------------")
                                            print("SPY NAME  : " + gend + a.upper())
                                            print("SPY AGE   : " + str(c))
                                            print("SPY RATING: " + str(d))
                                            if (e == 0):
                                                mes = "MESSAGE   : HELLO ROOKIE, HOPE YOU LEARN A LOT FROM YOUR SENIORS."
                                                print(mes)
                                            elif (e == 1):
                                                mes = "MESSAGE   : HELLO, I HOPE YOU HAVE A GREAT TIME HERE. I BELIEVE THAT BY ASSOCIATING WITH US YOU CAN LEARN A LOT."
                                                print(mes)
                                            elif (e == 2):
                                                mes = "MESSAGE   : HELLO, YOU ARE A ROOKIE NOW BUT WITH TIME AND PROPER DETERMINATION YOU CAN BECOME A PROFESSIONAL TOO"
                                                print(mes)
                                            elif (e == 3):
                                                mes = "MESSAGE   : HELLO, WE NEED MORE SPY LIKE YOU. YOUR 3 YEAR EXPERIENCE CAN BE A GOOD ASSET FOR YOUR FURTHER DEVELOPMENT."
                                                print(mes)
                                            elif (e == 4):
                                                mes = "MESSAGE   : HELLO, YOUR 4 YEAR EXPERIENCE IS A GREAT ACCOMPLISHMENT.I HOPE BY ASSOCIATING WITH US YOU CAN EXPAND YOUR EXPERIENCE."
                                                print(mes)
                                            elif (e == 5):
                                                mes = "MESSAGE   : HELLO, WITH THE AMOUNT OF EXPERIENCE THAT YOU HAVE,WE CONSIDER YOU A PROFESSIONAL HERE. I HOPE NEW ROOKIES LEARN A LOT FROM YOUR EXPERIENCE"
                                                print(mes)
                                            elif (e > 5):
                                                mes = "MESSAGE   : SINCE YOU HAVE AN EXPERIENCE OF " + str(
                                                    e) + " YEARS, WE CONSIDER YOU A HIGHER LEVEL PROFESSIONAL HERE."
                                                print(mes)
                                            print(" ")
                                            print(" ")
                                            print("YOUR ID HAS BEEN CREATED.")
                                            idh = open(a, 'a')
                                            idh.write(
                                                "SPY NAME: " + gend + a.upper() + "\n" + "SPY AGE: " + str(
                                                    c) + "\n" + "SPY RATING: " + str(d) + "\n")
                                            idh.write(str(mes))
                                            idh.close()
                                            fr = open(a + ' friend list', 'x')
                                            fr.close()
                                            st = open(a + ' status', 'x')
                                            st.close()
                                            f = open('userlist', 'a')
                                            f.write(a + "\n")
                                            f.close()
                                            up = open('userlist and pass', 'a')
                                            up.write(a + " " + password + "\n")
                                            up.close()
                                            mainmenu()

                                        elif (e > f):
                                            print(
                                                "According to your age, you cant have an expereince of more than " + str(
                                                    f) + " year(s).")
                                            new()
                                        else:
                                            print("Enter Valid Experience")
                                            new()
                                    elif (e.isnumeric() == False):
                                        print("Enter valid experience.")
                                        new()
                                else:
                                    print("Rating should be 1 to 10")
                                    new()
                            else:
                                print("Enter Valid Rating")
                                new()
                        else:
                            print("You are not eligible.")
                            new()
                    else:
                        print("Enter Valid Age")
                        new()
                else:
                    print("Password is weak.")
                    new()
            else:
                print("Password should contain both alphabet and number.")
                new()
        else:
            print("Name Can not involve numbers, character or space.")
            new()
    else:
        print("The Name is too Short")
        new()
def old():
    f = open('userlist', 'r')
    nlist = f.readlines()
    f.close()
    print("Existing users are: ")
    f = open('userlist','r')
    print(f.read())
    f.close()
    up = open('userlist and pass','r')
    passlist = up.readlines()
    up.close()
    oldu = input("Enter Username: ")
    while oldu :
        def addstatus():
            print("1. CANT TALK, SPYCHAT ONLY.\n2. AT MOVIES\n3. BUSY\n4. IN MEETING\n5. CUSTOM")
            chs = input("Enter Your Choice: ")
            if chs == "1":
                f = open(oldu + ' status', 'w')
                f.write("CANT TALK, SPYCHAT ONLY")
                f.close()
            elif chs == "2":
                f = open(oldu + ' status', 'w')
                f.write("AT MOVIES")
                f.close()
            elif chs == "3":
                f = open(oldu + ' status', 'w')
                f.write("BUSY")
                f.close()

            elif chs == "4":
                f = open(oldu + ' status', 'w')
                f.write("IN MEETING")
                f.close()
            elif chs == "5":
                stc = input("Enter Status: ")
                f = open(oldu + ' status', 'w')
                f.write(stc.upper())
                f.close()
            else:
                print("Enter Valid Choice")
                menu()
            print("Status Updated")
            menu()
        def showinfo():
            f = open(oldu, 'r')
            print(f.read())
            f.close()
            st = open(oldu+ ' status','r')
            status = st.read()
            st.close()
            print("FRIEND LIST:                                 STATUS:")
            print("------------                                 "+ status)
            f = open(oldu + " friend list", 'r')
            print(f.read())
            f.close()
            print("------------")
            menu()
        def addfriend():
            name = input("Enter Friends username: ")
            f = open('userlist', 'r')
            ulist = f.readlines()
            f.close()
            f = open(oldu+" friend list", 'r')
            afr = f.readlines()
            f.close()
            if ulist.__contains__(name + "\n"):
                if afr.__contains__(name+"\n"):
                    print(name +" is already your friend")
                    menu()
                elif name == oldu:
                    print("You can not add yourself.")
                    menu()
                else:
                    sel = input("Do you wish to add them Yes(y) or No(n)")
                    if sel == "y" or sel == "Y":
                        f = open(oldu + ' friend list', 'a')
                        f.write(name + "\n")
                        f.close()
                        print("Friend is added.")
                        menu()
                    elif sel == "n" or sel == "N":
                        print("Friend is not added.")
                        menu()
                    else:
                        print("Enter Valid choice.")
                        menu()
            else:
                print("Username does not exist.")
                menu()
        def menu():
            print("1. Add Friend\n2. Add/Change Status\n3. Show Information\n4. Change Password\n5. LogOut")
            choice = input("Enter your Choice: ")
            if choice == '1':
                addfriend()
            elif choice == '2':
                addstatus()
            elif choice == '3':
                showinfo()
            elif choice == '4':
                changepass()
            elif choice == '5':
                mainmenu()
            else:
                print("Please enter a valid Choice.")
                menu()

        def changepass():
            oldpp = input("Enter old password: ")
            if oldpp == oldp:
                oldn = input("Enter New Password: ")
                f = open('userlist and pass','r')
                passlist = f.readlines()
                passlist.remove(oldu+" "+oldp+"\n")
                f.close()
                f = open('userlist and pass','w')
                f.writelines(passlist)
                f.close()
                f = open('userlist and pass','a')
                f.write(oldu+" "+oldn +"\n")
                f.close()
                print("Password Updated. Please Login again.")
                mainmenu()
            else:
                print("Old password is wrong.")
                menu()
        if nlist.__contains__(oldu + "\n"):
            oldp = input("Enter password: ")
            if passlist.__contains__(oldu+" "+oldp+"\n"):
                you = open(oldu, 'r')
                print(you.read())
                you.close()
                st = open(oldu+' status','r')
                status = st.read()
                st.close()
                print("FRIEND LIST:                                 STATUS:")
                print("------------                                 "+status)
                fr = open(oldu + ' friend list', 'r')
                print(fr.read())
                print("------------")
                fr.close()
                menu()
            else:
                print("Password is Wrong")
                mainmenu()
                break
        else:
            print("Username does not exist.")
            mainmenu()
#main routine
mainmenu()