
file_name="sample.txt"
try:
    with open ("sample.txt","rt") as fh:
        print("Reading file contents")
        print(fh.readline())
        print(fh.readline())

except FileNotFoundError:
       print(f"Error: The file {file_name} does not exists" )

