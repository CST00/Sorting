#!/bin/bash
if diff ExpectedS1.txt Sorted.txt; then
	true
else
	exit(1)
fi
if diff ExpectedS2.txt Sorted2.txt; then
	true
else
	exit(1)
fi
