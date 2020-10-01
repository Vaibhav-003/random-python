def main():
#	rf = open("lcg128mix.log","r")
#	wf = open("lcg128mix_out.csv", "w+")

#	rf = open("xoroshiro128plus.log","r")
#	wf = open("xoroshiro128plus_out.csv", "w+")

#	rf = open("xoshiro128plus.log","r")
#	wf = open("xoshiro128plus_out.csv", "w+")

#	rf = open("xoshiro128starstar_test.log","r")
#	wf = open("xoshiro128starstar_out.csv", "w+")	

#	rf = open("xoroshiro128starstar_test.log","r")
#	wf = open("xoroshiro128starstar_out.csv", "w+")

#	rf = open("dieharder.log","r")
#	wf = open("dieharder.csv", "w+")

#	rf = open("mcg128out.log","r")
#	wf = open("mgc128out.csv", "w+")

	rf = open("out.log","r")
	wf = open("fibout.csv", "w+")
	
	rf1 = rf.readlines()
	RNG_name = ""
	test_name = ""
	test_num = ""
	weak_num = 0
	fail_num = 0
	pass_num = 0
	line_array=[]
	str_array = []
	wf.write("RNG Perm; Num of Pass Tests; Num of Weak Tests; Num of Failed Tests \n")
	for x in rf1:

		if "(" in x:
			if pass_num == 0:
				pass
			else:
				wf.write(str(RNG_name) + ";"+ str(pass_num) +";"+ str(weak_num) + ";" + str(fail_num) + "\n")
			for z in str_array:
				wf.write(z) 
			RNG_name = x.split("\n")[0]
			RNG_perm =RNG_name.split("[")[1]
			pass_num = 0
			weak_num = 0
			fail_num = 0
			str_array = []
			
			#print x

		if "PASSED" in x:
			line_array = x.split("|")
			test_name = line_array[0]
			test_num = line_array[1]
			pass_num +=1
			#print x
			#w_str =  ";;;" + test_name + ";" + test_num + ";" + "x;\n"
			
			#str_array.append(w_str)
			#print w_str

		if "WEAK" in x:
			line_array = x.split("|")
			test_name = line_array[0]
			test_num = line_array[1]
			weak_num +=1
			#print x
			#w_str =  ";;;" + test_name + ";" + test_num + ";" + "x;\n"
			
			#str_array.append(w_str)
			#print w_str

		if "FAILED" in x:
			line_array = x.split("|")
			test_name = line_array[0]
			test_num = line_array[1]
			fail_num +=1
			#print x
			#w_str =  ";;;" + test_name + ";" + test_num + ";" + ";x\n"
			#str_array.append(w_str)
			#print w_str
			#print RNG_name +";"+ str(weak_num) + ";" + str(fail_num) + ";;;;\n"
		else:
			pass
		

	
	wf.write(str(RNG_name) + ";"+ str(pass_num) +";"+ str(weak_num) + ";" + str(fail_num) + "\n")
	#for z in str_array:
	#	wf.write(z) 
	wf.close()

if __name__=="__main__":
	main()

