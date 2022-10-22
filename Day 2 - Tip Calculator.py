print("Welcome to the TIP Calculator \n")
bill_amount = input("What is the total of the bill? ")
tip_percentage = input("What is the tip that you want to give? Is it 10, 12, or 15? ")
split = input("How many ways should we split the bill? ")

print("\n")

bill_total = float(bill_amount)
tip_total = float(tip_percentage)
tip_amount = float(bill_total * tip_total / 100)
people = int(split)

total_per_person = float(bill_total + tip_amount) / people
final_amount = round(total_per_person, 2)
final_amount = "{:.2f}".format(total_per_person)

print(f"Ever person must pay $ {final_amount} each")