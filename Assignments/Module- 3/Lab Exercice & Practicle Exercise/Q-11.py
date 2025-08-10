# Write a Python program to handle file exceptions and use the finally block for closing the file.
try:
    f = open("example.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    try:
        f.close()
        print("File closed.")
    except:
        print("No file to close.")

        