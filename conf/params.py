import datetime

# Purchasing
PURCHASE_PRICE = 500000
DOWNPAYMENT = 250000
LOAN_AMOUNT = PURCHASE_PRICE - DOWNPAYMENT
INTEREST_RATE = .08
AMORTIZATION_YEARS = 30
AMORTIZATION_MONTHS = None
MORTGAGE_CHOICE = 'sac'
SELLING_COST = .06
CONTRACT_DATE = datetime.date(2010, 1, 1)

# Borrowers' age (mutuários)
BIRTH1 = datetime.date(1970, 1, 1)
BIRTH2 = datetime.date(1970, 1, 1)
PERC_BORROWER1 = .6
PERC_BORROWER2 = .4


# Macroeconomics
INFLATION = .02
RETURN_ON_CASH = .04

# Rental
RENT_PERCENTAGE = .002
RENT_RAISING_PERIOD = 12

# Calculated values
if not AMORTIZATION_MONTHS:
    AMORTIZATION_MONTHS = AMORTIZATION_YEARS * 12

TAX = .15
CUSTODY_FEE = .0003
REAL_RETURN = (RETURN_ON_CASH - INFLATION) * (1 - TAX)

DATA = 'data.csv'
