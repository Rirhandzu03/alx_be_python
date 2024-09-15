
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float (input("Enter your total monthly savings:"))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05


                                            
print("your monthly savings are" , monthly_savings)
print("Projected savings after one year, with interest", projected_savings)
