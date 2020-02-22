# https://flothesof.github.io/preparing-hashcode-2018.html

import numpy
import os
# from multiprocessing import Queue
from queue import PriorityQueue


class Solution:
    def read_input_file(self, filename):
        book_scanning = {}
        lines = open(filename).readlines()
        book_scanning['number_of_books'], book_scanning['Library'], book_scanning['Days'] = [int(val) for val in lines[0].split()]
        book_scanning['books'] = numpy.array([int(val) for val in lines[1].split()])

        book_scanning['library_books_number'], book_scanning['library_registration_time'], book_scanning['library_number_of_shipping'], book_scanning['library_books'] = [], [], [], []
        for i in range(0, book_scanning['Library']):
            book_scanning['library_books_number'].append(0), book_scanning['library_registration_time'].append(0), book_scanning['library_number_of_shipping'].append(0), book_scanning['library_books'].append([])
            
            book_scanning['library_books_number'][i], book_scanning['library_registration_time'][i], book_scanning['library_number_of_shipping'][i] = [int(val) for val in lines[2 + 2*i].split()]
            
            book_scanning['library_books'][i] = numpy.array([int(val) for val in lines[2 + 2*i + 1].split()])

        return book_scanning

    def get_library_registration(self, book_scanning):
        library_registration_time = book_scanning['library_registration_time']
        return numpy.array(library_registration_time).argsort()

    def write_output(self, file_name, library_scanned_book):        
        base = os.path.splitext(os.path.basename(file_name))[0]        
        f = open(base + ".out", "w")

        f.write( str(len(library_scanned_book)) + "\n")
        for library_index, library_books in library_scanned_book.items():
            f.write( str(library_index) + '\t' + str(len(library_books)) + "\n")
            f.write( '\t'.join([str(cell) for cell in library_books]) + "\n" )

obj = Solution()
for file_name in ["f_libraries_of_the_world.txt"]: 
    # "a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt"
    print("\n#=====Running for: ", file_name, "=====#")

    book_scanning = obj.read_input_file(file_name)
    # print(book_scanning)
    library_ids = obj.get_library_registration(book_scanning)
    # for i in library_ids:
    #     print(i, book_scanning['library_registration_time'][i])
    
    days, books_priority_queue, library_id = book_scanning['Days'], {}, 0    
    library_scanned_book, set_scanned_book = {}, set() 
    while(days > 0):
        print("\n#=====For day: ", book_scanning['Days'] - days, "=====#")
        if library_id < len(library_ids):
            library_index = library_ids[library_id]
            if book_scanning['library_registration_time'][library_index] == 0:
                book_priority_queue = PriorityQueue()
                for library_book in book_scanning['library_books'][library_index]:
                    # print(-book_scanning['books'][library_book], library_book )
                    book_priority_queue.put( ( (-1 * int(book_scanning['books'][library_book]) ), library_book ) )
                
                books_priority_queue[library_index] = book_priority_queue 
                library_id += 1
        
        if library_id < len(library_ids):
            library_index = library_ids[library_id]
            book_scanning['library_registration_time'][library_index] -= 1
        
        for library_index, library_books_priority_queue in books_priority_queue.items():
            # print(library_index, library_books_priority_queue)

            library_number_of_shipping = book_scanning['library_number_of_shipping'][library_index]
            while(library_number_of_shipping > 0 and library_books_priority_queue.qsize() > 0):
                library_book = library_books_priority_queue.get()

                print(library_book[0], library_book[1])
                library_book = library_book[1]
                
                if library_book not in set_scanned_book:
                    set_scanned_book.add(library_book)

                    if library_index not in library_scanned_book.keys():
                        library_scanned_book[library_index] = []
                    library_scanned_book[library_index].append(library_book)

                    library_number_of_shipping -= 1

            books_priority_queue[library_index] = library_books_priority_queue

        days -= 1
    
    print(library_scanned_book)
    obj.write_output(file_name, library_scanned_book)

    # if M * N <= 100000000:
    #     obj.solve_dp(file_name, M, N, pizza)
    # else:
    #     obj.solve_greedy(file_name, M, N, pizza)

    