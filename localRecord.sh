myDate=`date +'%Y-%m-%d_%H_%M'`
#raspivid -o /home/pi/$myDate.h264 -n -t 1200000
raspistill -vf -hf -tl 500 -o /home/pi/camera/$myDate.jpg
