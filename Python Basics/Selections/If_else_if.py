
# runway -> free : plane can land
# runway -> busy : plane cannot land
# fuel -> low : do emergency land

runway = "Not free"
fuel = "low"

if(runway == "free"):
    print("plane can land")
elif(fuel == "low"):
    print("do emergency land")
else:
    print("plane cannot land")