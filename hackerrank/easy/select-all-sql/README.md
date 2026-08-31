# Revising the Select Query II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Query all columns (attributes) for every row in the **CITY** table.

The **CITY** table is described as follows:  
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

**Input Format**

 

**Constraints**

 

**Output Format**

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T21:03:24.443Z  

```sql
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/select-all-sql/problem)