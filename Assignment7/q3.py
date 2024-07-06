

def band(color_split):
    band_value = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4, "Green": 5, "Blue": 6,
    "Violet": 7,
    "Grey": 8,
    "White": 9}
    
    if len (color_split) == 0 or color_split[0] == color_split[1]:
        return f"Please insert different color(s)"

    elif len(color_split) == 1: 
       return band_value[color_split[0]]

    elif len(color_split) >=2:
        return str(band_value[color_split[0]])+str(band_value[color_split[1]])
    

color_split = [i.capitalize() for i in input("Please enter the color: ").strip().split("-")]
# print(color_split)

value_of_band = band(color_split)
print(value_of_band)




# 1.   Black": 0
# 2.   Brown": 1
# 3.   Red": 2
# 4.   Orange": 3
# 5.   Yellow": 4
# 6.   Green": 5
# 7.   Blue": 6
# 8.   Violet": 7
# 9.   Grey": 8
# 10.  White": 9