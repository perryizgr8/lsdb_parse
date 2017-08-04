import json
import Lsa
from lsa_utils import *

file = open('lsdb.json')
lsdb = json.load(file)

Lsas = {}
i = 0
for lsa in lsdb:
    lsa_bytes = lsdb[lsa]['advert'].split()
    for byte in lsa_bytes:
        print(byte)
    age = get_lsa_age(lsa_bytes[0], lsa_bytes[1])
    lsid = get_lsid(lsa_bytes[4], lsa_bytes[5], lsa_bytes[6], lsa_bytes[7])
    rtr = get_rtr(lsa_bytes[8], lsa_bytes[9], lsa_bytes[10], lsa_bytes[11])
    seq = get_seq(lsa_bytes[12], lsa_bytes[13], lsa_bytes[14], lsa_bytes[15])
    Lsas[i] = Lsa.Lsa(age, lsa_bytes[2], lsa_bytes[3], lsid, rtr, seq)
    i = i + 1
print(i)
