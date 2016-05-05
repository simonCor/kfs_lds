myDate=`date +'%Y-%m-%d_%H_%M_%S'`
myFolder=/home/pi/camera/$myDate
mkdir $myFolder
#raspivid -o /home/pi/$myDate.h264 -n -t 1200000
#-ex antishake - Not used because may influence -ss
raspistill -bm -t 0 -tl 500 -ss 2 -o $myFolder/%05d.jpg
