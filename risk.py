import survey
import thinkstats
import math
import Pmf

def Records():
    table = survey.Pregnancies()
    table.ReadRecords()
    return table.records

def AllLiveBirths():
    return list(filter(lambda x: x.outcome == 1, Records()))

def FirstBabiesLiveBirths():
    return filter(lambda x: x.birthord == 1, AllLiveBirths())

def OtherBabiesLiveBirths():
    return filter(lambda x: x.birthord != 1, AllLiveBirths())

def PregLengthPmf(records):
    return Pmf.MakePmfFromList(list(map(lambda x: x.prglength, records)))

def NormalizeToBins(pmf):
    bins = {'x <= 37': 0, '38 <= x <= 40': 0, '41 <= x': 0}
    for val, freq in pmf.Items():
	if val <= 37:
	    bins['x <= 37'] += freq
	elif 38 <= val and val <= 40:
	    bins['38 <= x <= 40'] += freq
	else:
	    bins['41 <= x'] += freq
    return Pmf.MakePmfFromDict(bins)

def ProbEarly(pmf):
    return NormalizeToBins(pmf).freq('x <= 37')

def ProbLate(pmf):
    return NormalizeToBins(pmf).freq('38 <= x <= 40')

def ProbOnTime(pmf):
    return NormalizeToBins(pmf).freq('41 <= x')

def PrintProbs(pmf):
    NormalizeToBins(pmf).Print()

def PrintRelativeProbs(pmf1, pmf2):
    pmf1_normalized = NormalizeToBins(pmf1)
    pmf2_normalized = NormalizeToBins(pmf2)
    for value in pmf1_normalized.Values():
	relative_probability = pmf1_normalized.Prob(value)/ pmf2_normalized.Prob(value)
	print value, ':', (relative_probability - 1)*100.0

def PrintRelativeRisks():
    print 'All Live Births:'
    PrintProbs(PregLengthPmf(AllLiveBirths()))

    print 'First Babies Live Births:'
    PrintProbs(PregLengthPmf(FirstBabiesLiveBirths()))

    print 'Other Babies Live Births:'
    PrintProbs(PregLengthPmf(OtherBabiesLiveBirths()))

    print 'First Babies VS Other Babies Relative Risk:'
    PrintRelativeProbs(PregLengthPmf(FirstBabiesLiveBirths()), PregLengthPmf(OtherBabiesLiveBirths()))

def ConditionalProbability(pmf, value):
    """Returns the prob of value given that probabilities < value did not occur"""
    for v in pmf.Values():
	if v < value:
	    pmf.Set(v, 0)
    pmf.Normalize()
    return pmf.Prob(value)

def PrintConditionalProb():
    print 'P(week = 39 | !(week < 39)):'
    print 'All Live Births:', ConditionalProbability(PregLengthPmf(AllLiveBirths()), 39)
    print 'First Babies:', ConditionalProbability(PregLengthPmf(FirstBabiesLiveBirths()), 39)

PrintRelativeRisks()
print '---'
PrintConditionalProb()
