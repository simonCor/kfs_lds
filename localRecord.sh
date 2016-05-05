myDate=`date +'%Y-%m-%d_%H_%M_%S'`
myFolder=/home/pi/camera/$myDate
mkdir $myFolder
#raspivid -o /home/pi/$myDate.h264 -n -t 1200000
raspistill -bm -t 0 -tl 500 -o $myFolder/%05d.jpg
