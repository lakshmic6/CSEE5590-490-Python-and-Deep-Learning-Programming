# Program To Find Triplets that sum up to Zero From the given set of given integers
def findTriplets( Array, size ):
    found = True
    number1 = 0
    number2 = 0
    number3 = 0
    for i in range(0, size-2):

        # for the first number a[i]
        number1 = Array[i]

        for j in range( i+1, size-1 ):

            # for the second number a[j]
            number2 = Array[j]

            for k in range( i+3, size ):

                # for the third number a[k]
                number3 = Array[k]
                sum= number1 + number2 + number3

                # checking if the sum is equal to zero
                if ( sum == 0 ):
                    print( "triplets are", Array[i], Array[j], Array[k])
                    found = True

    if ( found == False ):
        print(" Triplets does not exist ")


# Defining the array and it's elements
Array = [2,3,5,0,1,6,7,-2,-3,-5]

# Finding out the length of the array

size = len(Array)
sum = 0

# Calling the function to find the triplets that sum up to 0
findTriplets( Array, size )
