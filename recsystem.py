'''
Harold and Kumar escape from Guantanamo Bay
Ted
Straight Outta Compton
A very Harold and Kumar Christmas
Get rich or die tryin'
Notorious
Frozen
Tangled
Cinderella
Toy Story 3
'''
#actual code
import sys
import time
from numpy import *
t=time.time()
num_movies=10
num_users=5
ratings=random.randint(11,size=(num_movies,num_users))
print "ratings"
print ratings
#convert all ratings to 1 if they are not equal to 0; logical NOT operator used
rated_by_user=(ratings!=0)*1
print "rated_by_user"
print rated_by_user
my_ratings=zeros((num_movies,1))
my_ratings[0]=8
my_ratings[4]=7
my_ratings[7]=3
print "my_ratings"
print my_ratings
#append column vector to ratings; axis=1 means column
ratings = append(my_ratings,ratings,axis=1)
print "ratings"
#ratings vector with my_ratings column vector appended
print ratings

rated_by_user=append((my_ratings!=0)*1,rated_by_user,axis=1)
print "rated_by_user"
print rated_by_user

#start mean normalization; subtract each element in the matrix with the avg value to know which value is above or below averages
mean_ratings=[]
mean_ratings=array(mean_ratings)
for i in range(0,ratings.shape[0]):
    s=[]
    s=array(s)
    #append only those values to s which are not zeros
    for j in range(0,ratings.shape[1]):
        if ratings[i][j]!=0:
            s=append(ratings[i][j],s)
    #print s
    mean_ratings=append(mean(s),mean_ratings)
print mean_ratings
print "-----"
#reverse mean_ratings
mean_ratings=mean_ratings[::-1]
print mean_ratings
print "-----"

#make mean_ratings a column vector
mean_ratings=mean_ratings.reshape(mean_ratings.shape[0],1)
print mean_ratings
print "-----"
#subtract the average of each row from every element of ratings matrix excluding elements = 0
for i in range(0,ratings.shape[0]):
    for j in range(0,ratings.shape[1]):
        if ratings[i][j]!=0:
            ratings[i][j]=ratings[i][j]-mean_ratings[i]
print ratings

#num_users =number of columns in the ratings matrix
num_users=ratings.shape[1]
#number of features of a movie can be the genres in which a movie can be included
num_features=10
#randn is for normally distributed
movie_features=random.randn(num_movies,num_features)
user_prefs=random.randn(num_users,num_features)
initial_X_and_theta = r_[movie_features.T.flatten(), user_prefs.T.flatten()]

print initial_X_and_theta
sys.exit()
def unroll_params(X_and_theta, num_users, num_movies, num_features):
	first = X_and_theta[:num_movies * num_features]
	# Reshape this column vector into a 10 X num_features matrix
	X = first.reshape((num_features, num_movies)).transpose()
	# Get the remaining values after the first matrix
	last = X_and_theta[num_movies * num_features:]
	# Reshape this column vector into a 6 X num_features matrix
	theta = last.reshape(num_features, num_users ).transpose()
	return X, theta


def calculate_gradient(X_and_theta, ratings, rated_by_user, num_users, num_movies, num_features, reg_param):
	#get movie_features and user_prefs separately
	X, theta = unroll_params(X_and_theta, num_users, num_movies, num_features)
	
	#we multiply by rated_by_user because we consider observations for which a rating is there
	difference = X.dot( theta.T ) * rated_by_user - ratings
	X_grad = difference.dot( theta ) + reg_param * X
	theta_grad = difference.T.dot( X ) + reg_param * theta
	#convert to column vector 
	return r_[X_grad.T.flatten(), theta_grad.T.flatten()]


def calculate_cost(X_and_theta, ratings, rated_by_user, num_users, num_movies, num_features, reg_param):
	X, theta = unroll_params(X_and_theta, num_users, num_movies, num_features)
	
	#multiply by rated_by_user because we only want to consider observations for which a rating was given; subtract from ratings to get squared errors
	cost = sum( (X.dot( theta.T ) * rated_by_user - ratings) ** 2 ) / 2
	regularization = (reg_param / 2) * (sum( theta**2 ) + sum(X**2))
	return cost + regularization

from scipy import optimize
# regularization paramater
reg_param = 30
#makes predictions; fmin minimizes the cost function; fprime is derivative of cost function
minimized_cost_and_optimal_params = optimize.fmin_cg(calculate_cost, fprime=calculate_gradient, x0=initial_X_and_theta, 								args=(ratings, rated_by_user,num_users,num_movies,num_features,reg_param), 								maxiter=100, disp=True, full_output=True ) 

cost, optimal_movie_features_and_user_prefs = minimized_cost_and_optimal_params[1], minimized_cost_and_optimal_params[0]
movie_features, user_prefs = unroll_params(optimal_movie_features_and_user_prefs, num_users, num_movies, num_features)

print movie_features
print user_prefs

all_predictions = movie_features.dot( user_prefs.T )
print all_predictions

# add back the ratings_mean column vector to my predictions
predictions_for_me = all_predictions[:, 0:1] + mean_ratings
print "my actual ratings"
print my_ratings
print "suggestions for me based on my previous ratings"
print predictions_for_me
print time.time()-t
