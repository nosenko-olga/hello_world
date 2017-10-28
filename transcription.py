import os,re

def ReadFromFile(FileName):
    f=open(FileName,"r")
    s=f.read()
    f.close()
    return s

def JMake(s):
    l=[["е","йэ"],
       ["ё", "йо"],
       ["ю", "йу"],
       ["я", "йа"]]
    for m in l:
        s=re.sub(r"([ аеёоэюяуиыъь])"+m[0],r"\g<1>"+m[1],s)
    return s

def Eeaf(s):
    l=[["б","п"],
       ["в","ф"],
       ["г","к"],
       ["д","т"],
       ["ж","ш"],
       ["з","с"],
       ["р","r"]]
    for m in l:
        s=re.sub(m[0]+r"([ьъ]?[ пктшсщчцф])",m[1]+r"\g<1>",s)
    return s
    

def Sonar(s):
    l=[["п","б"],
       ["ф","в"],
       ["к","г"],
       ["т","д"],
       ["ш","ж"],
       ["с","з"],
       ["ч","j"],
       ["ц",'z'],
       ["щ","s"],
       ["х","g"]]
    for m in l:
        s=re.sub(m[0]+r"([ьъ]?[ ]?[бвгджз])",m[1]+r"\g<1>",s)
    return s


def Soft(s):
    l=[["п","П"],
       ["ф","Ф"],
       ["к","К"],
       ["т","Т"],
       ["с","С"],
       ["х","Х"],
       ["п","П"],
       ["б","Б"],
       ["в","В"],
       ["г","Г"],
       ["д","Д"],
       ["з","З"],
       ["р","Р"],
       ["g",'G'],
       ["н","Н"],
       ["м","М"],
       ["л","Л"]]        
    for m in l:
        s=re.sub(m[0]+r"([еёяюи])",m[1]+r"\g<1>",s)
        s=re.sub(m[0]+r"(ь)",m[1],s)
    return s


def Util01(s):
    s=re.sub(r"ч",r"Ч",s)
    s=re.sub(r"щ",r"Щ",s)    
    s=re.sub(r"j",r"J",s)
    s=re.sub(r"s",r"S",s)    
    s=re.sub(r"[ьъ]",r"",s)
    return s

def Util02(s):
    l=[["и","ы"],
       ["e","э"],
       ["ю","у"],
       ["я","а"],
       ["ё","о"]]
    for m in l:
        s=re.sub(r"([zцшж])"+m[0],r"\g<1>"+m[1],s)
    return s
    
def Util03(s):
    l=[["ы","и"],
       ["э","e"],
       ["у","ю"],
       ["а","я"],
       ["о","ё"]]
    for m in l:
        s=re.sub(r"([ЧЩJS])"+m[0],r"\g<1>"+m[1],s)
    return s

def Util04(s):
    l=[["е","э"],
       ["ё","о"],
       ["ю","у"],
       ["я","а"]]
    for m in l:
        s=re.sub(m[0],m[1],s)
    return s



def Trans(s):
    s=" "+s+" "
    s=re.sub(r'[.,;:-?!]|["]','',s)
    s=Util04(Util03(Util02(Util01(Soft(Sonar(Eeaf(JMake(s.lower()))))))))
    return s.strip()

s=input("s = ")
print(Trans(s))
