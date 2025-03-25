import datetime


def ExtraCost(ExtraLiability, GlassCoverage, LoanerCar, NumCars):
   # Function that will calculate the extra costs

   if ExtraLiability == "Y":
       ExtraLiabilityCost = 130.00 * NumCars
   else:
       ExtraLiabilityCost = 0.00

   if GlassCoverage == "Y":
       GlassCoverageCost = 86.00 * NumCars
   else:
       GlassCoverageCost = 0.00

   if LoanerCar == "Y":
       LoanerCarCost = 58.00 * NumCars
   else:
       LoanerCarCost = 0.00

   ExtraCosts = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
   
   return ExtraCosts


def GetPayDate(InvDate):
    # Function to determine the pay date. Pay date is based off 20 days after the claim or the first day of the next month, whichever is later.
    Inv20 = InvDate + datetime.timedelta(days = 20)

    PurYear = InvDate.year
    PurMonth = InvDate.month
    PurDay = InvDate.day

    PayYear = PurYear
    PayMonth = PurMonth + 1
    if PayMonth == 13:
        PayMonth -= 12
        PayYear += 1
    
    PayDay = 1
    PayFirst = datetime.datetime(PayYear, PayMonth, PayDay)

    if Inv20 > PayFirst:
        PayDate = Inv20
    else:
        PayDate = PayFirst

    return PayDate


def MonthPay(FullOrMonthly, TotalInsurance, DownPay, PROCESS_FEE):
    if FullOrMonthly == "Full":
        MonthPay = 0
    elif FullOrMonthly == "Down Pay":
        MonthPay = ((TotalInsurance - DownPay) + PROCESS_FEE) / 8
    else:
        MonthPay = (TotalInsurance + PROCESS_FEE) / 8

    return MonthPay


def Payment(FullOrMonthly):
    if FullOrMonthly == "Full":
        PayMsg = "Paid in full"
    elif FullOrMonthly == "Down Pay":
        PayMsg = "Down Payment"
    else:
        PayMsg = "Monthly payments"
    
    return PayMsg
