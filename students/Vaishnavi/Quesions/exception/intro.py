'''
    syntax : 
    var = open('filename','mode')

    "r" - Read
    "a" - Append
    "w" - Write
    "x" - Create
    "t" - Text
    "b" - Binary

    var.read()    
    var.readline()

    var.write('data \n')

    var.close()

    Delete : 
    1.file
        import os
        os.remove('filename')

    2.Folder
        import os
        os.rmdir('folder_name')
'''

a = open( r'D:\test.txt','r')
print(a.read())