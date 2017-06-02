import Pmf
import relay
import myplot

def BiasRacePmf(unbiased_pmf, runner_speed):
    biased_pmf = {}
    for value, prob in unbiased_pmf.Items():
	biased_pmf[value] = prob * abs(value - runner_speed)
    rv = Pmf.MakePmfFromDict(biased_pmf)
    rv.Normalize()
    return rv

def RacePmf():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    return Pmf.MakePmfFromList(speeds)

myplot.Pmf(BiasRacePmf(RacePmf(), 7.5))
myplot.Show(title='PMF of biased running speeds of runner at 7.5 mph',
	xlabel='seed (mph)', ylabel='probability', label='prob')
