import pandas as pd
# import PyPDF2
from fpdf import FPDF
from datetime import datetime

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
        monthly_inst_amt.append(line[110:119])
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
    for i in range(0,total_lines):
        pdf.add_page()
        pdf.image(r'C:\Users\aizat\Desktop\TESTING\IMAGES\MiB-02.jpg',30,15,50)
        pdf.set_auto_page_break(auto=False)
        pdf.set_line_width(4)
        pdf.set_draw_color(r=0, g=0, b=0)
        pdf.line(x1=5, y1=4, x2=205, y2=4)         #1st horizontal line
        pdf.line(x1=5, y1=292, x2=205, y2=292)     #2nd horizontal line 
        pdf.line(5,6,5,290)                         # 1st vertical line
        pdf.line(205,6,205,290)                     # 2nd vertical line

        pdf.ln(1)
        pdf.set_font('Arial','',8)
        pdf.cell(10)
        pdf.cell(10,50,txt = 'Tarikh   :'  )
        pdf.cell(10)
        pdf.cell(10,50,txt = commencement_date[i])
        pdf.cell(110)
        pdf.cell(10,50,txt = 'Sulit & Persendirian')
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,56,txt = 'Date     :')
        pdf.cell(130)
        pdf.cell(10,56,txt = 'Private & Confidential')
        
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,70,txt = 'Tuan/Puan,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,76,txt = 'Sir/Madam,')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',9)
        pdf.cell(10,88,txt = 'NOTIS PENGELURAN PENUH PEMBIAYAAN DAN PERMULAAN BAYARAN ANSURAN BULANAN')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',9)
        pdf.cell(10,94,txt = 'NOTICE ON FULL DISBURSEMENT OF FACILITY AND COMMENCEMENT OF MONHLY INSTALLMENT')

        pdf.ln(1)
        pdf.set_font('Arial','B',8)
        pdf.cell(10)
        pdf.cell(10,104,txt = 'No.Akaun :')
        
        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,110,txt = 'Account No:')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,110,txt = account_no[i])

        
        pdf.cell(10)
        pdf.cell(10,122,txt = 'Keuntungan Progresif Yang Perlu Dibayar')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,128,txt = 'Progressive Profit Due')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,128,txt = 'RM')

        pdf.cell(10)
        pdf.cell(10,128,txt = profit_due[i])

        pdf.set_font('Arial','B',8)
        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,140,txt = 'Jumlah Bayaran Ansuran')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',)
        pdf.cell(10,146,txt = 'Monthly Installment Amoumt')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,146,txt = 'RM')

        pdf.cell(10)
        pdf.cell(10,146,txt = monthly_inst_amt[i])

        
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,158,txt = 'Tarikh Ansuran Bermula')

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,164,txt = 'Commencement Date')

        pdf.cell(50)
        pdf.cell(10,164,txt = drawdown_date[i])

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,176,txt = 'Tarikh Pengeluran Penuh')
        
        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','BI',8)
        pdf.cell(10,182,txt = 'Final Drawdown rate')

        pdf.cell(50)
        pdf.set_font('Arial','B',8)
        pdf.cell(10,182,txt = commencement_date[i])

        pdf.set_line_width(0.2)
        pdf.line(20,120,195,120)

        pdf.ln(1)
        pdf.cell(10)
        pdf.set_font('Arial','',8)

        
        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,220,txt = 'Kami ingin memaklumkan bahawa pengeluaran penuh telah dibuat untuk akaun pembiayaan anda.')
       
        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,226,txt = 'Please be informed that your facility has been fully disbursed')

        
        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,232,txt = 'Pembayaran untuk ansuran bulanan anda bermula seperti dinyatakan di atas.')
       
        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,238,txt = 'Kindly effect your instalment payment effective from the above date')
        

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,244,txt = 'Sila jelaskan sebarang faedah progresif yang perlu dibayar sebelum berkuatkuasanya ansuran bulanan.')
       
        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,252,txt = 'bagi mengelak anda daripada dikenakan penalti faedah.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,258,txt = 'Kindly settle all progressive interest due before the commencement date of the instalment amount in order ')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,264,txt = 'to avoid penalty interest being imposed.')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,270,txt = 'Penyata pembiayaan akan dihantar kepada anda sekali setahun untuk tujuan rekod. Sebagai alternatif')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,276,txt = 'anda boleh menyemak maklumat terperinci di Maybank2U. Untuk akaun pembayaran melalui Arahan Tetap')

        pdf.ln(1)
        pdf.cell(10)
        pdf.cell(10,282,txt = ' tarikh pembayaran adalah pada 1 haribulan pada setiap bulan.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,286,txt = 'The facility statement will be sent to you once a year for record purposes. Alternatively, you may check the')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,292,txt = 'details via Maybank2U. For accounts with Standing Instruction arrangement, the payment due date will be')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,298,txt = ' on the 1st day of each month.')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,304,txt = 'Sila hubungi cawangan Bank, di mana akaun kemudahan pembiayaan anda diselenggarakan, jika anda')


        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,310,txt = 'memerlukan penjelasan lanjut')


        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,316,txt = 'Do contact our branch, where your banking facility account is maintained, if you need further clarification')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,322,txt = 'Sila maklumkan kepada Pihak Bank dengan SEGERA sekiranya terdapat apa-apa perubahan alamat dan')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,328,txt = ' nombor telefon.')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,334,txt = 'Kindly notify the Bank IMMEDIATELY if there is any change of address and telephone number')

        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,338,txt = 'Terima kasih kerana menggunakan perkhidmatan perbankan kami')

        pdf.ln(1)
        pdf.set_font('Arial','I',10)
        pdf.cell(10)
        pdf.cell(10,344,txt = 'Thank you for banking with us')


        pdf.ln(4)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,350,txt = 'Yang benar,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,356,txt = 'bagi pihak!3! Maybank')


        pdf.ln(8)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,364,txt = 'Ini adalah cetakan komputer, tandatangan tidak diperlukan.,')

        pdf.ln(1)
        pdf.set_font('Arial','',10)
        pdf.cell(10)
        pdf.cell(10,370,txt = 'This is a computer generated, no signature is required.')

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

    pdf.output(r'C:\Users\aizat\Desktop\TESTING\OUTPUT\MBB001_TF.pdf')