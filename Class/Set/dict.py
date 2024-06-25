#Python dictionary is also called JSON in other programming language.
#EQ TO JSON
#using JSON for Py which is using {}
#The data is ordered
#TRhe data is indexed by key (not by number)
#Every single data is associated with a key
#


foreigner = {
    "firstname": "Peter",
    "lastname": "Parker",
    "passportno": "EA45555",
    "incometaxno": "SG9302",
    "pcbamount": 892,
    "lastmonth": 5,
    "lastyear": 2024,
    "prevmonth":[(4,2024,891),(3,2024,900),(2,2024,1200)],
    "address": { "office":
                {"street": "Jalan Mark Valley"}}
}

for month, year, amount in foreigner["prevmonth"]:
    print(f"Transaction: {month}-{year} RM:{amount}")

#for tupple get data
street_name = foreigner["address"]["office"]["street"]
print(street_name)


#method item()
for key,value in foreigner.items():
    print(key,value)

#dictinary modification like append
foreigner["car"] = "burgatti"
foreigner["salary"] = 3400
foreigner["salary"] = 7000
foreigner.pop("car")
print(foreigner)
print(foreigner["salary"])
