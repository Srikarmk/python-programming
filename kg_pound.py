def conversion():
    print("1.Convert kg to pound")
    print("2.Convert pound to kg")
    print("Choose option - ")
    num=int(input())
    if num==1:
        print("Enter weight in kg - ")
        kg=int(input())
        pound=2.20462 * kg
        print(pound)
    elif num==2:
        print("Enter weight in pound - ")
        pound=int(input())
        kg=0.453592 * pound
        print(kg)
    else:
        print("Choose correct option!")
        conversion()


conversion()