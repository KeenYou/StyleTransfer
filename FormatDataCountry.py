import csv
import random

CountryLyrics = [];
with open('lyrics.csv') as f:
    rows = csv.reader(f);
    for row in rows:
        if row[4] == 'Country' and row[5] is not None:
               CountryLyrics.append(row[5])

data = []

for i in range(14387):
    data.append(0)

trainData = open('lyrics.train.1', 'w');
devData = open('lyrics.dev.1', 'w');
testData = open('lyrics.test.1', 'w');

tempFile = open('temp.txt', 'w');

def generateValidRandomNum():
    valid = 0
    while(valid == 0):
        num = random.randint(0, 14387)
	if(data[num] == 0):
	    valid = 1
	    return num;

def writeTrainOutput():
    with open('temp.txt', 'r') as i:
        curr = 0;
	prev = 0;
	while True:
	    c = i.read(1)
	    curr = 0;
	    if not c:
	        break;
	    elif((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '\''):
	        trainData.write(c);
	    elif(c == ','):
	        trainData.write(' ' + c + ' ')
		curr = 1;
	    elif(c == '.' or c == '!' or c == '?'):
	        trainData.write(' ' + c + '\n')
		curr = 1
	    elif(c == ' ' and (prev == 0)):
	        trainData.write(' ')
	    prev = curr;
    i.close();


def writeDevOutput():
    with open('temp.txt', 'r') as i:
        curr = 0;
	prev = 0;
	while True:
	    c = i.read(1)
	    curr = 0;
	    if not c:
	        break;
	    elif((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '\''):
	        devData.write(c);
	    elif(c == ','):
	        devData.write(' ' + c + ' ')
		curr = 1;
	    elif(c == '.' or c == '!' or c == '?'):
	        devData.write(' ' + c + '\n')
		curr = 1
	    elif(c == ' ' and (prev == 0)):
	        devData.write(' ')
	    prev = curr;
    i.close();


def writeTestOutput():
    with open('temp.txt', 'r') as i:
        curr = 0;
	prev = 0;
	while True:
	    c = i.read(1)
	    curr = 0;
	    if not c:
	        break;
	    elif((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '\''):
	        testData.write(c);
	    elif(c == ','):
	        testData.write(' ' + c + ' ')
		curr = 1;
	    elif(c == '.' or c == '!' or c == '?'):
	        testData.write(' ' + c + '\n')
		curr = 1
	    elif(c == ' ' and (prev == 0)):
	        testData.write(' ')
	    prev = curr;
    i.close();

i = 0;
while(i < 11510):
    randomIndex = generateValidRandomNum();
    tempFile.write(CountryLyrics[randomIndex]);
    writeTrainOutput();
    i += 1;

while(i < 1438):
    randomIndex = generateValidRandomNum();
    tempFile.write(CountryLyrics[randomIndex]);
    writeDevOutput();
    i += 1;

while(i < 1439):
    randomIndex = generateValidRandomNum();
    tempFile.write(CountryLyrics[randomIndex]);
    writeTestOutput();

trainData.close();
devData.close();
testData.close();
