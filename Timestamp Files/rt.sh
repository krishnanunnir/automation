today=`date '+%H_%M_%S'`;
filename="$today-$1"
mv $1 $filename
mv $filename $2
touch $1


