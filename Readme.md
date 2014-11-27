It was a project given to me as a part of a programme between student and the company(Amazon).

It is an extension of the Route Generator which gives probable reasons for

exceptions in actual transit time taken. While generating the route parameters like altitude travelled i.e. sum 

of differences for all the locations in the route and connectivity of the route was calculated(It is the ratio of 

no of locations with population above certain value and total no of locations in route). Along with those 

parameters, a Holiday checker is used which gives the states affected by a certain Holiday. The date of 

travel, route, connectivity and altitude travel is used to check whether if there is a delay in transit time is it 

due to Holidays, major altitude changes in route, bad connectivity and other factors. If there is no reason for 

delay the records are stored in files and the next time, new source and destination being submitted are 

checked in this file for a sufficient count of occurrence which gives us an idea that it is not an exception but 

the delay in the route frequently occurs. 

For testing purpose random data was generated using a composition of Exponential and Bernoulli
