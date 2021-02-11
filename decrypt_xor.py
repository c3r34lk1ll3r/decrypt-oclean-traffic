import sys 
import json
import hashlib
xor_key = '#O+1C9L8E3A1%N0O=2N7E'

f = open(sys.argv[1], 'rb')

to_decrypt = f.read()

clear = ""
indx = 0
for i in to_decrypt:
    ch1 = i
    ch2 = ord(xor_key[indx % (len(xor_key))])
    clear+=chr(ch1 ^ ch2)
    indx+=1


jj = json.loads(clear)
print(jj)

#Str2 = jj['Action']
#BArr = clear
#Master_Key = 'w#2q*ahd=qe-qed673jhdhxzcnb%0-jh'
#TimeStamp = jj['TimeStamp']
### Compute MD5
### str2 == ACTION
### bArr = Decoded
### MD5( str2 + GenerateTimeStamp + "3.0.0" + H5PostTools.MastetKey + new String(bArr))))).upBytes(H5PostTools.XOR(bArr))).execute(absCallback);
#Result = hashlib.md5( (str2 + TimeStamp + "3.0.0" + Master_Key + bArr).encode('ascii') ).hexdigest()
#Assert result == '46157fd4becdef36361252e2fdaa6644'
#Print(result)
