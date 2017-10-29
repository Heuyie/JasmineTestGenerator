import time, math, os
from settings import *

testCases = []
with open('testcases.py') as ts:
  #read a line from the input file and separate the line into the category to include the input string and the string itself.
  for line in ts:
    listOfLine = line.strip('\n').split(',')
    category = listOfLine[0]
    #remove the first space
    if listOfLine[1][0] is ' ':
      testString = listOfLine[1][1:]
    #adding quotes to make this string in a js file.
    testString = testString.strip('\n').rstrip(' ')
    
    if category == 'undefined':
      testString = 'undefined'

    #check if the category is included in the test scope
    if category in included:
      if category in functionHeaderDict:
        fHeader = functionHeaderDict[category]
      else:
        fHeader = functionHeaderDict['all']
      
      if category in accepted:
        result = 'accept'
        expected = toEqualDict['accepted']
      else:
        result = 'reject'
        expected = toEqualDict['rejected']
      
      if category in expected:
        expected = toEqualDict[category]
      
      #adding quotes to make this string in a js file.
      category = listOfLine[0]
      
      testCase = [result, category, testString, fHeader, expected]
      testCases.append(testCase)

#create a new spec file and a dicrectory for the file if necessary
tt = str(int(math.floor(time.time())))
directory = 'spec/' + variableName
if not os.path.exists(directory):
    os.makedirs(directory)
ff = open(directory + '/' + tt + 'Spec.js', 'w+')

ff.write('describe(\'' + testClass + '\', function() {\n')
ff.write('  var ' + variableName +';\n')

if(beforeEach != ''):
  ff.write('\n  beforeEach(function() {\n    ')
  ff.write(beforeEach)
  ff.write('\n  });\n')

if(afterEach != ''):
  ff.write('\n  afterEach(function() {\n    ')
  ff.write(afterEach)
  ff.write('\n  });\n')

#write each testcase
for i in testCases:
  res = i[0]
  catgry = i[1]
  val = i[2]
  fhead = i[3]
  expct = i[4]
  
  ff.write('\n  it(\'should ' + res + ' ' + catgry + '\', function() {\n')

  if (catgry == 'number') or (catgry == 'undefined'):
    ff.write('    ' + variableName + ' = ' + str(val) + ';\n')
  else:
    ff.write('    ' + variableName + ' = ' + '\'' + str(val) + '\';\n')
  
  ff.write('    expect(' + fhead + ').toEqual(' + expct + ');\n')
  ff.write('  });\n')

ff.write('\n});')

newHtml = []
#read the existing SpecRunner.html and add a new line for the new spec file. The new file replaces the old file for this variable.
with open('SpecRunner.html', 'r') as sr:
  html = sr.readlines()
  
  for index, text in enumerate(html):
    if not (directory in text):
      newHtml.extend(text)
    nextText = html[index + 1]
    
    if(nextText == '</head>\n'):
      newHtml.extend('  <script src="' + directory + '/' + tt + 'Spec.js' + '"></script>\n')
    
    if(index == (len(html) - 2)):
      newHtml.extend(nextText)
      break

#write a new SpecRunner.html
with open('SpecRunner.html', 'w') as nsr:
  for item in newHtml:
    nsr.write(item)
