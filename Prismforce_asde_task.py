def can_abhimanyu_cross_chakravyuha(k, p, a, b):
    n = len(k)
    power = p
    skips_left = a
    recharges_left = b


    for i in range(n):
        # Check skipping possibility
        if skips_left > 0:
            skips_left -= 1
            print(f"Skipped enemy {i+1} with power {k[i]}")
            continue

        # Check if recharge left
        if power < k[i] and recharges_left > 0:
            power = p  # Recharge to initial amount of power
            print(f"Recharged! New power is {p}")
            recharges_left -= 1

        # fighting the enemy after exhausting all possible skip and recharge
        if power >= k[i]:
            power -= k[i]
        else:
            print(f"Abhimanyu loses at enemy {i+1} with power {k[i]}")
            return False  
        



        # Special cases for k3 and k7
        if (i == 2 or i == 6) and a > 0:
            regen_power = k[i] // 2
            if p < regen_power:
                if b > 0:
                    b -= 1  # Use a recharge
                    power = p
                    print(f"Recharged during regeneration! New power is {p}")
                else:
                    print(f"Abhimanyu loses to regenerating enemy {i+1}")
                    return False  

            power -= regen_power  # Attack from behind after regenerating
            print(f"Fought regenerating enemy {i+1}, remaining power: {p}")



    return True  # Abhimanyu successfully crosses the Chakravyuha




# Test case 1:
k1 = [20, 30, 50, 40, 60, 70, 80, 90, 100, 110, 120]
p1 = 150
a1 = 3  
b1 = 2  
if can_abhimanyu_cross_chakravyuha(k1, p1, a1, b1):
    print("Abhimanyu can cross the Chakravyuhu in Test Case 1")
else:
    print("Abhimanyu cannot cross the Chakravyuhu in Test Case 1")

print("\n" + "-" * 30 + "\n") #proper gap space between test cases

# Test case 2
k2 = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
p2 = 100
a2 = 1  
b2 = 1  
if can_abhimanyu_cross_chakravyuha(k2, p2, a2, b2):
    print("Abhimanyu can cross the Chakravyuhu in Test Case 2")
else:
    print("Abhimanyu cannot cross the Chakravyuha in Test Case 2")





