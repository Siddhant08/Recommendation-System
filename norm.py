import random
#initialize empty lists to store ratings
rahul=[]
silky=[]

#randomly fill lists with ratings in the range 1 to 5 considering Rahul's standards
for i in range(10):
	#randomly fill lists with ratings in the range 1 to 5 considering Rahul's standards
	rahul.append(random.randint(1,5))
	#randomly fill lists with ratings in the range 5 to 10 considering Silky's standards
	silky.append(random.randint(5,10))
#see ratings by Rahul and Silky
print rahul
print silky

print "------------------------------------"

#initialize lists to store the normalized ratings by Silky and Rahul
silky_norm=[]
rahul_norm=[]

#Use the formula below to get normalized ratings for Rahul and Silky
'''
normalized value range is 0 to 1
for Rahul, min value = 1 and max value = 5
norm_value = min_norm_range + (norm_max_value - norm_min_value)/(current_max_range - current_min_range)*(value - current_min_range)
'''
for i in rahul:
	rahul_norm.append(0+0.25*(i-1))
'''
normalized value range is 0 to 1
for Silky, min value = 5 and max value = 10
norm_value = min_norm_range + (norm_max_value - norm_min_value)/(current_max_range - current_min_range)*(value - current_min_range)
'''
for i in silky:
	silky_norm.append(0+0.2*(i-5))

print rahul_norm
print silky_norm
