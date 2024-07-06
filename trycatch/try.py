# Errors got 3:
# runtime
# logic
# syntax

try:

    principle = int(input("insert integer:\n"))

except ValueError:
    print("error: not an integer")

except Exception as e:
    print("Something went wrong: {e}")

else:
    print("All is well")
    #the code inside this block get exwecuted only when there is nol errror

finally:
    # 3the code inside this block always executed regardless error or non
    print("TQ regardless")