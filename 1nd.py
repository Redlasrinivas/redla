amount=float(input("Enter the amount"))
if amount>=5000:
   dis=(amount*10)/100
   tax=(amount*18)/100
   print ("u r tax amount for the items",tax)
   print ("u r discount is",dis)
   print ("u have to pay is ", (amount-dis)+tax)
   print ("visit again")
elif amount>=3000:
   dis=(amount*8)/100
   tax=(amount*10)/100
   print ("u r tax amount for the items",tax)
   print ("u r discount is",dis)
   print ("u have to pay is ",( amount-dis)+tax)
   print ("visit again")
elif amount>=2000:
   dis=(amount*5)/100
   tax=(amount*18)/100
   print ("u r tax amount for the items",tax)
   print ("u r discount is",dis)
   print ("u have to pay is ", (amount-dis)-tax)
   print ("visit again")
elif amount>=1000:
   dis=(amount*3)/100
   tax=(amount*18)/100
   print ("u r tax amount for the items",tax)
   print ("u r discount is",dis)
   print ("u have to pay is ", amount-dis)
   print ("visit again")
else :
   tax=(amount*18)/100
   print ("u r tax amount for the items",tax)
   print ("no discount sry!!! Visit again! Bill is",tax+amount)
