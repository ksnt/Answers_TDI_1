# Answers_TDI_1

Please use python3.x

## Q1.What is the mean of your total payment for N=10?

How to provide an answer to the question:<br>
Computational complexity when using brute force is 3628800, i.e., O(10^6), therefore, we can compute directly<br><br>

source code:<br>
1-1.py (Brute Force approach - Note: this does not work well because counting method is wrong)<br>
1-2.py (Monte Carlo method approach)

How to use:<br>
$python 1-1.py 10<br>
$python 1-2.py <br>

## Q2.What is the standard deviation of your total payment for N=10?

How to provide an answer to the question:<br>
Computational complexity when using brute force is 3628800, i.e., O(10^6), therefore, we can compute directly<br><br>

source code:<br>
1-4.py (Monte Carlo method approach)

How to use:<br>
$python 1-4.py<br>


## Q3.What is the mean of your total payment for N=20?

How to provide an answer to the question:<br>
Computational complexity when using brute force is 2432902008176640000, i.e., O(10^18), therefore ,we cannot compute with brute force method<br><br>

source code:<br>
1-3.py (Monte Carlo method approach) <br>

How to use: <br>
$python 1-3.py <br>

## Q4. What is the standard deviation of your total payment for N=20?

How to provide an answer to the question:<br>
Computational complexity when using brute force is 2432902008176640000, i.e., O(10^18), therefore ,we cannot compute with brute force method<br><br>

source code:<br>
1-5.py (Monte Carlo method approach) <br>

How to use: <br>
$python 1-5.py <br>


## Q5. What is the probability that your total payment is greater than or equal to 45 for N=10?

How to provide an answer to the question:<br>
1. we can compute sample space and the number of cases where total payment is greater than or equal to 45, therefore, we can gain result from direct computation. (NOTE: I did get my answer in an another way, but this approach also might be good)
2. Just calculate upper probability when total payment is greater than or equal to 160 to normal distribution.
<br><br>

How to solve:<br>
I just caclculated upper probability when total payment is greater than or equal to 160. I used mean value and standard deviation earned through previous questions for this calculus.<br>


## Q6. What is the probability that your total payment is greater than or equal to 160 for N=20?

How to provide an answer to the question:<br>
1. Infer probability density function, then integrate the function and calculate the probability where total payment is greater than or equal to 160.(NOTE: I did get my answer in an another way, but this approach also might be good)
2. Just calculate upper probability when total payment is greater than or equal to 160 to normal distribution.<br><br>

How to solve:<br>
I just caclculated upper probability when total payment is greater than or equal to 160. I used mean value and standard deviation earned through previous questions for this calculus.<br>
