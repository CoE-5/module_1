import sys
import csv
import operator

def sucph_to_dict():
  sucph = {
    'region' : [],
    'suc' : [],
    'enrolment_2010-2011' : [],
    'enrolment_2011-2012' : [],
    'enrolment_2012-2013' : [],
    'graduates_2009-2010' : [],
    'graduates_2010-2011' : [],
    'graduates_2011-2012' : [],
  }

  # ctr = 0
  with open('suc_ph.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    for row in reader:
      sucph['region'].append(row[0])
      sucph['suc'].append(row[1])
      sucph['enrolment_2010-2011'].append(row[2])
      sucph['enrolment_2011-2012'].append(row[2])
      sucph['enrolment_2012-2013'].append(row[4])
      sucph['graduates_2009-2010'].append(row[5])
      sucph['graduates_2010-2011'].append(row[6])
      sucph['graduates_2011-2012'].append(row[7])

  return sucph

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  # print "1. The region with the most SUC is National Capital Region (NCR)"
  # sucph = sucph_to_dict()
  # reg = {}
  # for region in sucph['region']:
  #   if region not in reg:
  #     reg[region] = 1
  #   else:
  #     reg[region] += 1

  # for key in sorted(reg, key = reg.get, reverse = True):
  #   print "1. The region with the most SUC is " + key
  #   break
  F = open('suc_ph.csv', 'r')
  suc = {}
  for index, line in enumerate(F):
      row = line.split(',')
      if row[0] in suc:
          suc[row[0]] += 1
      else:
          suc[row[0]] = 1
  F.close()
  suc_list = sorted(suc.items(), key=operator.itemgetter(1), reverse=True)
  print '1. The region with the most SUC is ' + suc_list[0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  # print "2. The region with the most SUC enrollees is CALABARZON (R-IVA)"
  sucph = sucph_to_dict()
  reg = {}
  reg_enr = {}
  enr = []
  i = 0

  if school_year == '2010-2011':
    school_year = 'enrolment_2010-2011'
  elif school_year == '2011-2012':
    school_year = 'enrolment_2011-2012'
  elif school_year == '2012-2013':
    school_year = 'enrolment_2012-2013'

  for region in sucph['region']:
    if region not in reg:
      reg[region] = 1
      if sucph[school_year][i].isdigit():
        reg_enr[region] = int(sucph[school_year][i])
    else:
      reg[region] += 1
      if sucph[school_year][i].isdigit():
        reg_enr[region] += int(sucph[school_year][i])
    i += 1

  for key in sorted(reg_enr, key = reg_enr.get, reverse = True):
    print "2. The region with the most SUC enrollees is " + key
    break

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  # print "3. The region with the most SUC graduates is Cagayan Valley (R-II)"
  sucph = sucph_to_dict()
  reg = {}
  reg_grad = {}
  enr = []
  i = 0

  if school_year == '2009-2010':
    school_year = 'graduates_2009-2010'
  elif school_year == '2010-2011':
    school_year = 'graduates_2010-2011'
  elif school_year == '2011-2012':
    school_year = 'graduates_2011-2012'

  for region in sucph['region']:
    if region not in reg:
      reg[region] = 1
      if sucph[school_year][i].isdigit():
        reg_grad[region] = int(sucph[school_year][i])
      else:
        reg_grad[region] = 0
    else:
      reg[region] += 1
      if sucph[school_year][i].isdigit():
        reg_grad[region] += int(sucph[school_year][i])
    i += 1

  for key in sorted(reg_grad, key = reg_grad.get, reverse = True):
    print "3. The region with the most SUC graduates is " + key
    break

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  # print "4. Top 3 cheapest SUC for BS level in school year 2010-2011"
  # print "  1. Technological University of the Philippines"
  # print "  2. Marikina Polytechnic College"
  # print "  3. Apayao State College"

  if level.upper() == 'BS' and school_year == '2010-2011':
    column = 2
  elif level.upper() == 'MS' and school_year == '2010-2011':
    column = 3
  elif level.upper() == 'PHD' and school_year == '2010-2011':
    column = 4
  elif level.upper() == 'BS' and school_year == '2011-2012':
    column = 5
  elif level.upper() == 'MS' and school_year == '2011-2012':
    column = 6
  elif level.upper() == 'PHD' and school_year == '2011-2012':
    column = 7
  elif level.upper() == 'BS' and school_year == '2012-2013':
    column = 8
  elif level.upper() == 'MS' and school_year == '2012-2013':
    column = 9
  elif level.upper() == 'PHD' and school_year == '2012-2013':
    column = 10

  school = []

  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  tf = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[column].isdigit():
        tf[row[1]] = float(row[column])
  f.close()
  tf_list = sorted(tf.items(), key = operator.itemgetter(1))

  for x in range(20):
    school.append(tf_list[x][0])

  print "4. Top 3 cheapest SUC for %s level in school year %s" %(level, school_year)
  print "  1. " + school[0]
  print "  2. " + school[1]
  print "  3. " + school[2]
    

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  # print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  # print "  1. Technological University of the Philippines"
  # print "  2. Marikina Polytechnic College"
  # print "  3. Apayao State College"

  if level.upper() == 'BS' and school_year == '2010-2011':
    column = 2
  elif level.upper() == 'MS' and school_year == '2010-2011':
    column = 3
  elif level.upper() == 'PHD' and school_year == '2010-2011':
    column = 4
  elif level.upper() == 'BS' and school_year == '2011-2012':
    column = 5
  elif level.upper() == 'MS' and school_year == '2011-2012':
    column = 6
  elif level.upper() == 'PHD' and school_year == '2011-2012':
    column = 7
  elif level.upper() == 'BS' and school_year == '2012-2013':
    column = 8
  elif level.upper() == 'MS' and school_year == '2012-2013':
    column = 9
  elif level.upper() == 'PHD' and school_year == '2012-2013':
    column = 10

  school = []

  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  tf = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[column].isdigit():
        tf[row[1]] = float(row[column])
  f.close()
  tf_list = sorted(tf.items(), key = operator.itemgetter(1), reverse=True)

  for x in range(20):
    school.append(tf_list[x][0])

  print "5. Top 3 expensive SUC for %s level in school year %s" %(level, school_year)
  print "  1. " + school[0]
  print "  2. " + school[1]
  print "  3. " + school[2]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  # print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  # print "   Technological University of the Philippines, Apayao State College, Marikina Polytechnic College, Surigao State College of Technolgoy"
  school = []
  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  for index, line in enumerate (f):
    row = line.split(',')
    # if row[2] != 'first_sem_2010-2011_bs_ab' and row[5] != 'first_sem_2011-2012_bs_ab' and row[8] != 'first_sem_2012-2013_bs_ab' and row[2] != 'first_sem_2012-2013_ms_ma' and row[2] != 'first_sem_2012_-2013_phd' and row[2].strip() != '-' and row[2] != 'free tuition fee' and row[2] != 'nds' and row[2] != 'nd' and row[5].strip() != '-' and row[5] != 'free tuition fee' and row[5] != 'nds' and row[5] != 'nd' and row[8].strip() != '-' and row[8] != 'free tuition fee' and row[8] != 'nds' and row[8] != 'nd':
    #   if row[2] < row[5] or row[2] < row[8]:
    #     school.append(row[1])
    if row[2].isdigit():
      if row[2] < row[5] or row[2] < row[8] or row[5] < row[8]:
        school.append(row[1])
  f.close()
  
  sch = ', '.join(school)
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013\n" + "   " + sch

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  # print "7. The discipline which has the highest passing rate is Accountancy"

  if school_year == '2010':
    school_year = 3
  if school_year == '2011':
    school_year = 4
  if school_year == '2012':
    school_year = 5

  discipline = {}
  f = open('performancesucprclicensureexam20102012.csv', 'r')
  for index, line in enumerate (f):
    row = line.split(',')
    if row[2] != 'discipline':
      if row[school_year].isdigit() and row[2] != 'Total':
        discipline[row[2]] = float(row[school_year])
  f.close()

  discipline_sorted = sorted(discipline, key = discipline.get, reverse = True)
  print "7. The discipline which has the highest passing rate is " + discipline_sorted[0]

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  # print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  # print "  1. Technological University of the Philippines"
  # print "  2. Marikina Polytechnic College"
  # print "  3. Apayao State College"

  if school_year == '2010':
    year = 3
  if school_year == '2011':
    year = 4
  if school_year == '2012':
    year = 5

  school = {}
  f = open('performancesucprclicensureexam20102012.csv', 'r')
  for index, line in enumerate (f):
    row = line.split(',')
    if row[2] == discipline:
      if row[year].isdigit() and row[2] != 'Total':
        school[row[1]] = float(row[year])
  f.close()

  school_sorted = sorted(school, key = school.get, reverse = True)
  print "8. Top 3  SUC with highest passing rate in %s for school year %s" %(discipline, school_year)
  print "  1. " + school_sorted[0]
  print "  2. " + school_sorted[1]
  print "  3. " + school_sorted[2]

def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()