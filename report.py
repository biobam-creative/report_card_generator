from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

import csv

width, height = A4

pdfmetrics.registerFont(TTFont('Raleway-Bold', 'static/Raleway-Bold.ttf'))

file = 'results.csv'
data = []
first_ca = []
second_ca = []
third_ca = []
exam = []
total = []
total_ca =[]
with open(file,"r") as f:
	file = csv.reader(f)
	for row in file:
		data.append(row)
		try:
			first_ca.append(int(row[2]))
			second_ca.append(int(row[3]))
			third_ca.append(int(row[4]))
			exam.append(int(row[5]))
			total_ca.append(int(row[6]))
			total.append(int(row[7]))
		except Exception as e:
			pass
totals =['','TOTAL',sum(first_ca),sum(second_ca),sum(third_ca),sum(total_ca), sum(exam),sum(total),'']
data.append(totals)
doc = canvas.Canvas('report_card2.pdf', pagesize=A4)

doc.drawImage('freedemia_without_text-1.png', 0, height-150, width=150, height=150, mask='auto')

doc.drawImage('30_transparent.png', width/2-250, height/2-250, width=500, height=500, mask='auto')

doc.setFont('Raleway-Bold',size = 35, leading=None)
doc.drawCentredString(width/2+50 , height-60, 'Biobam Group of Schools')

doc.setFont('Raleway-Bold',size = 25, leading=None)

doc.drawCentredString(width/2+50 , height-90, 'No. 1, Afolabi Drive, Off Expressway')
doc.drawCentredString(width/2+50 , height-120, 'Washington D.C, USA')
doc.setFont('Raleway-Bold',size = 35, leading=None)
doc.drawCentredString(width/2, height-170, 'Report Card')
doc.drawCentredString(width/2, height-190, '______________________________________________________________________________________')
doc.setFont('Raleway-Bold', size=15, leading=None)
doc.drawString(30, height-230, 'Name: Afolabi Emmanuel')
doc.drawString(width/2, height - 230, 'Class: S.S.S 1')
doc.drawString(440, height -230, 'Session: 2022/2023')
#container for the 'flowable' objects
element = []

t = Table(data)

tstyle = TableStyle([
('GRID', (0,0),(-1,-1),1, colors.Color(230/255,183/255,17/255)),
('BACKGROUND',(0,0),(-1,0),colors.Color(0/255,72/255,23/255)),
('TEXTCOLOR',(0,0),(-1,0),colors.Color(230/255,183/255,17/255)),
('FONT', (0,0),(-1,-1),'Raleway-Bold', 11)])
t.setStyle(tstyle)
element.append(t)


t.wrapOn(doc, width-60, height)
t.drawOn(doc, 30, height-480)
doc.drawString(30, height-580, 'Class Teacher\'s comment: ______________________________________________________________________________')
doc.drawString(30, height-620, 'Princpal\'s comment: _______________________________________________________________________________')
doc.drawString(30, height-660, 'Class Teacher\'s signature: ____________________________________________________________________________')
doc.drawString(30, height-700, 'Principal\'s signature: _____________________________________________________________________________')
doc.showPage()
doc.save()
