# open() function used to open a file.. 1st parameter is the name of the file and the second parameter will be the
# mode of the file.. there are different mode
# r ------ read only
# w ------ write only
# a ------ only append data
# r+ ----- read and write data
employee_file = open("file.txt", "a")
# if we use w ---- mode here it will overwrite the file
employee_file.write("Raza - Web Developer")
# we should close file here
employee_file.close()
