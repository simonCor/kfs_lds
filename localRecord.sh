myDate=`date +'%Y-%m-%d_%H_%M'`
raspivid -o $(myDate).h264 -n -t 1200000
