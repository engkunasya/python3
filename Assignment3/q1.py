# Given values
total_volume = 20
concentration_final = 0.35

concentration_A = 0.25
concentration_B = 0.50

# x = Volume A
# y = Volume B
# x + y = 20 = total_volume


# 1) x + y = 20
# 2) 0.25x + 0.50y = 0.35 * 20  |||   c_a * v_a + c_b * v_b = c_f * v_f |||
# 3) from 1,
#   x = 20 - y ||  y = 20 x
# from 2 and 3, x = (0.35 * 20 - 0.50(20-x)) / 0.25

x = (total_volume * concentration_final - total_volume * concentration_B) / (concentration_A - concentration_B)
y = total_volume - x

print(f"Volume of solution A (25% salt): {x} liters")
print(f"Volume of solution B (50% salt): {y} liters")

# PART 2
total_volume2 = 8
concentration_final2 = 0.25

concentration_A2 = 0.15
concentration_B2 = 0.40

x2 = (total_volume2 * concentration_final2 - total_volume2 * concentration_B2) / (concentration_A2 - concentration_B2)
y2 = total_volume - x2

print(f"Volume of solution A (15% sugar): {x2} liters")
print(f"Volume of solution B (40% sugar): {y2} liters")

# PART 3

if (x < 3):
  print("Solution of salt (A) is available can proceed")
else:
  print(f"Solution of salt (A) is not available, please order another {x - 3} liter now")
  
if (y < 3):
  print("Solution of salt (B) is available can proceed")
else:
  print(f"Solution of salt (B) is not available, please order another {y - 3} liter now")

if (x2 < 3):
  print("Solution of sugar (A) is available can proceed")
else:
  print(f"Solution of sugar (A) is not available, please order another {x2 - 3} liter now")
  
if (y2 < 3):
  print("Solution of sugar (B) is available can proceed")
else:
  print(f"Solution of sugar (B) is not available, please order another {y2 - 3} liter now")
