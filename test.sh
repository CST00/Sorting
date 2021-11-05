#!/bin/bash
if diff ExpectedS1.txt Sorted.txt; then
	echo "S1 Pass"
else
	echo"S1 Fail"
fi
if diff ExpectedS2.txt Sorted2.txt; then
	echo "S2 Pass"
else
	echo "S2 Failed"
fi
