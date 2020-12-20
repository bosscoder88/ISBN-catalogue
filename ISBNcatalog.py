from isbnlib import *
import csv
book = 0
book = int(input("How many boxes are there? "))
books = book + 1


for boxNo in range(1, books):
    print("\nWe will now go to Box", boxNo, "so please label this box correspondingly.")
    end = 0
    end = int(input("How many books are in this box? "))
    end += 1
    for bookNo in range(1, end):
        
        isbn = input("\nPlease enter a ISBN: ")


        info = meta(isbn, service='openl')
        try:
            
            # print(info)
            print("\n\nTitle:", info['Title'])
            print("Author(s):", info['Authors'])
            print("Publisher:", info['Publisher'])
            print("Year:", info['Year'])
            #print("Check out these related ISBN's:", editions(isbn, service='merge'))
        except:
            raise Exception('There has been an error. Most likely this book is not supported, and you will need to catalog it manually.')
        info["Box"] = boxNo
        rowToWrite = [info['Title'], info['Authors'], info['Publisher'], info['Year'],
                      info["Box"]]

        # print(rowToWrite) ## Bug Fixing
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rowToWrite)
print("Finished.")
