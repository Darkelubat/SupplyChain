x = input("Enter a number of supplier to generate.")
y = input("Max bound of Manager.")

f2 = open("Manager.net", "w")

f3 = open("BAZ.net", "w")

f4 = open("fuse.tpn", "w")

f4.write("load Manager.net\n")
f4.write("load BAZ.net\n")
f4.write("intersect\n")

for i in range(int(x)):
	f = open("Supplier"+str(i)+".net", "w")
	f.write("tr MOD : MOD_S"+str(i)+"_BAZ [1,7] {MOD?} -> p1\n")
	f.write("tr t0 : SO_BAZ_S"+str(i)+" [0,w[ IDLE -> SO2AR\n")
	f.write("tr INS [0,w[ SO2AR -> INS2AR\n")
	f.write("tr POK1"+str(i)+" : POK"+str(i)+" [0,w[ {MOD?} -> END\n")
	f.write("tr POK2"+str(i)+" : MOD_BAZ_S"+str(i)+" p1 -> END\n")
	f.write("tr te : SYNC [0,w[ END ->\n")
	f.write("tr t3 : AR_S"+str(i)+"_BAZ_SO [1,7] INS2AR -> Prod\n")
	f.write("tr product [6,10] Prod -> {MOD?}\n")
	f.write("tr t1 : AR_S"+str(i)+"_BAZ_SO [1,7] SO2AR -> Prod\n")
	f.write("pl IDLE (1)\n")
	f.write("net Supplier"+str(i)+"\n")
	
	f2.write("tr t"+str(i)+": MOD_BAZ_S"+str(i)+" [2,"+y+"] Supplier"+str(i)+" -> IDLE\n")
	f2.write("tr t"+str(i+90)+": MOD_S"+str(i)+"_BAZ"+" IDLE -> Supplier"+str(i)+"\n")
	f2.write("tr Validation"+str(i)+": POK"+str(i)+" IDLE -> IDLE\n")
	f2.write("pl Supplier"+str(i)+"\n")
        
	f3.write("tr t"+str(0+i*10)+" : SO_BAZ_S"+str(i)+" [0,1] IDLE"+str(i)+" -> SO2AR"+str(i)+"\n")
	f3.write("tr t"+str(1+i*10)+" : AR_S"+str(i)+"_BAZ_SO [0,w[ SO2AR"+str(i)+" -> {MOD"+str(i)+"?}\n")
	f3.write("tr MOD"+str(i)+" : MOD_S"+str(i)+"_BAZ [0,w[ {MOD"+str(i)+"?} -> Modification"+str(i)+"\n")
	f3.write("tr POK1"+str(i)+" : POK"+str(i)+" [0,w[ {MOD"+str(i)+"?} -> p"+str(3+i*10)+"\n")
	f3.write("tr POK2"+str(i)+" : MOD_BAZ_S"+str(i)+" [0,w[ Modification"+str(i)+" -> p"+str(3+i*10)+"\n")
	f3.write("tr te : SYNC [0,0] p"+str(3+i*10)+" ->\n")
	f3.write("pl IDLE"+str(i)+" (1)\n")
	
	f4.write("load Supplier"+str(i)+".net\n")
	f4.write("intersect\n")
	
f3.write("net BAZ")
f2.write("pl IDLE (1)\n")
f2.write("net Manager\n")

f4.write("load end.net\n")
f4.write("intersect\n")
