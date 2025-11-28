"""To find the compound interest"""
principal =float(input("Enter the principal amount "))
rate=float(input("Enter the interest rate "))
time=float(input("Enter the time "))
amount=principal*(1+rate/100)**time
amount1=principal*pow((1+rate/100),time)
compound_interest=amount-principal
compound_interest1=amount1-principal
print("The compound interest is", compound_interest)
print("The compound interest is", round(compound_interest1,2))