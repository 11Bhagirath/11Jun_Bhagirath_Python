# Write a Python program to check the current position of the file cursor using tell().

fl = open("Temp.txt","a")
fl.write("\nHello")

position = fl.tell()
print(f"Cursor Position: {position}")

