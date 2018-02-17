from exchanges.bitfinex import Bitfinex

btc = Bitfinex().get_current_price()
#btcpergpuperday = 0.00041  #This is the.. actual real number....
btcpergpuperday = 0.00035  # This is my conservative number to be safe
powerpergpuperday = float(0.50)
usdpergpuperday = float(btc) * btcpergpuperday

print "Current price of BTC: " + str(btc)
print "Assumptions: "
print "Each GPU makes " +str(btcpergpuperday)+ " per day ($"+ str(usdpergpuperday)+")"
print "Each GPU costs $" + str(powerpergpuperday) + " per day"

numgpu = float(6)  #number of gpus to start
day = 1
gpucost = 675  # The GPU Cost is a total cost of rig ownership ($4k/6)
balance = 0
amountinvested = 12000
totalyear = 3
yearsreinvest = 3
overhead = 0.2
addtlbal = 0
#essentially the following algorithm applies
# #gpu * ( btcpergpuperday * btc) - (#gpu * (powerpergpuperday))
#Aadding comments
for x in range(1,(totalyear*365)):
    addtlbal = (numgpu * (usdpergpuperday)) - (numgpu * powerpergpuperday)
    balance = balance + (addtlbal * (1 - overhead))
    #print("Balance at day: " + str(x) + " = " + str(balance))
    #print("approx monthly income: " + str(addtlbal * 30))

    if (balance > gpucost and x < (yearsreinvest*365)):
        #need to determine how many gpus we can buy...
        addtlgpu = int(balance / gpucost)
        balance = balance - (addtlgpu * gpucost)
        numgpu = numgpu + addtlgpu
        #print "Purchasing another GPU, now we have " + str(numgpu)
#the idea here is to plan for difficulty to some degree to take profits in a year
    if x == 365:
        btcpergpuperday = 0.0003
        usdpergpuperday = float(btc) * btcpergpuperday
# Again difficulty to take profits over the next year
    if x == 730:
        btcpergpuperday = 0.00025
        usdpergpuperday = float(btc) * btcpergpuperday
print ""
print "======================================================="
print "Summary of Run:"
print "Current Price of BTC: " + str(btc)
print "Total Number of Years: " + str(totalyear)
print "Years Reinvesting:" + str(yearsreinvest)
print "Overhead Assumption: " + str(overhead)
print "Number GPUs at end: " + str(numgpu)
print "Number of rigs at end: " + str(numgpu / 6)
print "Balance at end: " + str(balance)
print "Monthly Approximate Income: " + str((addtlbal * 30))
print "======================================================="
