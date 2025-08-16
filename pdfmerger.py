# To install: pip install PyPDF2

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    """Merges a list of PDF files into a single output file."""
    merger = PdfMerger()
    
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"Error: File not found at {pdf}. Skipping.")
    
    if merger.pages:
        merger.write(output_path)
        merger.close()
        print(f"Successfully merged PDFs into '{output_path}'")
    else:
        print("No valid PDF files were found to merge.")

if __name__ == "__main__":
    pdf_files_str = input("Enter the paths of the PDF files to merge, separated by spaces: ")
    pdf_files = pdf_files_str.split()
    output_file = "merged_document.pdf"
    
    merge_pdfs(pdf_files, output_file)