# # write a program that reads 
# # the first line of a pdf file

# # import PyPDF2

# def read_first_line(pdf_file_path):
#     try:
#         with open(pdf_file_path, 'rb') as pdf_file:
#             # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
#             # Check if the PDF has any pages
#             # if pdf_reader.numPages == 0:
#                 return "The PDF is empty."

#             # Read the first page
#             first_page = pdf_reader.getPage(0)
            
#             # Extract text from the first page
#             first_page_text = first_page.extractText()
            
#             # Split the text into lines and return the first line
#             first_line = first_page_text.strip().split('\n')[0]
            
#             return first_line
#     except FileNotFoundError:
#         return "File not found."
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     pdf_file_path = "example.pdf"  # Replace with the path to your PDF file
#     first_line = read_first_line(pdf_file_path)
#     print(f"The first line of the PDF is:\n{first_line}")





