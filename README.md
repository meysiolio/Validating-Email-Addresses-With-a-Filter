You are given an integer ***N*** followed by ***N*** email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.  


Valid email addresses must follow these rules:  

* It must have the username@websitename.extension format type.  
* The username can only contain letters, digits, dashes and underscores ***[a - z],[A - Z],[0 - 9],[_-]***.  
* The website name can only have letters and digits ***[a - z],[A - Z],[0 - 9]***.  
* The extension can only contain letters ***[a - z],[A - Z]***.  
* The maximum length of the extension is **3**.  

**Example**

Complete the function fun in the editor below.  

fun has the following paramters:  

* string s: the string to test  

**Returns**

* boolean: whether the string is a valid email or not  

**Input Format**

The first line of input is the integer ***N***, the number of email addresses.  
***N*** lines follow, each containing a string.  

Each line is a non-empty string.

**Sample Input**
```
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```
**Sample Output**
```
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```