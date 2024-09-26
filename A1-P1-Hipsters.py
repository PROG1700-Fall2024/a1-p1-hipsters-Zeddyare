#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #First- find out the values for each variable
    #180/12=$15/km 
    #tax in the example is at 14% (divided total by cost)
    
    #Greeting/description of program
    print("Hipster's Local Vinyl Records - Customer Order Details \n")
  

    #input for cx name
    cxName=input("Enter the customer's name: ")
    
    #input for distance of delivery 
    distance=input("Enter the distance in kilometeres for delivery: ")

    #input for cost of records (assuming no need for number of records, just their cost) 
    recordCost=input("Enter the cost of records purchased: " ) 
    print(" ") #I know theres an easier way to do this but with an input I'm not sure what it is 

    #Math time - had to remember to use floats 
    deliveryCost=float(distance)*15
    purchaseCost=float(recordCost)*1.14
    totalCost=float(purchaseCost)+float(deliveryCost)


    #output message for summary
    print("Purchase summary for",cxName)
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))
    print("Purchase Cost: ${0:.2f}".format(purchaseCost))
    print("Total Cost   : ${0:.2f}".format(totalCost))
    # YOUR CODE ENDS HERE

main()