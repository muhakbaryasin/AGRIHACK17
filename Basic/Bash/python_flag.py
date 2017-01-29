import base64
import sys
len_argv = len(sys.argv)
import os
if len_argv > 1:
	print('udah masuk')
	for each_ in sys.argv:
		try:
			#print(each_)
			anu = base64.b64decode( each_ ).decode()
			if anu.find('AGRI') > -1:
				print(anu)
			
		except Exception as e:
			continue
	
else:
	print(len_argv)
	#print(sys.argv)
	print('usage python_flag.py [base64codestring]')
# 
