#!/usr/bin/env python3
"""Script that reads stdin line by line and computes metrics"""

import sys

metrics = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()

        if len(data) > 2:
            status_code = data[-2]
            file_size = int(data[-1])
            total_size += file_size

            if status_code in metrics:
                metrics[status_code] += 1

        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for key in sorted(metrics.keys()):
                if metrics[key] > 0:
                    print("{}: {}".format(key, metrics[key]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for key in sorted(metrics.keys()):
        if metrics[key] > 0:
            print("{}: {}".format(key, metrics[key]))
