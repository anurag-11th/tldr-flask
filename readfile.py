#import PyPDF2
import docx2txt
import fleep
from tika import parser

accepted_files = ['docx', 'pdf', 'odt', 'rtf']

def getFileType(path):

	with open(path, "rb") as file:
		info = fleep.get(file.read(128))

	for ext in info.extension:
		if ext in accepted_files:
			return ext

def getText(path):

	extension = getFileType(path)
	#print(extension)

	if extension == "pdf":
		parsed = parser.from_file(path)
		return parsed["content"]

	elif path.endswith(".txt"):
		text = open(path, "r").read()
		return text

	elif extension == "docx":
		text = docx2txt.process(path)
		return text

	else:
		return -1

"""if __name__ == '__main__':
	print(getText('samples/st.docx'))"""


