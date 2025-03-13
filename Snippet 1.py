db = open("output.txt", "a")

a = "Hello " + str(1)
b = "How do you do?"

db.write(a + "," + b + "\n")

db.close()

with open("output.txt", "r") as db_read:
    print("Contents of output.txt:")
    print(db_read.read())
