from fpdf import FPDF
from tkinter import *
from tkinter import filedialog

def openFile():
    names = []asdasda
    title = []
    address_1 = []
    address_2 = []
    address_3 = []
    city = []
    state = []
    filepath = filedialog.askopenfilename()
    # file = open(filepath,'r')
    with open(filepath ,'r') as f:
        # print(f.read())
        total_client = 0
        for count, line in enumerate(f):
            if "CH000" in line [0:5]:
                total_client+=1
                names.append(line[40:88])
                title.append(line[88:128])
                address_1.append(line[128:168])
                address_2.append(line[168:208])
                address_3.append(line[208:248])
                city.append(line[288:313])
                state.append(line[313:338])
        f.close()
    for i in range(0,total_client):
        customer_name = names[i].strip()
        customer_title = title[i].strip()
        customer_address_1 = address_1[i].strip()
        customer_address_2 = address_2[i].strip()
        customer_address_3 = address_3[i].strip()
        customer_city= city[i].strip()
        customer_state = state[i].strip()
        print(customer_name)
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 8)
        pdf.ln(1)
        # pdf.cell(80)
        pdf.cell(7,30,customer_name)
        pdf.ln(3)
        pdf.cell(7,30,customer_title)
        pdf.ln(5)
        pdf.cell(7,30,customer_address_1)
        pdf.ln(3)
        pdf.cell(7,30,customer_address_2)
        pdf.ln(3)
        pdf.cell(7,30,customer_address_3)
        pdf.ln(3)
        pdf.cell(7,30,customer_city)
        pdf.ln(3)
        pdf.cell(7,30,customer_state)

        pdf.output(fr'OUTPUT\{customer_name}.pdf', 'F')

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()

# names = []
# title = []
# address_1 = []
# address_2 = []
# address_3 = []
# city = []
# state = []
# with open(r"C:\Users\aizat\Desktop\TESTING\INPUT\BKR_C18.txt" ,'r') as f:
#     total_client = 0
#     for count, line in enumerate(f):
#         if "CH000" in line [0:5]:
#             total_client+=1
#             names.append(line[40:88])
#             title.append(line[88:128])
#             address_1.append(line[128:168])
#             address_2.append(line[168:208])
#             address_3.append(line[208:248])
#             city.append(line[288:313])
#             state.append(line[313:338])

# print(address_1)

# for i in range(0,total_client):
#     customer_name = names[i].strip()
#     customer_title = title[i].strip()
#     customer_address_1 = address_1[i].strip()
#     customer_address_2 = address_2[i].strip()
#     customer_address_3 = address_3[i].strip()
#     customer_city= city[i].strip()
#     customer_state = state[i].strip()
#     print(customer_name)
#     pdf=FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', '', 8)
#     pdf.ln(1)
#     # pdf.cell(80)
#     pdf.cell(7,30,customer_name)
#     pdf.ln(3)
#     pdf.cell(7,30,customer_title)
#     pdf.ln(5)
#     pdf.cell(7,30,customer_address_1)
#     pdf.ln(3)
#     pdf.cell(7,30,customer_address_2)
#     pdf.ln(3)
#     pdf.cell(7,30,customer_address_3)
#     pdf.ln(3)
#     pdf.cell(7,30,customer_city)
#     pdf.ln(3)
#     pdf.cell(7,30,customer_state)

#     pdf.output(fr'OUTPUT\{customer_name}.pdf', 'F')