# Solve Me First

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Complete the function $solveMeFirst$ to compute the sum of two integers.

**Example**  
$a = 7$  
$b = 3$  

Return $10$.

**Function Description**  

Complete the $solveMeFirst$ function with the following parameters:  

- $int\ a$: the first value
- $int\ b$: the second value

Returns  
- $int$: the sum of $a$ and $b$


**Input Format**

 

**Constraints**

 $1 \le a, b \le 1000$   

**Output Format**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T10:53:04.748Z  

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solveMeFirst(int a, int b) {
 // Hint: Type return a+b; below:
  return a+b;
}

int main() {
  int num1, num2;
  int sum;
  cin>>num1>>num2;
  sum = solveMeFirst(num1,num2);
  cout<<sum;
  return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/solve-me-first/problem)