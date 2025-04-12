# WAP to find out how many days, weeks, months we have life if we live until 90 yeras old 


age = int(input("Enter your age:"))

years_left = 90-age

months_left = years_left * 12
weeks_left  = years_left * 52
days_left   = years_left * 365

print(f"you have {days_left} days {weeks_left} weeks and {months_left} months in life ")