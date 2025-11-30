#!/bin/bash

#calculates the CPU% every 2 seconds from proc
get_sum () {
	total=0

	for val in $1
	do
		(( total += val ))
	done
	echo $total 
}

#calculate idles and total
past_totals=$(awk '/^cpu[0-9]/ {print $2+$3+$4+$5+$6+$7+$8+$9+$10}' /proc/stat)
past_idles=$(awk '/^cpu[0-9]/ {print $4}' /proc/stat)
sleep 2
current_totals=$(awk '/^cpu[0-9]/ {print $2+$3+$4+$5+$6+$7+$8+$9+$10}' /proc/stat)
current_idles=$(awk '/^cpu[0-9]/ {print $4}' /proc/stat)


past_total=$(get_sum "$past_totals")
present_total=$(get_sum "$current_totals")
past_idle=$(get_sum "$past_idles")
present_idle=$(get_sum "$current_idles")

#idle times 
delta_total=$(( present_total - past_total ))
delta_idle=$(( present_idle - past_idle ))


#awk for float division
cpu_idle_percent=$(awk "BEGIN {print ($delta_idle/$delta_total)*100}")
cpu_user_percent=$(awk "BEGIN {print (1 - $delta_idle/$delta_total)*100}")

echo "idle percent" $cpu_idle_percent
echo "cpu percent" $cpu_user_percent