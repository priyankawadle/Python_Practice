import datetime as dt
class TaxPayer:
    def __init__(self,name,PAN,income,dob):
        self.__name = name
        self.__PAN = PAN
        self._income = income
        self.__dob = dob
        self.__age = self.calculate_age()
    
    def print_profile(self):
        print("Name is: ",self.__name)
        print("PAN is: ",self.__PAN)
        print("Income is: ",self._income)
        print("dob of person is: ",self.__dob)
        print("age of person is: ",self.__age)

    def calculate_age(self):
        dobarr = self.__dob.split("/")
        dob_date = dobarr[0]
        dob_month = dobarr[1]
        dob_year = dobarr[2]
        today = dt.datetime.today()
        today_date,today_month,today_year = today.day,today.month,today.year
        if today_month == int(dob_month) and today_date == int(dob_date):
           age = today_year- int(dob_year) 
        else :
            age = today_year- int(dob_year) 
            age -= 1
           
        return age




class TaxCalculator(TaxPayer):
    def __init__(self,name,PAN,income,dob):
        super().__init__(name,PAN,income,dob)
        self.taxable_income = self._income

    @property
    def tax(self):
        if self.taxable_income >= 0 and self.taxable_income <= 250000:
            return 0
        elif self.taxable_income >= 250001 and self.taxable_income <= 500000:
            return round( ((self.taxable_income-250000) * 5/100),2)
        elif self.taxable_income >= 500001 and self.taxable_income <= 1000000:
            return round(((self.taxable_income-500000 )* 10/100+12500),2)
        else:
            return round(((self.taxable_income -1000000)* 20/100 +62500),2)  

    def apply_standard_deduction(self):
        self.taxable_income = self.taxable_income - 50000

    def print_tax_summary(self):
        self.print_profile()
        print("Taxable income: ",self.taxable_income)
        print("Total tax: ",self.tax)

    def __sub__(self,amt):
        if self.taxable_income < amt:
            print( "Enter amount less than taxable amount")
        else:
            self.taxable_income -= amt

class SeniorCitizenTaxCalculator(TaxCalculator):
    
    @property
    def tax(self):
        if self.taxable_income <= 300000:
            tax = 0
        elif self.taxable_income <= 500000:
            tax = (self.taxable_income - 300000) * 0.05
        elif self.taxable_income <= 1000000:
            tax = (200000 * 0.05) + (self.taxable_income - 500000) * 0.10
        else:
            tax = (200000 * 0.05) + (500000 * 0.10) + (self.taxable_income - 1000000) * 0.20
        return tax




