#NESTED DICTIONARIES
#EX..
stundent = {
    "name" : "amit",
    "score" : {
        "chem" : 92,
        "phy" : 56,
        "math" : 93
    }
}
print(stundent["score"]["chem"])