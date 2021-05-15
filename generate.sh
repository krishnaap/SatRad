echo Starting process

cd /home/Cast/sat_retrieved
echo saving video for satellite images
convert -delay 50 20200808-0*.jpg Satellite_retrieved.mp4
echo saving video : Success

 
cp Satellite_retrieved.mp4 /home/Cast/

cd /home/Cast/Radar_retrieved/
echo saving video for radar
convert -delay 50 20200808-0*.gif Radar_retrieved.mp4
echo saving video : Success

 
