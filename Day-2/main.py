print("Welcome to tip calculator")
totalbill=float(input("Please Enter the Total Bill:"))
tip=int(input("How Much Tip U Want To Give 10 or 12 or 15?:"))
members=int(input("How many People are Present?:"))
Finalbill=(1+tip/100)*totalbill
eachonebill=round(Finalbill/members,2)
print(f"Each Person Should pay a bill of {eachonebill} Rupees")