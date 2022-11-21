Tax = (4, 7, 8, 23)
print(Tax[-2])
print(Tax.index(7))
print(Tax.count(8))
print(max(Tax))

TaxList = list(Tax)

print(Tax)
print(TaxList)
NewTax = tuple(TaxList)

print(Tax)
print(TaxList)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1,tax2,tax3,tax4)

a = 1
b = 10
print("a = ",a,"\tb = ",b)

#temp = a
#a = b
#b = temp

(a,b) = (b,a)
print("a = ",a,"\tb = ",b)

#exec

marketing = ['loyality program', 'client promotion', 'market reseatch']
marketing.append('public relations')
print(marketing[3])

marketing.insert(2,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)

internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)

listaTuple = tuple(emailMarketing)
print(listaTuple)