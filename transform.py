#! /usr/bin/python

#George Stenos
#860892560
#stenosg
#
#
#The following script performs transformation on the word specified by the config.txt file.


from optparse import OptionParser
import re, sys, datetime, shutil, os, fileinput

dateTime = datetime.datetime.now()
dateTimeStr = str(dateTime.year) + str(dateTime.month) + str(dateTime.day) + str(dateTime.hour) + str(dateTime.minute) + str(dateTime.second)

#file not here
def pres_error(error):
	sys.stderr.write(error + "\n")
	
	sys.exit(1)


#not a reg file
def type_error(error):
	sys.stderr.write(error + "\n")
	
	sys.exit(2)


#not a reg file
def match_error(error):
	sys.stderr.write(error + "\n")
	
	sys.exit(3)


parser = OptionParser()
parser.add_option("-c", "--config", dest="config", help="Contains values", metavar="CONFIG")
parser.add_option("-t", "--target", dest="target", help="Target file for transformations", metavar="TARGET")
(options, args) = parser.parse_args()



if not options.config: 
	error = "Config file not passed in" + "\n"
	pres_error(error)

if not options.target: 
	error = "Target file not passed in" + "\n"
	pres_error(error)

if not os.path.isfile(options.config):
	error = "Config is not a reg file" + "\n"
	type_error(error)


if not os.path.isfile(options.target):
	error = "Target is not a reg file" + "\n"
	type_error(error)


for line in fileinput.FileInput(options.config, inplace=1):
	if not re.match('[A-Z]+[=][A-Z]+', line):
		error = "Config NOT IN CORRECT FORMAT" + "\n"
		match_error(error)




backupFile = options.target + dateTimeStr
shutil.copyfile(options.target, backupFile)

f = open(options.config) 
linezor = f.readlines() #whole config file in here
f.close()

f2 = open( options.target )
linezor2 = f2.readlines() #whole target file in here
f2.close()


str_map = {}


temp = ""
wordz = ""
replace = ""

#handles config file
gekas = []

#holds string that will be replaced
ninis = []


f_edit = open( options.target , 'w' )

#Set up list of the config file, splitting by =
for checker in linezor:
	gekas = checker.split( '=' )
	str_map[gekas[0]] = gekas[1]

#split all the words up, making them more easily accessible
for checker2 in linezor2:
	ninis = checker2.split( ' ' )
	wordz = ""

	for i in range( len(ninis) ):
		result = re.search( r"(\$\$.*\$\$)" , ninis[i] )
		if result:
			temp = result.group(0).strip('\$')
			if str_map.get(temp):
				replace = str_map.get(temp)
				ninis[i] = replace
		#Enumerate the new line
		wordz += ninis[i].rstrip("\n") + " "
	f_edit.write(wordz + "\n")

f_edit.close()
	



