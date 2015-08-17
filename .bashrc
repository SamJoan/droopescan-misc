function pos() { nb=$1; cat -n final/part$nb | grep `tail -n 1 final/results-part$nb/error-log.txt | awk -F' ' '{print $8}'`; }              
