import pandas as pd
from fpdf import FPDF
import PyPDF2
from datetime import datetime
from tqdm import tqdm

start_time = datetime.now()
# print(now)
FMT = "%H:%M:%S"
# date_time = now.strftime("%m.%d.%Y, %H:%M:%S")
# year = now.strftime("%Y")
# print(f"Start Time: {date_time}")

with open (r"C:\Users\aizat\Desktop\TESTING\INPUT\ASBI-191022.txt") as file:
    total_lines = len(file.readlines())
    print(total_lines)
    file.seek(0)
    account_no = []
    account_no1 = []
    commencement_date = []
    drawdown_date = []
    monthly_inst_amt = []
    profit_due = []
    name = []
    add1 = []
    add2 = []
    add3 = []
    hno = []

    for i in file:
        line=i.strip()
        account_no.append(line[0:12])
        account_no1.append(line[1:5])
        name.append(line[22:44].strip())
        monthly_inst_amt.append(line[110:118])
        profit_due.append(line[166:171])
        commencement_date.append(line[12:22])
        drawdown_date.append(line[118:128])
        add1.append(line[248:280].strip())
        add2.append(line[288:325].strip())
        add3.append(line[328:350].strip())
        hno.append(line[208:236].strip())

    # list =[]
    # list1 = []

    # with open(r"E:\IWOC\SOURCE\TF-191022.txt") as f:
    #     for line in f:
    #         if line.startswith(r"!1!"):
    #             line = line.strip()
    #             line = line[3:]
    #             line = line[0:-2].split("\\")
    #             list.append(line)
    #             line = str(line)
    #         if line.startswith(r"!2!"):
    #             line = line.strip()
    #             line = line[3:]
    #             line = line[0:-2].split("\\")
    #             list.append(line)
    #         if '!3!' in line:
    #             list1.append(line[0:20])
    
    pdf = FPDF()
    for i in tqdm (range(0,total_lines)):
        pdf.add_page()
        pdf.image(r'C:\Users\aizat\Desktop\TESTING\IMAGES\MiB-02.jpg',30,15,50)
        pdf.set_auto_page_break(auto=False)
        pdf.set_line_width(4)
        pdf.set_draw_color(r=0, g=0, b=0)
        pdf.line(x1=5, y1=4, x2=205, y2=4)         #1st horizontal line
        pdf.line(x1=5, y1=292, x2=205, y2=292)     #2nd horizontal line 
        pdf.line(5,6,5,290)                         # 1st vertical line
        pdf.line(205,6,205,290)                     # 2nd vertical line

        pdf.set_font('Arial','',8)
        pdf.ln(1)
        pdf.cell(175)
        pdf.cell(10,50,txt = 'Sulit & Persendirian', align='R')
        pdf.set_font('Arial','I',8)
        pdf.ln(3)
        pdf.cell(175)
        pdf.cell(10,50,txt = 'Private & Confidential', align='R')
        pdf.set_font('Arial','',8)
        pdf.ln(3)
        pdf.cell(10)
        pdf.cell(10,50,txt = 'Tarikh :'  )
        pdf.cell(10)
        pdf.cell(10,50,txt = commencement_date[i])
        # pdf.cell(110)
        pdf.ln(3)
        pdf.set_font('Arial','I',8)
        pdf.cell(10)
        pdf.cell(10,50,txt = 'Date')
        pdf.cell(130)

        pdf.set_font('Arial','',8)
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,60,txt = 'Tuan/Puan,')

        pdf.set_font('Arial','I',8)
        pdf.ln(3)
        pdf.cell(10)
        pdf.cell(10,60,txt = 'Sir/Madam,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,70,txt = 'NOTIS PENGELURAN PENUH PEMBIAYAAN DAN PERMULAAN BAYARAN ANSURAN BULANAN')

        pdf.ln(3)
        pdf.cell(10)
        pdf.set_font('Arial','BI',9)
        pdf.cell(10,71,txt = 'NOTICE ON FULL DISBURSEMENT OF FACILITY AND COMMENCEMENT OF MONHLY INSTALLMENT')

        pdf.ln(1)
        pdf.set_font('Arial','B',8)
        pdf.cell(10)
        pdf.cell(10,80,txt = 'No.Akaun')
        
        pdf.ln(3)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,80,txt = 'Account No.')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,80,txt = f': {account_no[i]}')

        pdf.set_font('Arial','B',8)
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,90,txt = 'Jumlah Bayaran Ansuran')
        pdf.ln(3)
        pdf.cell(10)
        pdf.set_font('Arial','BI',)
        pdf.cell(10,90,txt = 'Monthly Installment Amount')
        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,90,txt = f': RM         {monthly_inst_amt[i]}')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,100 ,txt = 'Tarikh Ansuran Bermula')
        pdf.ln(3)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,100,txt = 'Commencement Date')

        pdf.set_font('Arial','B',8)
        pdf.cell(50)
        pdf.cell(10,100,txt = f': {drawdown_date[i]}')

        pdf.ln(1)

        pdf.set_line_width(0.2)
        pdf.line(21,93,195,93)

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',8)

        
        pdf.image(r'C:\Users\aizat\Desktop\TESTING\IMAGES\MiB-03.jpg', 20, 260 , 15)        
        
        top = pdf.y
        pdf.ln(53)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.multi_cell(176, 4, txt = f'Kami ingin memaklumkan bahawa pengeluaran penuh untuk akaun pembiayaan anda telah dibuat pada {commencement_date[i]}', align='J')
        pdf.y = top

    # date to be mentioned here 
    
        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,124,txt = f'Please be informed that the bank has fully disbursed your financing account on {commencement_date[i]}')

        
        pdf.ln(6)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,124,txt = 'Pembayaran untuk ansuran bulanan anda bermula seperti dinyatakan di atas.')
        pdf.ln(4)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,124,txt = 'Kindly effect your instalment payment effective from the above date.')
        
        top = pdf.y
        pdf.ln(70)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.multi_cell(176,1,txt = 'Penyata pembiayaan akan dihantar kepada anda sekali setahun untuk tujuan rekod. Sebagai alternatif.', align='J')
        pdf.y = top

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,198,txt = 'anda boleh menyemak maklumat terperinci di Maybank2U. Bagi akaun pembayaran melalui Arahan.')


        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,204,txt = 'Bayaran dan tarikh pembayaran adalah pada.')
        

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,210,txt = 'Kindly settle all progressive interest due before the commencement date of the instalment amount in order ')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,216,txt = 'to avoid penalty interest being imposed.')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,222,txt = 'Penyata pembiayaan akan dihantar kepada anda sekali setahun untuk tujuan rekod. Sebagai alternatif')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,228,txt = 'anda boleh menyemak maklumat terperinci di Maybank2U. Untuk akaun pembayaran melalui Arahan Tetap')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,234,txt = ' tarikh pembayaran adalah pada 1 haribulan pada setiap bulan.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,240,txt = 'The facility statement will be sent to you once a year for record purposes. Alternatively, you may check the')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,246,txt = 'details via Maybank2U. For accounts with Standing Instruction arrangement, the payment due date will be')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,252,txt = ' on the 1st day of each month.')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,258,txt = 'Sila hubungi cawangan Bank, di mana akaun kemudahan pembiayaan anda diselenggarakan, jika anda')


        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,264,txt = 'memerlukan penjelasan lanjut')


        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,270,txt = 'Do contact our branch, where your banking facility account is maintained, if you need further clarification')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,276,txt = 'Sila maklumkan kepada Pihak Bank dengan SEGERA sekiranya terdapat apa-apa perubahan alamat dan')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10) 
        pdf.cell(10,282,txt = ' nombor telefon.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,288,txt = 'Kindly notify the Bank IMMEDIATELY if there is any change of address and telephone number')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,294,txt = 'Terima kasih kerana menggunakan perkhidmatan perbankan kami')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,300,txt = 'Thank you for banking with us')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,306,txt = 'Yang benar,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,312,txt = 'bagi pihak!3! Maybank')


        pdf.ln(8)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,316,txt = 'Ini adalah cetakan komputer, tandatangan tidak diperlukan.,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,322,txt = 'This is a computer generated, no signature is required.')

        pdf.add_page()
        pdf.image(r'C:\Users\aizat\Desktop\TESTING\IMAGES\MiB-01.jpg',5, 10,200)
        pdf.ln(1)
        pdf.set_font('Arial','B',10)
        pdf.cell(40)
        pdf.cell(10,420,txt = name[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,426,txt = add1[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,432,txt = hno[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,438,txt = add2[i])

        pdf.ln(1)
        pdf.cell(40)
        pdf.cell(10,444,txt = add3[i])
    # for j in tqdm(range(100)):
    pdf.output(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\MBB001_TF.pdf')

pdf_in = open(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\MBB001_TF.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()

for pagenum in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[pagenum]
    if pagenum % 2:
        page.rotate(180)
    pdf_writer.add_page(page)

pdf_out = open(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\MBB001_TF.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()

end_time = datetime.now()
# date_time = now.strftime("%m.%d.%Y, %H:%M:%S")
# print(f"End Time: {date_time}")
print(type(start_time))
print(datetime.strftime(start_time) - datetime.strftime(end_time))