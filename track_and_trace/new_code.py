import sys
import argparse
import csv
import os.path
from track_and_trace.forms import CodesForm, ProductForm


class GenerateNewCode():
    def read_codes(self, filename="static/codes.txt"):
        """
        Function to read unique code from file
        """
        with open(filename, "r") as f:
            contents = f.read().splitlines()
            code = contents[0]
            
        return code

    def delete_code(self, filename="static/codes.txt", used_codes_filename="static/used_codes.txt"):
        """
        Function to delete used code from list
        to create new file for used_codes registration
        """
        with open(filename, "r") as f:
            contents = f.read().splitlines()
            # remove line items from list, by line index, starts from 0
            code_to_delete = contents.delete[0]
            
        with open(used_codes_filename, "a") as f:
            f.write(code_to_delete + "\n")
            
        
    def join_product_code_data(self, name, batch, expire):
        """
        Function to join product data from input
        """
        form = ProductForm()
        product_name=form.product_name.data, 
        product_batch=form.product_batch.data, 
        expire_date=form.expire_date.data
        
        
        product = product_name + product_batch + expire_date
        return product


    def join_product_code(self, product, code):
        """"
        Function to produce `product_code` 
        from uniques code and data from input
        """
        first_line = str(code)
        product_code = product + "/" + first_line
        return product_code



    def create_product_codes_reg(self, box, new_filename="static/product_codes.txt"):
        """
        Function to create .txt and record 
        unique product codes to it.
        """
        product_code_lines = str(box)
        with open(new_filename, "a") as f:
            f.write(product_code_lines + "\n")


    def track_data_csv(self, codes, filename="static/Track_data.csv"):
        """
        Function to create .csv file and record 
        1. used unique codes from file
        2. generated unique product_codes
        3. product code group
        """

        file_exist = os.path.isfile(filename)

        with open(filename, "a", newline="") as csvfile:

            headers = ["codes"]
            writer = csv.DictWriter(csvfile, fieldnames=headers)

            if not file_exist:
                writer.writeheader()  # file doesn't exist yet, write a header

            code = '\n'.join(codes)
            writer.writerow(
                {
                    "codes": code
                }
            )


