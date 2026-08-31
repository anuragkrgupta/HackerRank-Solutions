# Japanese Cities' Names

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Query a list of **CITY** and **STATE** from the **STATION** table.  
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
**Submitted:** 2026-08-31T21:07:28.575Z  

```sql
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-1/problem)