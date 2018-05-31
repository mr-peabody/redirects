import pip
import csv
count = 0
with open('redirects.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    count += 1
    count_str = str(count)

    file = open('redirects/'+count_str+'.htm', 'w')
    file.write('url = "' + row[0] + '"\nis_hidden = 0\n==\n\n<?php\nfunction onStart(){return Redirect::to("' + row[1] + '");}\n?>\n==')
    file.close()
