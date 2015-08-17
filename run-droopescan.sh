set -e 
set -u

cd droopescan
cwd=/root/final/
for file in ${cwd}part*; do
	results_dir=${cwd}results-$(basename $file)/
	echo $results_dir
	url_file=$file
	mkdir -p $results_dir;
	./droopescan scan -U $url_file --error-log ${results_dir}error-log.txt --massscan-override -e v 1> ${results_dir}results.json 2>${results_dir}stderr.txt &
done
