from tkinter import *

root = Tk()
root.title("Share Calculator")
root.iconbitmap(r'images/nepse.ico')


def displaying_total():
    info_window.grid(row=6, column=0, columnspan=2)  # display the frame by adding it to the grid.

    TA = Label(info_window, text="Total Amount")
    tans = Label(info_window, text=f"Rs. {total_amount:.2f}")

    BrCom = Label(info_window, text="Broker Commission")
    brcomans = Label(info_window, text=f"Rs. {broker_commission:.2f}")

    DPAmt = Label(info_window, text="DP Amount")
    dpamtans = Label(info_window, text=f"Rs. {DP_Amount:.2f}")

    SEBON = Label(info_window, text="SEBON FEE")
    sebonans = Label(info_window, text=f"Rs. {SEBON_FEE:.2f}")

    AmPay = Label(info_window, text="Amount Payable")
    ampayans = Label(info_window, text=f"Rs. {Amount_payable:.2f}")

    NPPPS = Label(info_window, text="Net Purchase Price Per Share")
    npppsans = Label(info_window, text=f"Rs. {NetPPPS:.2f}")

    TA.grid(row=1, column=0)
    tans.grid(row=1, column=1)

    BrCom.grid(row=2, column=0)
    brcomans.grid(row=2, column=1)

    DPAmt.grid(row=3, column=0)
    dpamtans.grid(row=3, column=1)

    SEBON.grid(row=4, column=0)
    sebonans.grid(row=4, column=1)

    AmPay.grid(row=5, column=0)
    ampayans.grid(row=5, column=1)

    NPPPS.grid(row=6, column=0)
    npppsans.grid(row=6, column=1)


def calculation():
    global DP_Amount
    global broker_commission
    global total_amount
    global SEBON_FEE
    global Amount_payable
    global NetPPPS
    quantity = int(shareQEnt.get())
    price = int(ppEnt.get())
    total_amount = quantity * price

    DP_Amount = 25
    fiftyT = 50000
    fiveL = 500000
    twentyL = 2000000
    OneCr = 10000000

    if total_amount < fiftyT:
        broker_commission = 0.40 / 100 * total_amount
    elif total_amount > fiftyT & total_amount <= fiveL:
        broker_commission = 0.37 / 100 * total_amount
    elif total_amount > fiveL & total_amount <= twentyL:
        broker_commission = 0.34 / 100 * total_amount
    elif total_amount > twentyL & total_amount <= OneCr:
        broker_commission = 0.30 / 100 * total_amount
    else:
        broker_commission = 0.27 / 100 * total_amount

    SEBON_FEE = 0.015 / 100 * total_amount

    Amount_payable = total_amount + broker_commission + DP_Amount + SEBON_FEE
    # print(f"{Amount_payable:.2f}")

    NetPPPS = Amount_payable / quantity
    # print(f"{NetPPPS:.2f}")

    displaying_total()


def cancel():
    shareQEnt.delete(0, END)
    ppEnt.delete(0, END)
    info_window.grid_forget()   # hide the frame by removing it from the grid.
    shareQEnt.focus_set()       # put the cursor back in the entry box ready for next input.


header = Label(root, text="NET Buy/Sell PRICE CALCULATOR", fg="#ff9500")
subheader = Label(root, text="Calculate net price of purchase/Sale when you buy/sell stocks")

transLabl = Label(root, text="Transaction type")
transEnt = Entry(root, width=50, fg="#7f8c8d")
transEnt.insert(0, "Buy")

shareQLabl = Label(root, text="Share Quantity")
shareQEnt = Entry(root, width=50, fg="#2c3e50")

ppLabl = Label(root, text="Purchase Price")
ppEnt = Entry(root, width=50, fg="#2c3e50")

calcButton = Button(root, text="Calculate", fg="#ffffff", bg="#34495e", command=calculation)
cancButton = Button(root, text="Cancel", fg="#ffffff", bg="#bdc3c7", command=cancel)

header.grid(row=0, column=0)
subheader.grid(row=1, column=0)

transLabl.grid(row=2, column=0)
transEnt.grid(row=2, column=1)

shareQLabl.grid(row=3, column=0)
shareQEnt.grid(row=3, column=1)

ppLabl.grid(row=4, column=0)
ppEnt.grid(row=4, column=1)

calcButton.grid(row=5, column=0)
cancButton.grid(row=5, column=1)

info_window = Frame(root)   # create a frame for the output widgets.

root.mainloop()
