import survey
import thinkstats
import math
import Pmf
import matplotlib.pyplot as pyplot

LIVE_BIRTH_OUTCOME = 1

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

def countLiveBirths(records):
	live_birth_count = 0
	for record in records:
		if record.outcome == LIVE_BIRTH_OUTCOME:
			live_birth_count += 1
	return live_birth_count

def countLiveBirthsByOrder(records):
	live_birth_counts = {}
	for record in records:
		if record.outcome == LIVE_BIRTH_OUTCOME:
			if record.birthord in live_birth_counts.keys():
				live_birth_counts[record.birthord] += 1
			else: 
				live_birth_counts[record.birthord] = 1
	return live_birth_counts

def avgLivePregLen(records):
	live_births_counts_first_ord = 0
	live_births_counts_other_ord = 0
	live_births_length_first_ord = 0
	live_births_length_other_ord = 0
	
	for record in records:
		if record.outcome == LIVE_BIRTH_OUTCOME:
			if record.birthord == 1:
				live_births_counts_first_ord += 1
				live_births_length_first_ord += record.prglength	
			else:
				live_births_counts_other_ord += 1
				live_births_length_other_ord += record.prglength
	
	print 'AVG Pregnancy Length for 1st babies', live_births_length_first_ord*1.0 / live_births_counts_first_ord
	print 'AVG Pregnancy Length for other order babies', live_births_length_other_ord*1.0 / live_births_counts_other_ord


avgLivePregLen(table.records)

def firstPregnancies(records):
	return list(filter(lambda x: x.outcome == LIVE_BIRTH_OUTCOME and x.birthord == 1, records))

def otherPregnancies(records):
	return list(filter(lambda x: x.outcome == LIVE_BIRTH_OUTCOME and x.birthord != 1, records))

print ('variance of first live preg length', 
   math.sqrt(thinkstats.Var(map(lambda x: x.prglength, firstPregnancies(table.records))))) 
print ('variance of other live preg length', 
   math.sqrt(thinkstats.Var(map(lambda x: x.prglength, otherPregnancies(table.records)))))

hist = Pmf.MakeHistFromList(list(map(lambda x: x.prglength, table.records)))
print hist.Mode()

for tuple in hist.AllModes():
	print tuple

def RenderPlot(hist):
   vals, freq = hist.Render()
   rectangles = pyplot.bar(vals, freq)
   pyplot.show()

def RemainingLifetime(lifetime_pmf, age):
    rv = lifetime_pmf.Copy()
    while age != 0:
	rv.Set(age, 0)
	age -= 1
    rv.Normalize()
    return rv

pmf = Pmf.MakePmfFromList([1,2,23,4,4,1,2,45,6,8,3,8,93,19,4,1,51,23,10])
new_pmf = RemainingLifetime(pmf, 10)

#RenderPlot(new_pmf)

def PmfMean(pmf):
   mean = 0
   for value, freq in pmf.Items():
       mean += value * freq
   return mean

print (pmf.Mean(), PmfMean(pmf))

def PmfVar(pmf):
   mean = pmf.Mean()
   var = 0
   for value, freq in pmf.Items():
	var += freq * (value - mean) * (value - mean)
   return var

print (pmf.Var(), PmfVar(pmf))

