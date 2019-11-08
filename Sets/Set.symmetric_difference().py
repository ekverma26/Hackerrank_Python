# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some
# have subscribed to French only, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the
# French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper
# but not both.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper. 
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper. 
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints
# 0 < Total number of students in college < 1000

# Output Format
# Output total number of students who have subscriptions to the English or the French newspaper but not both.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1 = set(map(int, input().split()))
b=int(input())
s2 = set(map(int, input().split()))
s3=set()
s3=s1.difference(s2)
s4=set()
s4=s2.difference(s1)
print(len(s3)+len(s4))
