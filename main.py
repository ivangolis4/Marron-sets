def num_of_length():
    try:
        return int(input("Enter Length: "))
    except ValueError:
        print("Invalid!")
        return num_of_length()


def your_birth_month():
    count = 0
    month = input("Enter your Birth Month: ").lower()
    while count < 1:
        if month == "january":
            count += 1
            m1.add(month)
        elif month == "february":
            count += 1
            m1.add(month)
        elif month == "march":
            count += 1
            m1.add(month)
        elif month == "april":
            count += 1
            m1.add(month)
        elif month == "may":
            count += 1
            m1.add(month)
        elif month == "june":
            count += 1
            m1.add(month)
        elif month == "july":
            count += 1
            m1.add(month)
        elif month == "august":
            count += 1
            m1.add(month)
        elif month == "september":
            count += 1
            m1.add(month)
        elif month == "october":
            count += 1
            m1.add(month)
        elif month == "november":
            count += 1
            m1.add(month)
        elif month == "december":
            count += 1
            m1.add(month)
        else:
            print("Invalid Input!")
            return your_birth_month()


def classmate_birth_month():
    count2 = 0
    month2 = input("Enter your Classmates Birth Month: ").lower()
    while count2 < 1:
        if month2 == "january":
            count2 += 1
            m2.add(month2)
        elif month2 == "february":
            count2 += 1
            m2.add(month2)
        elif month2 == "march":
            count2 += 1
            m2.add(month2)
        elif month2 == "april":
            count2 += 1
            m2.add(month2)
        elif month2 == "may":
            count2 += 1
            m2.add(month2)
        elif month2 == "june":
            count2 += 1
            m2.add(month2)
        elif month2 == "july":
            count2 += 1
            m2.add(month2)
        elif month2 == "august":
            count2 += 1
            m2.add(month2)
        elif month2 == "september":
            count2 += 1
            m2.add(month2)
        elif month2 == "october":
            count2 += 1
            m2.add(month2)
        elif month2 == "november":
            count2 += 1
            m2.add(month2)
        elif month2 == "december":
            count2 += 1
            m2.add(month2)
        else:
            print("Invalid Input!")
            return classmate_birth_month()


m1 = set([])
m2 = set([])

g1 = set([])
g2 = set([])
length = num_of_length()


print("Enter first group: ")
for i in range(length):
    group1 = input()
    g1.add(group1)

print("Enter Second Group:")
for o in range(length):
    group2 = input()
    g2.add(group2)


print("set1: ", g1)
print("set2: ", g2)

print("Union: ", g1.union(g2))
print("Intersection: ", g1.intersection(g2))
print("Difference: ", g1.difference(g2))

ybm = your_birth_month()

cm = classmate_birth_month()


if m1 == m2:
    print("The same Birth Month")

else:
    print("Not the same Birth Month")
