import urllib.request, urllib.parse, urllib.error
import ssl
import json
from tkinter import *

window = Tk()
window.wm_title("Covid-19")
var = StringVar()
var1 = StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()
var15=StringVar()
var16=StringVar()
var17=StringVar()
var18=StringVar()
var19=StringVar()
var20=StringVar()
var21=StringVar()
var22=StringVar()
var23=StringVar()
var24=StringVar()
clicked2=StringVar()
clicked1 = StringVar()
clicked1.set("State")
clicked2.set("District")

state_list = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
              'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat',
              'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep',
              'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
              'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh',
              'West Bengal']


def put(value):
    useful_data3 = info[clicked1.get()]["districtData"]

    district_list = []

    for district in useful_data3:
        district_list.append(district)

    drop2 = OptionMenu(window, clicked2, *district_list)
    drop2.grid(row=1, column=1)
    var1.set("Which District ?")

e1 = Label(window, text="Which State/UT ?", font="Arial")
e1.grid(row=0, column=0)
drop1 = OptionMenu(window, clicked1, *state_list, command=put)
drop1.grid(row=0, column=1)


e2 = Label(window, textvariable=var1, font="Arial")
e2.grid(row=1, column=0)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://api.covid19india.org/state_district_wise.json'
url1 = 'https://api.covid19india.org/zones.json'
url2 = 'https://api.covid19india.org/data.json'

uh = urllib.request.urlopen(url, context=ctx)
uh1 = urllib.request.urlopen(url1, context=ctx)
uh2 = urllib.request.urlopen(url2, context=ctx)

data = uh.read()
data1 = uh1.read()
data2 = uh2.read()

info = json.loads(data)
info1 = json.loads(data1)
info2 = json.loads(data2)


def putt():

    state = clicked1.get()
    city = clicked2.get()

    useful_data = info[state]['districtData'][city]
    useful_data1 = info1['zones']
    useful_data2 = info2['cases_time_series'][-1]

    for zone in useful_data1:
        if zone['district'] == city:
            special = zone['zone']
    active = useful_data['active']
    confirmed = useful_data['confirmed']
    deceased = useful_data['deceased']
    recovered = useful_data['recovered']
    # nationwide
    newcases = useful_data2['dailyconfirmed']
    newdeaths = useful_data2['dailydeceased']
    newrecovered = useful_data2['dailyrecovered']
    date = useful_data2['date']
    totconfirm = useful_data2['totalconfirmed']
    totrecvrd = useful_data2['totalrecovered']
    totdcsd = useful_data2['totaldeceased']
    totactive = int(totconfirm) - int(totrecvrd) - int(totdcsd)

    a = 'New cases as on ' + date + ':' + newcases
    b = 'New recovered as on ' + date + ':' + newrecovered
    c = 'New deaths as on ' + date + ':' + newdeaths
    city_name['bg']="Aquamarine"
    Nation['bg'] = "Aquamarine"
    var.set(city)
    var10.set("National Tally as of "+date)
    var2.set("Confirmed Cases")
    var3.set(confirmed)
    var4.set("Active Cases")
    var5.set(active)
    var6.set("Recovered")
    var7.set(recovered)
    var8.set("Deceased")
    var9.set(deceased)
    var11.set("Total Cases")
    var12.set(totconfirm)
    var13.set("Active Cases")
    var14.set(totactive)
    var15.set("Total Recovered")
    var16.set(totrecvrd)
    var17.set("New cases as on "+date)
    var18.set(newcases)
    var19.set("New recovered as on "+date)
    var20.set(newrecovered)
    var21.set("New deaths as on "+date)
    var22.set(newdeaths)
    if special=="Red":
        num11['fg']="Red"
        lb11['fg'] = "Red"
    elif special=="Orange":
        num11['fg']="Orange"
        lb11['fg'] = "Orange"
    elif special=="Green":
        num11['fg']="Green"
        lb11['fg'] = "Green"
    var23.set("Zone")
    var24.set(special)


button = Button(window, text="CHECK", bd=4, font="Arial", activeforeground="Tomato",
                activebackground="Medium Aquamarine", command=putt)
button.grid(row=2, column=1)

city_name = Label(window, width=22, height=1, bd=8, fg="Indigo", font="Boulder", textvariable=var)
city_name.grid(row=4, column=0)

lb1 = Label(window, font="Arial",fg="Royal Blue", textvariable=var2)
lb1.grid(row=5, column=0)
num1=Label(window,font="Arial",fg="Royal Blue", textvariable=var3)
num1.grid(row=5,column=1)

lb2 = Label(window, font="Arial",fg="Crimson",textvariable=var4)
lb2.grid(row=6, column=0)
num2=Label(window,font="Arial",fg="Crimson",textvariable=var5)
num2.grid(row=6,column=1)

lb3 = Label(window,font="Arial",fg="Forest Green", textvariable=var6)
lb3.grid(row=7, column=0)
num3=Label(window,font="Arial",fg="Forest Green",textvariable=var7)
num3.grid(row=7,column=1)

lb4 = Label(window,font="Arial", textvariable=var8)
lb4.grid(row=8, column=0)
num4=Label(window,font="Arial",textvariable=var9)
num4.grid(row=8,column=1)

Nation=Label(window,width=22, height=1, bd=8, fg="Indigo", font="Boulder",textvariable=var10)
Nation.grid(row=10,column=0)

lb5 = Label(window,font="Arial",fg="Royal Blue", textvariable=var11)
lb5.grid(row=11, column=0)
num5=Label(window,font="Arial",fg="Royal Blue",textvariable=var12)
num5.grid(row=11,column=1)

lb6 = Label(window,font="Arial", fg="Crimson",textvariable=var13)
lb6.grid(row=12, column=0)
num6=Label(window,font="Arial",fg="Crimson",textvariable=var14)
num6.grid(row=12,column=1)

lb7 = Label(window, font="Arial",fg="Forest Green",textvariable=var15)
lb7.grid(row=13, column=0)
num7=Label(window,font="Arial",fg="Forest Green",textvariable=var16)
num7.grid(row=13,column=1)

lb8 = Label(window,font="Arial",fg="Tomato", textvariable=var17)
lb8.grid(row=14, column=0)
num8=Label(window,font="Arial",fg="Tomato",textvariable=var18)
num8.grid(row=14,column=1)

lb9 = Label(window,font="Arial", fg="Yellow Green",textvariable=var19)
lb9.grid(row=15, column=0)
num9=Label(window,font="Arial",fg="Yellow Green",textvariable=var20)
num9.grid(row=15,column=1)

lb10 = Label(window,font="Arial",fg="Teal", textvariable=var21)
lb10.grid(row=16, column=0)
num10=Label(window,font="Arial",fg="Teal",textvariable=var22)
num10.grid(row=16,column=1)

lb11 = Label(window,font="Arial",fg="Teal", textvariable=var23)
lb11.grid(row=9, column=0)
num11=Label(window,font="Arial",fg="Teal",textvariable=var24)
num11.grid(row=9,column=1)

window.mainloop()
