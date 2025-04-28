def menes_generators(s=0):
    """
    This function generates the names of the months in Latvian.
    It uses a generator to yield each month one by one.
    """
    a = ["Janvāris","Februāris","Marts",
        "Aprīlis","Maijs","Jūnijs",
        "Jūlijs","Augusts","Septembris",
        "Oktobris","Novembris","Decembris"]

    while True:
        yield a[s]
        s = (s+1)%12

aa = input("Ievadi menesi numurs: ") 
bb = input("Ievadi meneses saraksta garums: ")
      
okt = menes_generators(int(aa)-1)


for i in range(int(bb)):
    print(okt.__next__())