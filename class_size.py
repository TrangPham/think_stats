import Pmf

def ClassSizes():
    return {
        7:8,
	12:8,
	17:14,
	22:4,
	27:6,
	32:12,
	37:8,
	42:3,
	47:2,
	}

def ClassSizesPmf():
    return Pmf.MakePmfFromDict(ClassSizes())

print 'Mean:', ClassSizesPmf().Mean()

def SampledClassSizesPmf():
    pmf = ClassSizesPmf().Copy()
    for value, prob in pmf.Items():
	#pmf.Mult(value, value)
	pmf.Set(value, value * prob)
    pmf.Normalize()
    return pmf

print 'Baised Mean Sampled:', SampledClassSizesPmf().Mean() 

def UnbiasedSampledClassSizesPmf():
    pmf = SampledClassSizesPmf().Copy()
    for value, prob in pmf.Items():
	pmf.Set(value, 1/prob)
    pmf.Normalize()
    return pmf

print 'Unbiased Sampled Mean:', UnbiasedSampledClassSizesPmf().Mean()
