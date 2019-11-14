class UnidaysDiscountChallenge:
    basket = [0,0,0,0,0]
    
    def __init__(self, pricingRules):
        self.A = pricingRules.getPriceA()
        self.B = pricingRules.getPriceB()
        self.C = pricingRules.getPriceC()
        self.D = pricingRules.getPriceD()
        self.E = pricingRules.getPriceE()
        

    def AddToBasket(self):
        userInput = ""
        while userInput.lower() != "x":
            userInput = input("Enter the letter of the item you wish to add to basket (A/B/C/D/E) \
\n Or enter 'x' to calculate total.")
            if userInput.lower() == "a":
                self.basket[0] = self.basket[0] + 1
            elif userInput.lower() == "b":
                self.basket[1] = self.basket[1] + 1
            elif userInput.lower() == "c":
                self.basket[2] = self.basket[2] + 1
            elif userInput.lower() == "d":
                self.basket[3] = self.basket[3] + 1
            elif userInput.lower() == "e":
                self.basket[4] = self.basket[4] + 1
            elif userInput.lower() == "x":
                break
            else:
                print("Invalid input. Try again.")
        return self.CalculateTotalPrice()
                

    def CalculateTotalPrice(self):
        #get how many of each item is in basket
        countA = self.basket[0]
        countB = self.basket[1]
        countC = self.basket[2]
        countD = self.basket[3]
        countE = self.basket[4]

        #multiply the amount of each item by its price
        total = (countA * self.A \
                 + countB * self.B \
                 + countC * self.C \
                 + countD * self.D \
                 + countE * self.E)

        print("Total before discounts: £" + str(total))
        total = pricing.applyDiscounts(countB, countC, countD, countE, total)
        print("Total after discounts: £" + str(total))

        #add delivery fee
        if total > 50 or total == 0:
            print("No delivery fee applicable.")
            return total
        else:
            total = total + 7
            print("Delivery Fee: £7")
            return total
        
    

class PricingRules:
    def __init__(self, A,B,C,D,E):
        #__ prefix makes these private variables
        self.__priceOfA = A 
        self.__priceOfB = B
        self.__priceOfC = C
        self.__priceOfD = D
        self.__priceOfE = E

    #get functions
    def getPriceA(self):
        return self.__priceOfA

    def getPriceB(self):
        return self.__priceOfB

    def getPriceC(self):
        return self.__priceOfC

    def getPriceD(self):
        return self.__priceOfD

    def getPriceE(self):
        return self.__priceOfE
    

        
    def applyDiscounts(self,B,C,D,E,total):
        #doesn't currently take count of item 'A' as it has no applicable discount
        #multiple if statements as these are not mutually exclusive discounts
        #// is integer division
        if B >= 2:
            discount = (B // 2) * 4 #for every 2, reduce price by £4
            total -= discount
        if C >= 3:
            discount = (C // 3) * 2 #for every 3, reduce price by £2
            total -= discount
        if D >= 2:
            discount = (D // 2) * 7 #for every 2, reduce price by £7
            total -= discount
        if E >= 3:
            discount = (E // 3) * 5 #for every 3, reduce price by £5
            total -= discount
        return total




#main
runProgram = True
while runProgram == True:
    pricing = PricingRules(8,12,4,7,5) #creates an instance of pricing rules setting the prices
    discountExample = UnidaysDiscountChallenge(pricing).AddToBasket()
    print("Final total: £" + str(discountExample))
    keepRunning = input("Shop again? y/n").lower()
    while keepRunning != "y" and keepRunning != "n":
        print("Invalid input.")
        keepRunning = input("Shop again? y/n").lower()
    if keepRunning == "n":
        runProgram = False
    else:
        runProgram = True
        




    
