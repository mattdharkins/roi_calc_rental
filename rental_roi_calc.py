class RentalCalc():
    def __init__(self):
        self.properties = {}
        self.income = {'Rental Income':[],'Other Income':[]}
        self.expenses = {
            'Taxes':[], 'Insurance':[], 'Utilities':[], 'HOA':[], 'Lawncare':[], 'Vacancy Allowance':[], 'Repair and Maint':[],
            'CapEx Allowance':[], 'Mortgage':[], 'Management':[], 'Other Expenses': [] 
            }
        self.acq = {'Down Payment':[], 'Closing Costs':[], 'Rehab Budget':[], 'Other Acquisition Costs':[]}
        

    def gather_info(self):
        address = input("What is the property street address? ")
        address_formatted = address.title()
        rental_income_value = int(input("Let's look at the income for the property.\nEnter the amount of rental income: "))
        self.income['Rental Income'] = rental_income_value
        other_income_value = int(input("Other Income: "))
        self.income['Other Income'] = other_income_value
        income_values = self.income.values()
        total_income = sum(income_values)
        income_formatted = format(total_income, ",")
        print(f" --- Total Income ${income_formatted} ---")
        taxes_value = int(input("\nLet's move on to expenses.\nEnter the amount of taxes: "))
        self.expenses['Taxes'] = taxes_value
        ins_value = int(input("Insurance: "))
        self.expenses['Insurance'] = ins_value
        util_value = int(input("Utilities (if you're paying): "))
        self.expenses['Utilities'] = util_value
        hoa_value = int(input("HOA fees: "))
        self.expenses['HOA'] = hoa_value
        lawn_value = int(input("Lawncare: "))
        self.expenses['Lawncare'] = lawn_value
        vacancy_value = int(input("Vacancy Allowance: "))
        self.expenses['Vacancy Allowance'] = vacancy_value
        repairs_value = int(input("Repair and Maint: "))
        self.expenses['Repair and Maint'] = repairs_value
        capex_value = int(input("Capital Expenditures Allowance: "))
        self.expenses['CapEx Allowance'] = capex_value
        mtg_value = int(input("Mortgage Payment: "))
        self.expenses['Mortgage'] = mtg_value
        mgmt_value = int(input("Property Management: "))
        self.expenses['Management'] = mgmt_value
        other_exp_value = int(input("Other Expenses: "))
        self.expenses['Other Expenses'] = other_exp_value
        expense_values = self.expenses.values()
        total_expenses = sum(expense_values)
        expenses_formatted = format(total_expenses, ",")
        print(f" --- Total Expenses ${expenses_formatted} ---")
        down_pmt_value = int(input("\nLet's move on to acquisition costs.\nEnter the amount of the down payment: "))
        self.acq['Down Payment'] = down_pmt_value
        closing_costs_value = int(input("Closing Costs: "))
        self.acq['Closing Costs'] = closing_costs_value
        rehab_value = int(input("Rehab Budget: "))
        self.acq['Rehab Budget'] = rehab_value
        other_acq_value = int(input("Other Acquisition Costs: "))
        self.acq['Other Acquisition Costs'] = other_acq_value
        acq_values = self.acq.values()
        total_acq = sum(acq_values)
        acq_formatted = format(total_acq, ",")
        print(f" --- Total Acquisition Costs ${acq_formatted} ---")
        annual_cash_flow = (total_income - total_expenses) * 12
        acf_formatted = format(annual_cash_flow, ",")
        annual_return = annual_cash_flow / total_acq
        percent_convert = annual_return * 100
        annual_return_rounded = round(percent_convert, 2)
        print(f"\n\n ---  Property Analysis for: {address_formatted}  ---  \n")
        print(f"      Income:   {income_formatted}")
        print(f"      Expenses:  {expenses_formatted}")
        print(f"      Annual Cash Flow: {acf_formatted}\n")
        print(f"  **The cash on cash ROI is {annual_return_rounded}%\n\n")


calc_user = RentalCalc()


def use_calc():
    calc_active = True
    print("Welcome to the Rental Property ROI Calculator!\n")
    print("Important: When entering numbers in calculator, use only whole numbers without commas. (Ex: 1,000 as 1000)")
    while calc_active:
        answer = input("What would you like to do?\n1: Start Calculating  | 2: Exit ")
        if answer == '1':
            calc_user.gather_info()
        elif answer == '2':
            calc_active = False


use_calc()




