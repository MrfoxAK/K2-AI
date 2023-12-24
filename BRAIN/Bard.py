from bardapi import BardCookies
import datetime

cookie_dict = {
     "__Secure-1PSID" : "dQibpSnrSt0Q0eax0KQ-q3ekQCEQnMGT5p2Gxs9nLb-zoqOZXfUhx_mYHcnlBEKqtmEJHg.",
     "__Secure-1PSIDTS" : "sidts-CjEBPVxjSqhs-S7kB3ofUD8LJp5FvTBVlRlDdI72MHEIZOpXNWBSu9pj235hrUbcQCNOEAA",
     "__Secure-1PSIDCC" : "ABTWhQH9dVHAg6Mve-m8EJDEyahtjvhN8nTRxp2laEQUBCmNcWN1_l3Y4RFNA1a1T_8QKZ6m1qc"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
     Query = input("Enter Your Query")
     Reply = bard.get_answer(Query)['content']
     print(Reply)








