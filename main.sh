echo starting satellite and radar image retrieval
echo press ctrl + c to start saving images into animation at any instant.

(
	trap exit INT 
	python rad_retrieval.py & python sat_retrieval.py & wait
)


echo Retrieval complete

cd ./sat
echo saving video for satellite images
convert -delay 50 20210516-*.jpg Satellite_retrieved.mp4
echo saving video : Success
cp Satellite_retrieved.mp4 ./cast/

cd ./rad
echo saving video for radar
convert -delay 50 20210516-*.gif Radar_retrieved.mp4
echo saving video : Success
cp Radar_retrieved.mp4 ./cast/
 
