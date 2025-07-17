# IEUK 2025 

## Overview

This Python script (`parser.py`) parses web server log files to help identify potential non-human (bot) traffic and summarize request patterns. It reads a specified log file (default `sample-log.log`).

This specific repo contains:

1. **Top IP Addresses**: Lists the 20 IPs with the most requests.
2. **Per-IP Log Files**: Creates a `.txt` file for each of these IPs containing all of their log entries.
3. **All Clients Summary**: Prints a sorted list of all client identifiers (e.g., user agents) and their request counts.
4. **Top Requested Resources**: Lists the 10 most-requested HTTP methods and paths.
5. **Overall Statistics**: Displays the total number of requests and average requests per IP.
6. **Successful Requests from Suspicious IPs**: Merges entries with status code 200 from every suspicious IP `successful_suspicious.txt`.

## File Structure

* `parser.py` — Main script containing all functions.
* `sample-log.log` — Example log file (should follow the format: IP, timestamp, request method, path, status, client identifier, etc.).

## Key Functions

* `ips()` — Returns a dict mapping each IP address to its request count.
* `clients()` — Returns a dict mapping each client identifier (e.g., user agent) to its request count.
* `req_resources()` — Returns a dict mapping each "METHOD PATH" to its request count.
* `reverse_sort_dict_by_val(d)` — Sorts any dict by values in descending order.
* `collate_suspicious_logs(ip)` — Writes all log lines for `ip` into `<ip>.txt`.
* `collate_successful_suspicious_logs(file_list)` — Appends all lines with status `200` from given files into `successful_suspicious.txt`.
* `main()` — Coordinates execution: computes summaries, prints results, and calls collation functions.

## Requirements

* Python 3.6 or higher
* No third-party libraries required (uses only Python built-in modules)

---
