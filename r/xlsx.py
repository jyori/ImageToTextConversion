import xlsxwriter 

workbook = xlsxwriter.Workbook('check.xlsx') 
worksheet = workbook.add_worksheet() 
 
r = 0
c = 0
j = 0

content = ["A", "B", "C", "D",
            " ", "F", "G", "H"] 


"""for r in range(0,2):
	j = 0"""
for i in content:
	if j<4:
		worksheet.write(r, c+j, i)
		j += 1
	else:
		j=0
		r +=1
		if j<4:
			worksheet.write(r, c+j, i)
			j += 1


workbook.close() 

"""for r in range(1,2):
	for i in content :
		worksheet.write(r, c, i)
		c +=1
		print(3)
	print(1)
	r += 1
	print(2)
	
workbook.close() 
"""