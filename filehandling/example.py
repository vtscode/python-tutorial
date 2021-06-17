import csv
# import gdal
# import osgeo

# print(osgeo)

try :
    with open('data.csv','w+')as f:
        data = csv.writer(f,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # cara nambah / write file
        data.writerow(['Javascript', 'Bjarne Stroustrup', '1985', '.js'])
        f.seek(0) # Important: return to the top of the file before reading, otherwise you'll just read an empty string
        data = csv.reader(f)
        for row in f:
            print(row.split(","))
except:
    print("ada error")
# try :
#     with open('data.csv','r')as f:
#         data = csv.reader(f)
#         for row in f:
#             print(row[0])
# except:
#     print("ada error")



#1 Operasi read
#membuka file data.txt dengan mode read
# data = open('data.txt',mode='r')
#mencetak isi data.txt
# print(data.read())

# # menambah data
# data = open('data.txt','a')

# #menambah kalimat
# data.write("Jago python handling dalam sehari\n")



# data.close() 


# #membaca file databaru.txt dengan mode write
# file = open('databaru.txt','w') 

# #menulis kalimat di file databaru.txt
# file.write("Belajar nulis di file\n") 
# file.write("nulis di file dengan mode write\n") 

# file.close() #mengakhiri program file kita


# import os

# os.remove("databaru.txt")


# with open("data.txt", "a") as file:
#     file.write("gunakan with untuk menutup file secara otomatis")

# try:
#     with open("dataku.txt", "r+") as file:
#         print(file.read(1))
# except:
#     print("ada ERROR : tidak ada data")

# try:
#     with open("dataku.txt", "w") as file:
#         file.write("tambh data")
# except:
#     print("ada ERROR : tidak ada data")