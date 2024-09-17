while True:
    r1 = int(input("R1: "))
    r2 = int(input("R2: "))

    if r1 == 0 or r2 == 0:
        print("PROGRAMA FINALIZADO")
        break
    else:
        R = (r1 * r2) / (r1 + r2)
        print(f"RESISTENCIA: {R:.2f}")        
    
