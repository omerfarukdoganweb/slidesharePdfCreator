import urllib.request
from fpdf import FPDF
from bs4 import BeautifulSoup

url=input("slide url:")
response=urllib.request.urlopen(url)
data=response.read()
response.close()
liste=[]

soup=BeautifulSoup(data,"html.parser")
for i in soup.find_all("img",attrs={"class":"slide_image"}):
    liste.append(i["data-full"])
x=0

for i in liste:
    x=x+1
    image=urllib.request.urlopen(i)
    byte=image.read()
    image.close()
    f=open(str(x)+".jpg","wb")
    f.write(byte)
    f.close()
    print(x)
    
x=0
imagelist=[]
pdf = FPDF()
while x<int(len(liste)):
    x=x+1
    imagelist.append(str(x)+".jpg")

print("wait")

for image in imagelist:
    pdf.add_page("P")
    pdf.image(image,10,10,190,278)
    print(image," bitti")

print("preparing pdf")

pdf.output("file.pdf", "F")

print("ok")
