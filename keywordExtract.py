import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import functools

##### ------------ Pre-Processing -----------------------#####

## configure stemmer
ps = PorterStemmer()

## configure stop words for programs
stop_words = stopwords.words("english")
stop_words.append(['//','\\',';','++','()','{','}','(',')',',','!','[]'])
stop_words.append(['!=','=','=='])
#print(stop_words)

## Read file from PDF 
fileRead = open('JavaDoc.pdf','rb')
pdf_reader= PyPDF2.PdfFileReader(fileRead)
num_pages = pdf_reader.getNumPages()

text = ''

# iterate over the pages of pdf and write into text doc
for page in list(range(num_pages)):
    page_obj = pdf_reader.getPage(page)
    text = text + (page_obj.extractText())

    
#tokenize words
words = word_tokenize(text)

filtered_text= [];

# remove punctuations and useless words 
for w in words:
    # stem word
    w = ps.stem(w)
    if w not in stop_words:
        if len(w) > 4:
            filtered_text.append(w)
            




###### -------------------------- Find the keywords ---------------------------######
# finds 20 most common keywords
filtered_text = nltk.FreqDist(filtered_text)
keywords = filtered_text.most_common(20)
print(filtered_text.most_common(20))



####### ------------------------- Save the keywords to txt file ----------------#######
new_text = ''.join(str(keywords))
print(new_text)

# save to text file
fileWrite = open('ExtractedKeywords.txt','w')
fileWrite.write(new_text)


