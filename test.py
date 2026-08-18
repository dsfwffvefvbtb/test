nama = input("masukkan nama anda : ")
bb = int(input("berat badan anda : "))
tb = int(input("tinggi anda (cm) : "))
print ("nama anda : ",nama,)
print("berat badan anda : ",bb)
print("tinggi badan anda : ",tb)
BMI = bb / (tb/100)**2
print ("body mass index anda : ",BMI)
if BMI < 17 : 
  print("keterangan : underweight")
if BMI <=25 : 
  print ("keterangan : ideal")
if BMI > 25 : 
  print ("keterangan : overweight")