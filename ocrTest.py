import cv2
import pytesseract
import datefinder

pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('img.jpg')


text = pytesseract.image_to_string(image,lang='spa')

print('Texto: ',text)

print('posicion: ',text.find('FECHA DE NA'))

y= text.find('FECHA DE NA') +12
cadena=text[y:(y+20)]
print('fech: ',cadena)


def month_string_to_number(string):
    m = {
        'ene': 1,
        'feb': 2,
        'mar': 3,
        'abr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'ago':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dic':12
        }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        return 0

matches = list(datefinder.find_dates(cadena))

if len(matches) > 0:
    # date returned will be a datetime.datetime object. here we are only using the first match.
    date = matches[0]
    print (date)
else:
    for indice in range(len(cadena)):
        caracter = cadena[indice]
        print(caracter)
        palabra=""
        if caracter != '':
            palabra=palabra+caracter            
            print('palabra',palabra)
        else:
            numero=0
            numero=month_string_to_number(palabra)
            palabra=""
            if numero>0:
                cadena.replace(palabra,numero)
print ('fecha cambio',cadena)

cv2.waitKey(0)
cv2.destroyAllWindows()





