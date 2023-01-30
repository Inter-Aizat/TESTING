# from fpdf import FPDF
# import webbrowser

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'B', 16)


# print(pdf.y)
# print(pdf.x)
# top = pdf.y
# offset = pdf.x + 40
# pdf.multi_cell(0,5,'Hello World!,how are you today',1,'J')
# pdf.multi_cell(0,10,'This cell needs to beside the other',1)

# pdf.output(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\test.pdf', 'F')
# webbrowser.open_new(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\test.pdf')

from tqdm import tqdm
from time import sleep

for i in tqdm(range(10)):
    sleep(3)