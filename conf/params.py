import datetime

# Purchasing
PURCHASE_PRICE = 650000
DOWNPAYMENT = 420000
LOAN_AMOUNT = PURCHASE_PRICE - DOWNPAYMENT
HOUSE_APPRECIATION = .06

FINANCING_RATE = .075

# Alternatives: 'price', 'sac' or 'sac_inflation'
MORTGAGE_CHOICE = 'sac'
SELLING_COST = .06
CONTRACT_DATE = datetime.date(2014, 1, 20)

# Borrowers' age (mutuários)
BIRTH1 = datetime.date(1968, 3, 28)
BIRTH2 = datetime.date(1970, 9, 1)

PERC_BORROWER1 = 1
PERC_BORROWER2 = 1 - PERC_BORROWER1

# Macroeconomics
INFLATION = .04
TREASURE_RETURN = .05

# Adjustment fees
REFERENCIAL_FEE = 0

# Rental -- about 3.5% of home value per year
RENT_PERCENTAGE = .0029
RENT_RAISING_PERIOD = 12

AMORTIZATION_MONTHS = 182

TAX = .15
CUSTODY_FEE = .0003

# REAL
REAL_RETURN = round((TREASURE_RETURN - INFLATION) * (1 - TAX), 6)
REAL_HOUSE_APPRECIATION = round((HOUSE_APPRECIATION - INFLATION), 6)

DATA = 'data.csv'
