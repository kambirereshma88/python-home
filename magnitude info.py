magnitude=input("Enter magnitude value:")
magnitude=float(magnitude)
    
if magnitude >=1.0 and magnitude < 2.0:
    magnitudeinformation= "microearthquakes not felt or rarely felt"
    print("magnitude information:",magnitudeinformation)
elif magnitude >=2.0 and magnitude <4.0:
    magnitudeinformation="very rarely causes damage"
    print("magnitude information:",magnitudeinformation)
elif magnitude >=4.0 and magnitude <5.0:
    magnitudeinformation="Damage done to weak building"
    print("magnitude information:",magnitudeinformation)
elif magnitude >=5.0 and magnitude <6.0:
    print("causes damage to poorly constructed building")
elif magnitude >=6.0 and magnitude <7.0:
    print("causes damage to well built structure")
elif magnitude >=7.0 and magnitude <8.0:
    print("causes damage to most buildings")
elif magnitude >=8.0 and magnitude <9.0:
    print("causes major destruction")
elif magnitude >=9.0:
    print("unbelievable damage")
else:
    print("magnitude value not within defined ranges")
else:
    magnitude == 'Errorvalue':
        print("please enter valid number")
    


