while [ 1 ]
do
	nc -l -p 8888 | mplayer -fps 31 -cache 1024 -
done