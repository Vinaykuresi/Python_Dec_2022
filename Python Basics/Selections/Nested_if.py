
# if under if
# condition inside condition

# 2 conditions

# 1 -> airline checking
# 2 -> baggage weight checking

airline = "Emirates"

luaggage_weight = 35
AI_weight_limit = 30

extra_amount = 500

if(airline == "AirIndia"):
    extra_amount_charged = 0
    if(luaggage_weight <= AI_weight_limit):
        print("No amount charged")
    else:
        extra_amount_charged = (luaggage_weight - AI_weight_limit) * extra_amount
        print("Baggage amount charged : ", extra_amount_charged)
elif(airline == "Emirates"):
    print("No amount charged")

