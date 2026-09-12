# Weather Observation Station 3

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Query a list of **CITY** names from **STATION** for cities that have an even **ID** number. Print the results in any order, but exclude duplicates from the answer.  
The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where **LAT\_N** is the northern latitude and **LONG\_W** is the western longitude.

**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T21:14:31.475Z  

```sql
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-3/problem)