# A Very Big Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large.

**Function Description**

Complete the $aVeryBigSum$ function with the following parameter(s):

- $int\ ar[n]$: an array of integers  

**Return**

- $long$: the sum of the array elements

**Input Format** 

The first line of the input consists of an integer $n$.  
The next line contains $n$ space-separated integers contained in the array. 

**Output Format**

Return the integer sum of the elements in the array.

**Constraints**  
$1 \le n \le 10$  
$0 \le ar[i] \le 10^{10}$  

**Sample Input**  

    STDIN                                                   Function
    -----                                                   --------
    5                                                       arr[] size n = 5
    1000000001 1000000002 1000000003 1000000004 1000000005  arr[...]  
    

**Output**   
	
    5000000015

**Note:** 

The range of the 32-bit integer is $(-2^{31}) ~to~  (2^{31} -1)~ or~ [-2147483648,2147483647]$.   

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.  

**Input Format**




**Constraints**

 

**Output Format**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T11:22:40.973Z  

```cpp
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'aVeryBigSum' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts LONG_INTEGER_ARRAY ar as parameter.
 */

long aVeryBigSum(vector<long> ar) {
    long sum = 0;
    for(int i = 0; i<ar.size(); i++){
        sum = sum + ar[i];
    }
    return sum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ar_count_temp;
    getline(cin, ar_count_temp);

    int ar_count = stoi(ltrim(rtrim(ar_count_temp)));

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split(rtrim(ar_temp_temp));

    vector<long> ar(ar_count);

    for (int i = 0; i < ar_count; i++) {
        long ar_item = stol(ar_temp[i]);

        ar[i] = ar_item;
    }

    long result = aVeryBigSum(ar);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/a-very-big-sum/problem)