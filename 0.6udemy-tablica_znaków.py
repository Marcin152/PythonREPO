s = "A python project"
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message = 'Document "cv.doc" was printed or printer: XEROX'
print(message.find(":"))
print(message[message.find(':'):])
print(message[42:])
print(message[message.find(':')+2:])

print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

#exec

q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
q = "a gentleman"
print(q[3])
print(q[6])
print(q[7])
print(q[2])
print(q[0])
print(q[4])
print(q[5])
print(q[1])
print(q[8:])

q = "THE MORSE CODE"
print(q[1:4],q[6])