# File Objects

#f = open("test.txt", "r")
#print (f.name)# test.txt 
#print (f.mode)# r

#f.close()




#with open("test.txt", "r") as f:
    #pass

#print(f.closed)#True
#print(f.read())# ValueError: I/O operation on closed file.




#with open("test.txt", "r") as f:
    #f_contents = f.read()
    #print(f_contents)

#1)This is a text file
#2)With multiple lines of data...
#3)Third line 
#4) Fourth line
#5)Fifth line
#6)Sixth line
#7)Seventh line
#8)Eigth line
#9)Ninth line
#10)Tenth line

#with open("test.txt", "r") as f:
    #f_contents = f.readlines()
    #print(f_contents)

#['1)This is a text file\n', 
#'2)With multiple lines of data...\n', '3)Third line \n', 
#'4) Fourth line\n', '5)Fifth line\n', '6)Sixth line\n', 
#'7)Seventh line\n', '8)Eigth line\n', '9)Ninth line\n', 
#'10)Tenth line']
    

#with open("test.txt", "r") as f:
    #f_contents = f.readline()
    #print(f_contents)

#1)This is a text file


#with open("test.txt", "r") as f:
    #f_contents = f.readline()
    #print(f_contents)# 1)This is a text file

    #f_contents = f.readline()
    #print(f_contents)#2)With multiple lines of data...  






# To make it print without space in the terminal:
    
#with open("test.txt", "r") as f:
    #f_contents = f.readline()
    #print(f_contents, end='')# 1)This is a text file

    #f_contents = f.readline()
    #print(f_contents, end='')#2)With multiple lines of data...



    # To iterate in a file in order to get the amount we need of 
    #text instead of using readlines over and over
    #do the following:

#with open("test.txt", "r") as f:
    #for line in f:
        #print(line, end='')
#1)This is a text file
#2)With multiple lines of data...
#3)Third line 
#4) Fourth line
#5)Fifth line
#6)Sixth line
#7)Seventh line
#8)Eigth line
#9)Ninth line
#10)Tenth line 



# Sometimes you want more control of what you are reading from a file
        
#with open("test.txt", "r") as f:
    #f_contents = f.read(100)
    #print(f_contents)

#1)This is a text file
#2)With multiple lines of data...
#3)Third line 
#4) Fourth line
#5)Fifth line
#6)S    






# Or multipli the amount of times:

#with open("test.txt", "r") as f:
    #f_contents = f.read(100)
    #print(f_contents)

    #f_contents = f.read(100)
    #print(f_contents)

# 1)This is a text file
#2)With multiple lines of data...
#3)Third line 
#4) Fourth line
#5)Fifth line
#6)S
#ixth line
#7)Seventh line
#8)Eigth line
#9)Ninth line
#10)Tenth line




    

# If you print it for a third time, nothing happen 
#because the file is complete and the print statement will 
#just return an empty string
    
#with open("test.txt", "r") as f:
    #f_contents = f.read(100)
    #print(f_contents)

    #f_contents = f.read(100)
    #print(f_contents)

    #f_contents = f.read(100)
    #print(f_contents)




# If we don't know how big the size of the file is, we ca iterate through it
# using a loop and getting small chunks at the time.
    
#with open("test.txt", "r") as f:

    #size_to_read = (100)

    #f_contents = f.read(size_to_read)
    
    #while len(f_contents) > 0:
        #print(f_contents, end='')
        #f_contents = f.read(size_to_read)# add this line or the loop will be infinite

# 1)This is a text file
#2)With multiple lines of data...
#3)Third line 
#4) Fourth line
#5)Fifth line
#6)Sixth line
#7)Seventh line
#8)Eigth line
#9)Ninth line
#10)Tenth line





# To get a better idea let's short the size_to_read to 10 characters only 
        
# with open("test.txt", "r") as f:

#     size_to_read = (10)

#     f_contents = f.read(size_to_read)
    
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)

# 1)This is *a text fil*e
# 2)With m*ultiple li*nes of dat*a...
# 3)Thi*rd line 
# 4*) Fourth l*ine
# 5)Fift*h line
# 6)S*ixth line
# *7)Seventh *line
# 8)Eig*th line
# 9)*Ninth line*
# 10)Tenth *line*





# We can see the actual position using f.tell
        
# with open("test.txt", "r") as f:

#     size_to_read = (10)

#     f_contents = f.read(size_to_read)
#     #print(f_contents, end='*')

#     print(f.tell())#10
# It is saying that we are at the 10th position of the file
    #since we alredy read 10 characthers

    



# And we can manipulate our actual position using the seek method

# with open("test.txt", "r") as f:

#     size_to_read = (10)

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f_contents = f.read(size_to_read)
#     print(f_contents)

#1)This is a text fil
    


# What if we want the second read to start back at the beginning of the file?
# We use then the seek method:
    
# Between the 2 reads insert seek:

# with open("test.txt", "r") as f:

#     size_to_read = (10)

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents)
#1)This is 1)This is 
    

# Writting to files: If the file is open in read mode will send an error.
# We have to have the file open in write mode
    
# with open("test.txt", "r") as f:
#     f.write('Test')
#io.UnsupportedOperation: not writable


# Let,s create a new file and make it writable
# If the file does not exist it will create it, because of 'w' by convention
# But if the file exists "Be careful" it will overwrite on it 
# But if you do not want to overwrite it you can use "a" to append to it
    

# with open('test2.txt', 'w') as f: # this one will overwrite in case of an existed
   # pass  # once you run the code the file appears on the explorer          

# Now we can write to it
    
    # f.write('Test')#run the code and nothing shows on the terminal
#but click on the test2.txt on theexplorer then you will see the
# word 'Test' written 

    # f.write('Test')



# Seek workd different when writting files but work different when writting then when
#reading
    
# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('Test')

# with open('Test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')



# To copy read and write text files

# with open("test.txt", "r") as rf:
#     with open("test_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)



# To copy file images add b for binary to mode
            
# with open("fommy.jpeg", "rb") as rf:
#     with open("fommy_copy.jpeg", "wb") as wf:
#         for line in rf:
#             wf.write(line)# a copy file is created of the image

# If you try without binary sends an error:
            
# with open("fommy.jpeg", "r") as rf:
#     with open("fommy_copy.jpeg", "w") as wf:
#         for line in rf:
#             wf.write(line)#UnicodeDecodeError: 'utf-8' 
#codec can't decode byte 0xff in position 0: invalid start byte


# Or more control over yor filr with chunk sizes iterations

with open("fommy.jpeg", "rb") as rf:
    with open("fommy_copy.jpeg", "wb") as wf:
        chunk_size = 4090
        rf_chunk = rf.read(chunk_size)
        while len (rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)










 





