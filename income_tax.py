class TaxPayer:
    def __init__(self,name,PAN,income):
        self.__name = name
        self.__PAN = PAN
        self._income = income
    
    def print_profile(self):
        print("Name is: ",self.__name)
        print("PAN is: ",self.__PAN)
        print("Income is: ",self._income)


class TaxCalculator(TaxPayer):
    def __init__(self,name,PAN,income):
        super().__init__(name,PAN,income)
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


