#!/bin/bash
import sys
if diff ExpectedS1.txt Sorted.txt; then
	echo "s1 passed"
else
	sys.exit("s1 failed")
fi
if diff ExpectedS2.txt Sorted2.txt; then
	echo "s1 passed"
else
	sys.exit("s2 failed")
fi
