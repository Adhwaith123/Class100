class atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber
    def start(self):
        print("started"+self.atmCardNumber)

ATM=atm("CashWithdrawl","BalanceEnquiry")
ATM.start()

