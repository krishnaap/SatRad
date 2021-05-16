# SATellite and RADar image retrieval and animation creator tool
This is a python scripts for downloading consecutive satellite/radar images with a specific time interval. Then save those downloaded images into an animation.
The `main.sh` script will run whole process, start with simultaneous running of both python scripts `sat_retriever.py` and `rad_retriever.py` and save images into `sat` and `rad` foldders in the background. When you need to stop the data retrieval and make the downloaded images into video ***press ctrl+c***, this will stop retrieval and make the video.

###### Required python packages for aquiring images.
- cv2
- glob
- apscheduler

###### Required packages for making animation
- Imagemagic

###### If you are using Python on Anaconda, activate your conda environment before running th script.

