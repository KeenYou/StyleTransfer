import csv
import random

HipHopLyrics = [];
with open('lyrics.csv') as f:
    rows = csv.reader(f);
    for row in rows:
        if row[4] == 'Hip-Hop' and row[5] is not None:
               HipHopLyrics.append(row[5])

data = []

for i in range(24850):
    data.append(0)

trainData = open('lyrics.train.0', 'w');
devData = open('lyrics.dev.0', 'w');
testData = open('lyrics.test.0', 'w');

tempFile = open('temp.txt', 'w');

def generateValidRandomNum():
    valid = 0
    while(valid == 0):
        num = random.randint(0, 24850)
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
while(i < 19880):
    randomIndex = generateValidRandomNum();
    tempFile.write(HipHopLyrics[randomIndex]);
    writeTrainOutput();
    i += 1;

while(i < 2485):
    randomIndex = generateValidRandomNum();
    tempFile.write(HipHopLyrics[randomIndex]);
    writeDevOutput();
    i += 1;

while(i < 2485):
    randomIndex = generateValidRandomNum();
    tempFile.write(HipHopLyrics[randomIndex]);
    writeTestOutput();

trainData.close();
devData.close();
testData.close();
