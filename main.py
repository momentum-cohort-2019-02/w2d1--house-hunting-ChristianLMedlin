def house_calculator () :
    total_cost = int(input("How much does your dream home cost? $"))
    
    portion_down_payment = 0.25
    
    down_payment = total_cost * portion_down_payment
    
    current_savings = 0
    
    r = .04
    
    annual_salary = int(input("What is your salary? $"))
    
    portion_saved = float(input("What percentage of your monthly income, entered as a decimal, are you saving? "))
    
    monthly_savings = ((annual_salary / 12) * portion_saved)
    
    i = 1
    while current_savings < down_payment:
        current_savings = ((current_savings + monthly_savings) + current_savings*r/12)
        
        if current_savings >= down_payment:
            print("You need to save for " + str(i) + " more months until your purchase.")
        elif current_savings < down_payment:
            i += 1
        
house_calculator()