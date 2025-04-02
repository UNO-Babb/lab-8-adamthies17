#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    student_id = makeID(data[0], data[1], data[3], data[6], data[5])
    output = data[1] + "," + data[0] + "," + student_id + "\n"
    outFile.write(output)
    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum, major, year):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  major = major.upper()


  
  if year == "Freshman":
    year = "FR"
  elif year == "Sophomore":
    year = "SO"
  elif year == "Junior":
    year = "JR"
  elif year == "Senior":
    year = "SR"

  id = first[0] + last + idNum[idLen - 3: ] + major[0:3] + "-" + year
  
  #print(id)
  return id
   



if __name__ == '__main__':
  main()
