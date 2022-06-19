import sys

cart = []
amt = []

print("\t\t\t\t\t\t******WELCOME TO FLIPKART******\n")
x = input("Enter the Name:\n")

count = 5
number = input("Enter a 5-digit password number:\n")

if len(number) == count:
    print("Valid password")
    a = 0

    while a != 6:
        print("\n**************************************************")
        print('Available to shop on Flipkart')

        a = int(input("\nSelect the Item:\n Press 1 \t for Electronics\n Press 2 \t for Mobiles\n Press 3 \t for Appliance\n Press 4 \t for Offer\n Press 5 \t for Bill\n Press 6 \t for Exits\n"))
        print("**************************************************")

        if a == 1:
            print("\n**************************************************")
            print("Welcome to Electronic:")
            e1 = dict([(40000, 'Laptop'), (24000, 'Camera'), (10000, 'Tablets')])
            print(e1)
            e = int(input("\nSelect the Item to buy:\n Press 1 \t for Laptop\t is 40,000\n Press 2 \t for Camera\t is 24,000\n Press 3 \t for Tabelts\t is 10,000\n Press 4 \t for Exits\n"))

            if e == 1:
                print("Laptop is added to cart at Rs 40,000")
                cart.append('Laptop')
                amt.append(40000)
                print(cart)
                print(amt)

            elif e == 2:
                print("Camera is added to cart Rs 24,000")
                cart.append('Camera')
                amt.append(24000)
                print(cart)
                print(amt)

            elif e == 3:
                print("Tablets is added to cart Rs 10,000")
                cart.append('Tablets')
                amt.append(10000)
                print(cart)
                print(amt)

            else:
                print("Exits try again!!!")

        elif a == 2:
            print("\n**************************************************")
            print("\nWelcome to Mobile:")
            m1 = dict([(38000, 'One plus 5T'), (88000, 'i-phone x'),
                      (40000, 'Sumsung Galaxy egde')])
            print(m1)
            m = int(input('\nSelect the Item to buy:\n Press 1 \t for One plus 5T\t is 38,000\n Press 2 \t for i-phone x\t\t is 88,000\n Press 3 \t for Sumsung Galaxy egde is 40,000\n Press 4 \t for Exits\n'))

            if m == 1:
                print("One plus 5T is added to cart Rs 38,000")
                cart.append('One plus 5T')
                amt.append(38000)
                print(cart)
                print(amt)

            elif m == 2:
                print("i-phone x is added to cart Rs 88,000")
                cart.append('i-phone x')
                amt.append(88000)
                print(cart)
                print(amt)

            elif m == 3:
                print("Sumsung Galaxy egde is added to cart Rs 40,000")
                cart.append('Sumsung Galaxy egde')
                amt.append(40000)
                print(cart)
                print(amt)

            else:
                print("Exits try again!!!")

        elif a == 3:
            print("\n**************************************************")
            print("\nWelcome to Appliance:")
            t1 = dict(
                [(22000, 'T.V'), (15000, 'Washing Machine'), (28000, 'A.C')])
            print(t1)

            m = int(input('\nSelect the Item to buy:\n Press 1 \t for T.V\t\t is 22,000\n Press 2 \t for Washing Machine\t is 15,000\n Press 3 \t for A.C\t\t is 28,000\n Press 4 \t for Exits\n'))

            if m == 1:
                print("T.V is added to cart Rs 22,000")
                cart.append('T.V')
                amt.append(22000)
                print(cart)
                print(amt)

            elif m == 2:
                print("Washing Machine is added to cart Rs 15,000")
                cart.append('Washing Machine')
                amt.append(15000)
                print(cart)
                print(amt)

            elif m == 3:
                print("A.C is added to cart Rs 28,000")
                cart.append('A.C')
                amt.append(28000)
                print(cart)
                print(amt)

            else:
                print("Exits try again!!!")

        elif a == 4:
            print("\n**************************************************")
            print("\nWelcome to Offer:")
            t1 = dict([(40000, 'T.V,A.C'), (95000,
                      'i-phone x,One plus 5T'), (45000, 'Laptop,Tablets')])
            print(t1)

            m = int(input('\nSelect the Item to buy:\n Press 1 \t for T.V & A.C\t\t\t is 40,000\n Press 2 \t for i-phone x & One plus 5T\t is 95,000\n Press 3 \t for Laptop & Tablets\t\t is 45,000\n Press 4 \t for Exits\n'))

            if m == 1:
                print("T.V and A.C is added to cart Rs 22,000")
                cart.append('T.V,A.C')
                amt.append(40000)
                print(cart)
                print(amt)

            elif m == 2:
                print("i-phone x and One plus 5T is added to cart Rs 15,000")
                cart.append('i-phone x,One plus 5T')
                amt.append(95000)
                print(cart)
                print(amt)

            elif m == 3:
                print("Laptop and Tablets is added to cart Rs 28,000")
                cart.append('Laptop,Tablets')
                amt.append(45000)
                print(cart)
                print(amt)

            else:
                print("Exits try again!!!")

        elif a == 5:
            print("\n**************************************************")
            print('\t\t$$$$$ Bill $$$$$\n')

            if not cart:

                print("\n**************************************************")
                print("Name is:", x)
                print("Product is:", cart)
                print("Product price is Rs:", amt)
                print("Total amount before GST:", sum(amt))
                gst = (sum(amt)*9)/100
                total_gst = sum(amt)+(gst)

                print("SGST Rs : ", gst, "%")
                print("GST Rs : ", gst, "%")
                print("Total amount after GST:", total_gst)
                print("\n**************************************************")
                print("\t\t\t\t!!!THANK YOU!!!\t\t\t\t")

                print("\n**************************************************")

                sys.exit()

            else:
                print("Do you want to make changes on your cart\n")
                print(cart)
                print(amt)
                m = int(input("\nIf YES enter '1' for NO enter '0'\n"))

                while m == 1:

                    m1 = input("\nEnter the cart index no:\n")
                    del cart[m1]

                    m2 = input("\nEnter the price index no:\n")
                    del amt[m2]

                    print("\nAfter deletion:\n")
                    print(cart)
                    print(amt)
                    print("\n")
                    print("Do you want to make changes on your cart\n")
                    print(cart)
                    print(amt)
                    m = input("\nIf YES enter '1' for NO enter '0' \n")

                # Delivery address
                print("\n**************************************************")
                print("\n\t\t*** Delivary address***")

                c = input("\nEnter State:")

                c1 = input("\nEnter Pincode:")

                c2 = input("\nEnter Town/City:")

                c3 = input("\nEnter Colony/Street/Locality:")

                c4 = input("\nEnter Flat no/Room no:")

                c5 = input("\nEnter Building name/Chawl name:")

                c6 = input("\nEnter the Landmark:")

                count = 0

                nr = input("\nEnter a mobile number: ")

                count = len(nr)

                if count == 10:
                    print("Valid Number")

                else:
                    print("Invalid Number:")

                print("\n**************************************************")
                print("Name is: ", x)
                print("Mobile no is: ", nr)
                print("Product is:", cart)
                print("Product price is Rs:", amt)
                print("Total amount before GST:", sum(amt))
                gst = (sum(amt)*9)/100
                total_gst = sum(amt)+(gst)

                print("SGST Rs : ", gst, "%")
                print("GST Rs : ", gst, "%")
                print("Total amount after GST:", total_gst)
                print("\n**************************************************")

                # Feedback

                print("\t\t***Please give a Feedback***\t")

                c8 = input("\nIf 'YES' Press 1 & For 'NO' Press 0")

                if c8 == 1:

                    c9 = input("\nEnter Feedback:")

                    print("\t\t\t\t!!!THANK YOU!!!\t\t\t\t\n")

                    print("\n**************************************************")

                    sys.exit()

                else:

                    print("\t\t\t\t!!!THANK YOU!!!\t\t\t\t\n")

                    print("\n**************************************************")

                    sys.exit()

else:
    print("\nInvalid password")
    print("\n!!Exits!!\n")
