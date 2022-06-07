# Code-Cheif-Activity-2
In this repositary I had uploaded three code of 
* Password Validation
* Phone number Validaton
* Url Validation
* In the Above we use Python programming language and we use replit to run the code
# The below code is to check the password is vaild or not 
* This is the Algorothim I excuted
* Steps to execute program
1. We are taking the password text as input from user.
2. creating the regex  compiler equation with given validation string
3. "re" module search() method we are passing the reg expression and user password input. This re.search() will be validate given string matches to the corresponding regex condition or not and return true/false response.
4. Based on this response we are printing the validate password result or else loop will continue till password is valid
# The below code is to check the Phone number is vaild or not 
* This is the Algorothim I excuted
* Steps to execute program
1. Take the input of a number as num
2. Now with the help of re.complie check whether the given number fiollows the given condition. Take re.complie variable pattren.
3. With the help of import re which help us to check if a particular string matches with the given condition where re rmeans regular expression
4. Now throught if the condition is true then enter the inout_code(country code)
5. Take a variable which specifies valid_code = flase
6. Throught the conditional statement check whether the string length of input_code is not less thhan 2 or greater than 3
7. If the len is not between them then print Invalid 
8. Now throught elif not re.search check if the '+' symbol exists in the number. If not print that it should exist
9. Now check if the digits are not in blw 0-9. If the number are not in blw them then then print the given string should exist blw the 0-9.
10. If the string follows above condition then valid-code:True.
11. Then If the patten.match which check if the pattren matches the given string then parint valid moble number
12. Else print Invalid moble Number.
# The below code is to check the Url number is vaild or not
1. Take a string input of a Url
2. Now throught a function called check-url take a function call 
3. now in the fuction call take a variable which has the condition that need to be fullfilled by the url and name it as re.exp.copy the taken url throught this 
4. Now take a variable named exp and re.complile (re-rep) that is to check if the taken Url has the given condition.
5. If the Url does not have the condition the print that the string is empty
6. If the reseach of the taken is ture that means it follows the conditions then the Url is valid
7. The string does not follow any rule then print Url is invalid.
