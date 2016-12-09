def guest_greeting():
    print "Welcome Guest"


def ret_customer():
    print "Returning Customer"
    custid = raw_input("Enter your CustomerID: ")
    customer_data = find_ret_cust(custid)
    if customer_data == "False":
        print "Could not find your ID number: "+custid+"\nPlease Try Again"
        ret_customer()
    else:
        for word in customer_data:
            print word


def find_ret_cust(customer):
    try:
        with open("CustomerList.txt","r") as file:
            data = file.readlines()
            for line in data:
                words = line.split(',')
                if customer == words[0]:
                    return words
        return "False"
    except: print "Could not open CustomerList File"


def new_customer():
    try:
        print "Welcome new customer"
        list = open("CustomerList.txt","r")
        num = str(len(list.readlines())+1) # used to generate customer ID
        list.close()

        print "Please enter the following"
        first = raw_input("First Name: ")
        last = raw_input("Last Name: ")
        str_address = raw_input("Street Address: ")
        city = raw_input("City: ")
        state = raw_input("State(Can be Abbreviated): ")
        zipcode = raw_input("Zipcode: ")
        phone = raw_input("Phone: ")
        # generate a new customer ID number
        new_id = num + phone[-4:]

        print "\nYour Customer ID is: " + new_id
        cust_data = ",".join([new_id,first.title(),last.title(),str_address,city,state,zipcode,phone])
        print cust_data
        # appending CustomerList to include new information
        list = open("CustomerList.txt","a")
        list.writelines(cust_data+"\n")
        list.close()
    except:
        print ("Could not open CustomerList.txt")


choice = 0

while choice != -1:
    print "Hello..."
    print "1. Returning Customer"
    print "2. New Customer"
    print "3. Guest"

    choice = raw_input("Please enter a number: ")

    if choice == '1':
        ret_customer()
        choice = -1
    elif choice == '2':
        new_customer()
        choice = -1
    elif choice == '3':
        guest_greeting()
        choice = -1
    else:
        print "ERROR: Not Valid"
