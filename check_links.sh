
# Check only internal URLs.
# --check-css
# --check-css   --> Check syntax of CSS URLs with the W3C online validator.
# --check-html  --> Check syntax of HTML URLs with the W3C online validator.
# --complete    --> Log all URLs, including duplicates. Default is to log duplicate URLs only once.
# NOT USING --verbose     --> Log all checked URLs. Default is to log only errors and warnings.
# --threads=100 --> Start 100 threads
# --ignore-url=/xmlrpc.php --> Ignore the xmlrpc.php file it's a wordpress thing.
# --ignore-url=^mailto     --> Ingore all mailto stuff on our website.
# --ignore-url=^/add-to-cart  -->  Ignore adding to cart stuff.
# --no-status         Do not print check status messages.
# --no-warnings       Don't log warnings. Default is to log warnings.
# Pipe it all into test.csv

# Final command:  this takes about 19 hours and works well enough.
#linkchecker www.dexterindustries.com --complete --recursion-level=10 --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
linkchecker www.dexterindustries.com --threads=25 --complete --recursion-level=10 --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv














# DEAD ATTEMPTS AREA OF FAILURE - CORDON THIS OFF BOYS, THESE DONT WORK!

# linkchecker www.dexterindustries.com --check-css --check-html --complete --threads=25 --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
# linkchecker www.dexterindustries.com --threads=25 --complete --no-status --no-warnings --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
# linkchecker www.dexterindustries.com --threads=25 --complete --no-status --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
# linkchecker www.dexterindustries.com --threads=25 --complete --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
# linkchecker www.dexterindustries.com --threads=25 --no-status --no-warning --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv

# (Works and takes 29 hours) linkchecker www.dexterindustries.com --complete --ignore-url=/xmlrpc.php --ignore-url=^mailto --ignore-url=/add-to-cart -ocsv > test.csv
# Check to certain recursion level
