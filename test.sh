#!/bin/bash
if diff ExpectedS1.txt Sorted.txt; then
	true
else
	false
fi
if diff ExpectedS2.txt Sorted2.txt; then
	true
else
	false
fi
