from thinkstats import MeanVar

pumpkin_weights = [1, 1, 1, 3, 3, 591]

mean_and_var = MeanVar(pumpkin_weights)

print 'the mean is', mean_and_var[0]
print 'the variance is', mean_and_var[1]

