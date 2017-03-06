# WJSTestSuite
test suite for the weighted job scheduling problem


# Usage:
First, clone the WJSTestSuite directory into the directory that has your payoff_sched executable (such that payoff_sched and WJSTestSuite are in the same directory and on the same level -- "tests" and "payoff_sched" executables should not be on the same level).
Now run the tests by executing the "tests" file.

Note: you may need to add execute permissions to tests and payoff_sched:

<pre><code>chmod +x payoff_sched
cd WJSTestSuite
chmod +x tests
dos2unix tests
./tests</code></pre>


# Notes:
- checks for expected versus actual payoff
- checks for first line syntax
- checks for sorted output schedules
- checks for overlapping schedules in output
- checks for inconsistency between payoff given on first line and payoff given by schedules
- DOES NOT check for any specific schedule
- DOES NOT check for existence of the outputted schedule's intervals in input intervals
