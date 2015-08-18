function pos() { nb=$1; cat -n final/part$nb | grep `tail -n 1 final/results-part$nb/error-log.txt | awk -F' ' '{print $8}'` 2> /dev/null; }              
function posa() {
	for nb in $(seq 0 9); do 
		while true ; do
			posr=$(pos 0$nb);
			ec=$?
			if [[ $ec -eq 0 ]]; then
				echo "$nb -> $(echo "$posr" | head -n 1)"
				break;
			fi
			sleep 0.1;
		done;
	done;
}
