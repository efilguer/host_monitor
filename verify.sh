#!/bin/bash


installed_ps=$(dpkg -l | awk '/^ii/ {print $2}')


for package in "$installed_ps"
do
	#in ubuntu debsums is used to verify package integrity
	#show packages that show missing or failed checks
	sudo debsums -a $package | grep -vi ok
done
