
# tanda pagar adalah komentar, tidak dieksekusi.

"""

Ini multiline comment, diawali dan diakhiri tanda kutip (") tiga kali.
dimana kamu dapat menyisipkan komentar dalam bentuk paragraf.

"""

# definisikan variable
my_var1 = 65 # Integer
my_var2 = 0x47 # Heksadecimal
my_var3 = [82, 'ini index ke 1'] # List
my_var4 = "73" # String
my_var5 = 0b1111011 # Binary

# ubah string ke integer
my_var4 = int(my_var4)

# ubah integer ke ASCII karakter
char_123 = chr(my_var5)

# operasi aritmatik
char_121 = 56 + my_var1 / 1

# append string 
flag = "Flag: " + chr(my_var1)

# akses index list
my_var3 = my_var3[0]

# looping
new_list = [119, 107, 114, 113, 98, 108, 118, 98, 104, 100, 118, 124, 98, 100, 113, 103, 98, 102, 114, 114, 111, 128]
sesuatu = []

for counter in range(len(new_list)):
	sesuatu.append(new_list[counter]-3)

# inline looping
sesuatu = [item-3 for item in new_list]

# conditional statement
if sesuatu[0] == 116:
	# menggabungkan banyak variable
	flag = flag + chr(my_var2) + chr(my_var3)
elif sesuatu[0] == 119:
	print "Ini gak dieksekusi"
else:
	print "ini juga gak dieksekusi"

# ubah array of number menjadi string
string_ = "".join([chr(number) for number in sesuatu])

flag = flag + chr(my_var4) + char_123 + chr(char_121) + string_

# memotong string
flag_kiri = flag[:11]
flag_kanan = flag[11:]


flag = flag_kiri + 'p' + flag_kanan
