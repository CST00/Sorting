#!/bin/bash
import sys
if diff ExpectedS1.txt Sorted.txt; then
	echo "s1 passed"
else
	exit 1
fi
if diff ExpectedS2.txt Sorted2.txt; then
	echo "s2 passed"
else
	exit 2
fi
