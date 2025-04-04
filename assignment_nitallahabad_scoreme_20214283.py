import PyPDF2
import openpyxl

def extract_tables_from_pdf(pdf_path, excel_path):
    """
    Detects and extracts tables from a PDF and stores them in an Excel sheet.

    Args:
        pdf_path (str): The path to the input PDF file.
        excel_path (str): The path to the output Excel file.
    """

    # Load PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # You might need more sophisticated logic to identify table pages
        # For simplicity, let's assume the first page contains a table
        page = reader.pages[0]
        text = page.extract_text()

    # Table Detection and Extraction (This is a simplified placeholder)
    # In a real-world scenario, you'd need robust algorithms here
    # to handle various table formats, with/without borders, etc.
    # This is the most challenging part and requires advanced techniques
    # For this example, let's assume the table is simple and space-separated

    if text:
        lines = text.split('\n')
        table_data = []
        for line in lines:
            # Simple space splitting - VERY basic
            row = line.split() 
            if row: # Ensure no empty rows are added
                table_data.append(row)

    # Excel Export
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_index, row in enumerate(table_data, start=1):
        for col_index, cell_value in enumerate(row, start=1):
            sheet.cell(row=row_index, column=col_index, value=cell_value)

    workbook.save(excel_path)

    print(f"Table extracted from '{pdf_path}' and saved to '{excel_path}'")

# --- Example Usage ---
pdf_file = "input.pdf"  # Replace with your PDF path
excel_file = "output.xlsx" # Replace with your desired Excel path
extract_tables_from_pdf(pdf_file, excel_file)