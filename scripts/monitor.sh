#!/bin/bash

# Author: Dasun
# Date: 2026-04-08
# Version: 1.0
# Description: System monitoring script with alert

set -e
set -o pipefail

echo "Checking system..."

# Disk usage
df -h

# Memory usage
MEM=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

echo "Memory usage: $MEM %"

if (( $(echo "$MEM > 80" | bc -l) )); then
    echo "⚠️ ALERT: High memory usage"
fi

# CPU cores
echo "CPU cores:"
nproc