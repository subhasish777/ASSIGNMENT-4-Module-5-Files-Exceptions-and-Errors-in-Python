
file_name="output.txt"
with open("output.txt","wt") as fh:
    str1=input("Enter text to write to the file:")
    fh.write(str1)
    print(f"Data successfully written to {file_name} ")

with open("output.txt","at") as fh:
    str1=input("Enter additional data to append to the file")
    fh.write("\n" + str1 )
    print("Data successfully appended")


with open("output.txt","rt") as fh:
    content= fh.read()
    print(f"Final content of {file_name}")
    print(content)