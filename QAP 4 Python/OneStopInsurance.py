# Description: Insurance policy calculation program.
# Author: Spencer Noseworthy
# Date(s): 25/03/25 - 


# Define required libraries.
import datetime
import FormatValues as FV
import OneStopFunctions as OSF


# Define program constants.
f = open("OPIDef.dat", "r")

POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DISCOUNT_ADDITIONAL = float(f.readline())
EXTRA_COVERAGE = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())

f.close()

CUR_DATE = datetime.datetime.now()
AllowedChar = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'")
AllowedCharNum = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz.-'0123456789")
AllowedUpperCharNum = set("ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789")
AllowedNum = set("1234567890")
AllowedDollar = set("1234567890.") # I was going to include a comma for the allowed charaters for dollar values, 
                                   # but didn't want that to throw off any calculations down the line.
ProvLst = ["NL", "NS", "PE", "NB", "ON", "QC", "MB", "BC", "SK", "AB", "NT", "NU", "YT"]
PayLst = ["Monthly", "Full", "Down Pay"]


# Define program functions.


# Main program starts here.
while True:
    # Gather user inputs.

    # I know validations are not required, but after a few I decided to just 
    # validate them all to ensure they're not empty.

    # Using it as a little bit of a challenge to both myself and to you, see if you can break it!
 

    while True:
        CustFirst = input("Enter the customer's first name (End to stop): ").title()
        if CustFirst == "":
            print()
            print("   Error - First name cannot be blank.")
            print()
        elif set(CustFirst).issubset(AllowedChar) == False:
            print()
            print("   Error - First name contains invalid characters.")
            print()
        else:
            break
    
    if CustFirst == "End":
        break

    while True:
        CustLast = input("Enter the customer's last name: ").title()
        if CustLast == "":
            print()
            print("   Error - Last name cannot be blank.")
            print()
        elif set(CustLast).issubset(AllowedChar) == False:
            print()
            print("   Error - Last name contains invalid characters.")
            print()
        else:
            break

    while True:
        Address = input("Enter the customer's address: ").title()
        if Address == "":
            print()
            print("   Error - Customer address cannot be blank.")
            print()
        elif set(Address).issubset(AllowedCharNum) == False:
            print()
            print("   Error - Address contains invalid characters.")
            print()
        else:
            break

    while True:
        City = input("Enter the city: ").title()
        if City == "":
            print()
            print("   Error - City cannot be blank.")
            print()
        elif set(City).issubset(AllowedChar) == False:
            print()
            print("   Error - City contains invalid characters.")
            print()
        else:
            break

    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov not in ProvLst:
            print()
            print("   Error - Province is invalid.")
            print()
        else:
            break
          
    while True:
        Postal = input("Enter the postal code (X0X0X0): ").upper()
        if Postal == "":
            print()
            print("   Error - Postal code cannot be blank.")
            print()
        elif len(Postal) != 6:
            print()
            print("   Error - Postal code must be 6 digits.")
            print()
        elif set(Postal).issubset(AllowedUpperCharNum) == False:
            print()
            print("   Error - Last name contains invalid characters.")
            print()
        else:
            break
 
    while True:
        Phone = input("Enter the customer phone number (0000000000): ")
        if Phone == "":
            print()
            print("   Error - Phone number cannot be blank.")
            print()
        elif set(Phone).issubset(AllowedNum) == False:
            print()
            print("   Error - Phone number must be digits only.")
            print()
        elif len(Phone) != 10:
            print()
            print("   Error - Phone number must be 10 digits long.")
            print()
        else:
            break
        
    while True:
        try:
            NumCars = input("Enter the number of cars being insured: ")
            NumCars = int(NumCars)
        except:
            print()
            print("   Error - Number of cars is not a valid integer.")
            print()
        else:
            break
        
    while True:
        ExtraLiability = input("Enter the option for extra liability (Y/N): ").upper()
        if ExtraLiability != "Y" and ExtraLiability != "N":
            print()
            print("   Error - Extra liablilty option must be a Y(es) or an N(o).")
            print()
        else:
            break

    while True:
        GlassCoverage = input("Enter the option for glass coverage (Y/N): ").upper()
        if GlassCoverage != "Y" and GlassCoverage != "N":
            print()
            print("   Error - Glass coverage option must be a Y(es) or an N(o).")
            print()
        else:
            break

    while True:
        LoanerCar = input("Enter the option for a loaner car (Y/N): ").upper()
        if LoanerCar != "Y" and LoanerCar != "N":
            print()
            print("   Error - Loaner car option must be a Y(es) or an N(o).")
            print()
        else:
            break
            
    while True: 
        FullOrMonthly = input("Enter the option for payment (Full, Monthly or Down Pay): ").title()
        if FullOrMonthly not in PayLst:
            print()
            print("   Error - Option for payment must be either; Full, Monthly or Down Pay.")
            print()
        else:
            break
           
    DownPay = 0
    if FullOrMonthly == "Down Pay":
        try:
            DownPay = input("Enter the amount of the down payment: ")
            DownPay = float(DownPay)
        except:
            print()
            print("   Error - Down payment is not a valid integer.")
            print()
        
    
    ClaimNumLst = []
    ClaimDateLst = []
    ClaimAmtLst = []
    while True:
        while True:
            ClaimNum = input("Enter the claim number (00000) (99999 to end): ")
            if ClaimNum == "":
                print()
                print("   Error - Claim number cannot be blank.")
                print()
            elif set(ClaimNum).issubset(AllowedNum) == False:
                print()
                print("   Error - Claim number must be only digits.")
                print()
            elif len(ClaimNum) != 5:
                print()
                print("   Error - Claim number must be 5 digits long.")
                print()
            else:
                break
        if ClaimNum == "99999":
            break

        while True:
            try:
                ClaimDate = input("Enter the claim date (YYYY-MM-DD): ")
                ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
            except:
                print()
                print("   Error - Date is invalid. Use YYYY-MM-DD format.")
                print()
            else:
                break
            
        while True:
            try:
                ClaimAmt = input("Enter the claim amount: ")
                ClaimAmt = float(ClaimAmt)
            except:
                print()
                print("   Error - Down payment is not a valid float value.")
                print()
            else:
                break

        ClaimNumLst.append(ClaimNum)
        ClaimDateLst.append(ClaimDate)
        ClaimAmtLst.append(ClaimAmt)


    # Perform required calculations.
    InsuranceFirst = BASIC_PREMIUM

    if NumCars == 1:
        InsuranceAdd = 0
    else:
        InsuranceAdd = (BASIC_PREMIUM * DISCOUNT_ADDITIONAL) * (NumCars - 1)

    InsurancePrem = InsuranceFirst + InsuranceAdd

    ExtraCosts = OSF.ExtraCost(ExtraLiability, GlassCoverage, LoanerCar, NumCars)

    BeforeTaxInsurance = InsurancePrem + ExtraCosts
    HST = BeforeTaxInsurance * HST_RATE
    TotalInsurance = HST + BeforeTaxInsurance

    MonthPay = OSF.MonthPay(FullOrMonthly, TotalInsurance, DownPay, PROCESS_FEE)

    PayDate = OSF.GetPayDate(CUR_DATE)
    PayDate = FV.FDateS(PayDate)
    InvDate = FV.FDateS(CUR_DATE)

    PayMsg = OSF.Payment(FullOrMonthly)


    # Concatenation of inputs & some values to make the display a little neater.
    FullName = CustFirst + " " + CustLast
    FullAddress = Address + ", " + City + ", " + Prov + " " + Postal

    if GlassCoverage == "Y":
        GlassMsg = "Glass coverage"
    else:
        GlassMsg = "No glass coverage"

    if ExtraLiability == "Y":
        LiabilityMsg = "Extra liability"
    else:
        LiabilityMsg = "No liability coverage"

    if LoanerCar == "Y":
        LoanerMsg = "Loaner car"
    else:
        LoanerMsg = "No loaner car"
    
    ExtraCoverage = GlassMsg + ", " + LiabilityMsg + ", " + LoanerMsg
    
    
    # Display results
    print()
    print(f"   ONE STOP INSURANCE                                  Policy Number: {POLICY_NUM:>4d}")
    print(f"   Your one stop shop for insurance.              Invoice date: {InvDate}")
    print()
    print(f"   =======================================================================")
    print(f"   Customer information:")
    print(f"   {FullName:<20s}                                     {FV.FPhone14(Phone):>14s}")
    print(f"   {FullAddress:<63s} ") # 63 Characters for the full address brings it right to the end of the dividing line, and just about everything SHOULD fit there.
    print()
    print(f"   Number of Cars: {NumCars:<2d}")
    print(f"   Payment type: {PayMsg:<20s}")
    print(f"   Extra coverage: {ExtraCoverage}")
    print(f"   =======================================================================")
    print(f"   Insurance premium:                                          {FV.FDollar2(InsurancePrem):>11s}")
    print(f"   Extra coverage cost:                                         {FV.FDollar2(ExtraCosts):>10s}")
    print(f"   HST:                                                         {FV.FDollar2(HST):>10s}")
    print(f"   Subtotal:                                                   {FV.FDollar2(TotalInsurance):>11s}")
    print(f"   Monthly payments:                                            {FV.FDollar2(MonthPay):>10s}")
    print(f"   First payment date:                                          {PayDate:>10s}")
    print(f"   =======================================================================")
    print(f"   Claim #                     Claim Date                          Amount")
    print(f"   =======================================================================")
    for i in range(len(ClaimNumLst)):
        print(f"   {ClaimNumLst[i]}                       {FV.FDateS(ClaimDateLst[i])}                      {FV.FDollar2(ClaimAmtLst[i]):>11s}")

    print(f"   =======================================================================")    




       
    # Write the values to a data file for storage.
    f = open(f'Policies.dat', 'a')

    f.write(f"{str(POLICY_NUM)}, ")
    f.write(f"{CustLast}, ")
    f.write(f"{CustFirst}, ")
    f.write(f"{Address}, ")
    f.write(f"{City}, ")
    f.write(f"{Postal}, ")
    f.write(f"{Phone}, ")
    f.write(f"{str(NumCars)}, ")
    f.write(f"{ExtraLiability}, ")
    f.write(f"{GlassCoverage}, ")
    f.write(f"{LoanerCar}, ")
    f.write(f"{PayMsg}, ")
    f.write(f"{FV.FNumber2(DownPay)}, ")
    f.write(f"{str(ClaimNum)}, ")
    f.write(f"{str(ClaimDate)}, ")
    f.write(f"{FV.FNumber2(ClaimAmt)}, ")
    f.write(f"{FV.FNumber2(InsurancePrem)}, ")
    f.write(f"{FV.FNumber2(ExtraCosts)}, ")
    f.write(f"{FV.FNumber2(HST)}, ")
    f.write(f"{FV.FNumber2(TotalInsurance)}, ")
    f.write(f"{FV.FNumber2(MonthPay)}, ")
    f.write(f"{FV.FNumber2(PayDate)}\n ")
    
    f.close()

    print()
    print("   Insurance data has been saved successfully.")
    print()

    POLICY_NUM += 1

    f = open(f'OSIDef.dat', 'w')

    f.write(f"{str(POLICY_NUM)}, ")
    f.write(f"{FV.FNumber2(BASIC_PREMIUM)}, ")
    f.write(f"{FV.FNumber2(DISCOUNT_ADDITIONAL)}, ")
    f.write(f"{FV.FNumber2(EXTRA_COVERAGE)}, ")
    f.write(f"{FV.FNumber2(GLASS_COVERAGE)}, ")
    f.write(f"{FV.FNumber2(LOANER_COVERAGE)}, ")
    f.write(f"{FV.FNumber2(HST_RATE)}, ")
    f.write(f"{FV.FNumber2(PROCESS_FEE)}, ")
    
    f.close()
  
# Any housekeeping duties at the end of the program.
