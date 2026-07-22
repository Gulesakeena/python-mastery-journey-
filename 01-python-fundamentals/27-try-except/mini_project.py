"""
Safe File Reader
"""

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Program Finished.")