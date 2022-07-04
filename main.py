#20i-0889
#19i-1777
#19i-1789
#20i-1865

import requests
import nltk

from bs4 import BeautifulSoup


link1 = requests.get('https://rni.nust.edu.pk/research-and-innovation/')
html1 = link1.content
nust1 = BeautifulSoup(html1, 'html.parser')
paras1 = nust1.get_text()
f = open("nust.txt", "w")
f.write(paras1)


link2 = requests.get('https://rni.nust.edu.pk')
html2 = link2.content
nust2 = BeautifulSoup(html2, 'html.parser')
paras2 = nust2.get_text()
f.write(paras2)

link3 = requests.get('https://hr.nust.edu.pk/Trainings.aspx')
html3 = link3.content
nust3 = BeautifulSoup(html3, 'html.parser')
paras3 = nust3.get_text()
f.write(paras3)


link4 = requests.get('https://hr.nust.edu.pk')
html4 = link4.content
nust4 = BeautifulSoup(html4, 'html.parser')
paras4 = nust4.get_text()
f.write(paras4)

link5 = requests.get('https://hr.nust.edu.pk/AboutHR.aspx')
html5 = link5.content
nust5 = BeautifulSoup(html5, 'html.parser')
paras5 = nust5.get_text()
f.write(paras5)
f.close()








#LUMS
link1 = requests.get('https://lums.edu.pk/alumni-stories')
html1 = link1.content
nust1 = BeautifulSoup(html1, 'html.parser')
paras1 = nust1.get_text()
z = open("Lums.txt", "w")
z.write(paras1)


link2 = requests.get('https://lums.edu.pk/student-noticeboard')
html2 = link2.content
nust2 = BeautifulSoup(html2, 'html.parser')
paras2 = nust2.get_text()
z.write(paras2)

link3 = requests.get('https://lums.edu.pk/news/baradari-cafe-lums-alum-mr-luqman-ali-afzal-inaugurated-campus')
html3 = link3.content
nust3 = BeautifulSoup(html3, 'html.parser')
paras3 = nust3.get_text()
z.write(paras3)


link4 = requests.get('https://lums.edu.pk/news/bringing-blockchain-technology-forefront-lums-leverage-stacks-grant-build-novel-academic')
html4 = link4.content
nust4 = BeautifulSoup(html4, 'html.parser')
paras4 = nust4.get_text()
z.write(paras4)

link5 = requests.get('https://lums.edu.pk/news/lums-vice-chancellor-addresses-35th-pakistan-society-development-economists-annual-conference')
html5 = link5.content
nust5 = BeautifulSoup(html5, 'html.parser')
paras5 = nust5.get_text()
z.write(paras5)

z.close()



#FAST
link1 = requests.get('http://nu.edu.pk/Program/BS(AI)')
html1 = link1.content
nust1 = BeautifulSoup(html1, 'html.parser')
paras1 = nust1.get_text()
s = open("Fast.txt", "w")
s.write(paras1)


link2 = requests.get('http://nu.edu.pk/Admissions/HowToApply')
html2 = link2.content
nust2 = BeautifulSoup(html2, 'html.parser')
paras2 = nust2.get_text()
s.write(paras2)

link3 = requests.get('http://nu.edu.pk/Student/Conduct')
html3 = link3.content
nust3 = BeautifulSoup(html3, 'html.parser')
paras3 = nust3.get_text()
s.write(paras3)


link4 = requests.get('http://nu.edu.pk/University/History')
html4 = link4.content
nust4 = BeautifulSoup(html4, 'html.parser')
paras4 = nust4.get_text()
s.write(paras4)

link5 = requests.get('http://nu.edu.pk/Student/Grading')
html5 = link5.content
nust5 = BeautifulSoup(html5, 'html.parser')
paras5 = nust5.get_text()
s.write(paras5)

s.close()
#Nust
f = open("nust.txt", "rt")
nust=open("nust dat.txt","w")

for line in f:
   word=nltk.word_tokenize(line)
   l=str(nltk.pos_tag(word))
   nust.write(l)
   nust.write("\n")

nust.close()
f.close()

nustn=open("nust noun.txt","w")
File = open("nust dat.txt")
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = [] 
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
nustn.write(str(nouns))

nustn.close()

fhand = open("nust noun.txt")
counts = dict()

nustf=open("nust frequency.txt","w")

for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
nustf.write(str(counts))

nustf.close()





#Lums
f = open("Lums.txt", "rt")
lk=open("lums dat.txt","w")

for line in f:
   word=nltk.word_tokenize(line)
   l=str(nltk.pos_tag(word))
   lk.write(l)
   lk.write("\n")

lk.close()
f.close()

n=open("lums noun.txt","w")
File = open("lums dat.txt")
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = [] 
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
n.write(str(nouns))

n.close()

fhand = open("lums noun.txt")
counts = dict()

fre=open("lums frequency.txt","w")

for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
fre.write(str(counts))

fre.close()








#FAST
f = open("Fast.txt", "rt")
lk=open("fast dat.txt","w")

for line in f:
   word=nltk.word_tokenize(line)
   l=str(nltk.pos_tag(word))
   lk.write(l)
   lk.write("\n")

lk.close()
f.close()

n=open("fast noun.txt","w")
File = open("fast dat.txt")
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = [] 
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
n.write(str(nouns))

n.close()

fhand = open("fast noun.txt")
counts = dict()

fre=open("fast frequency.txt","w")

for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
fre.write(str(counts))

fre.close()