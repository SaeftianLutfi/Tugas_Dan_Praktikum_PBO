# Open a File

teks = "Saya Mahasiswa Universitas Muhammadiyah Cirebon"

# Write the File
with open("test.txt", "a") as file1:
    file1.write(teks)
    
# Close the File
file1.close()

with open("test.txt", "r") as file2:
    read_content = file2.read()
    print(read_content)
    
# Close the file
file2.close()
