#!/bin/bash

# Get current time (HH:MM format)
current_time=$(date +"%H:%M")

# Define workday end time
work_end="18:00"

# Convert HH:MM to minutes since midnight
current_minutes=$(awk -F: '{print $1 * 60 + $2}' <<< "$current_time")
end_minutes=$(awk -F: '{print $1 * 60 + $2}' <<< "$work_end")

# Calculate remaining minutes
remaining_minutes=$((end_minutes - current_minutes))

if [ "$remaining_minutes" -gt 0 ]; then
    hours=$((remaining_minutes / 60))
    minutes=$((remaining_minutes % 60))
    echo "Current time: $current_time. Workday ends in $hours hours and $minutes minutes."
else
    echo "Workday has already ended!"
fi
