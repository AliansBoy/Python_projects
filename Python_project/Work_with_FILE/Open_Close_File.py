work_file = open("File.txt", 'r')
file_content = work_file.read()

work_file.close()

print(file_content)

user_name = input("Please input the name ")
work_file_write = open("File.txt", 'w')
file_content_write = work_file_write.write(user_name)

work_file_write.close()
