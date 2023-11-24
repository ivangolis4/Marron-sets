months = ["JANUARY","FEBRUARY","MARCH","APRIL",
          "MAY","JUNE","JULY","AUGUST",
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]

#IVAN N. GOLIS

first_group = set([])
second_group = set([])
s1 = set([])
s2 = set([])
def userInput():
    try:
        return int(input("Enter length:"))
    except ValueError:
        return userInput()


def my_birth_month():
    print("Enter your birth month:")
    for i in months:
        a1 = input().upper()
        if a1 == months[0]:
            s1.add(a1)
            break
        elif a1 == months[1]:
            s1.add(a1)
            break
        elif a1 == months[2]:
            s1.add(a1)
            break
        elif a1 == months[3]:
            s1.add(a1)
            break
        elif a1 == months[4]:
            s1.add(a1)
            break
        elif a1 == months[5]:
            s1.add(a1)
            break
        elif a1 == months[6]:
            s1.add(a1)
            break
        elif a1 == months[7]:
            s1.add(a1)
            break
        elif a1 == months[8]:
            s1.add(a1)
            break
        elif a1 == months[9]:
            s1.add(a1)
            break
        elif a1 == months[10]:
            s1.add(a1)
            break
        elif a1 == months[11]:
            s1.add(a1)
            break
        else:
            print("Invalid Input.")
            return my_birth_month()




def my_classmate_birth_monh():
    print("Enter your classmate birth month:")
    for i in months:
        a1 = input().upper()
        if a1 == months[0]:
            s1.add(a1)
            break
        elif a1 == months[1]:
            s1.add(a1)
            break
        elif a1 == months[2]:
            s1.add(a1)
            break
        elif a1 == months[3]:
            s1.add(a1)
            break
        elif a1 == months[4]:
            s1.add(a1)
            break
        elif a1 == months[5]:
            s1.add(a1)
            break
        elif a1 == months[6]:
            s1.add(a1)
            break
        elif a1 == months[7]:
            s1.add(a1)
            break
        elif a1 == months[8]:
            s1.add(a1)
            break
        elif a1 == months[9]:
            s1.add(a1)
            break
        elif a1 == months[10]:
            s1.add(a1)
            break
        elif a1 == months[11]:
            s1.add(a1)
            break
        else:
            print("Invalid Input.")
            return my_birth_month()




my_birth_month()
my_classmate_birth_monh()

if s1 == s2:
    print("The same birth month.")
else:
    print("Not the same birth month.")

