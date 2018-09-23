# Tamil Handwritten Optical Character Recognition - Dataset creation and Training a CNN on this data

# Data Acquisition
There is no complete data for tamil handwritten characters. So the first natural step was to create a dataset which is sufficiently large, easier to create and also can be reproduced atleast for other Dravidian languages(Tamil is the oldest of them).

A form contatining 266 square fields was created for collecting data, this form is available in "ImageStorage/Forms/DataAcquisitionForm.jpg". The filled forms were scanned using a hp scanner with resolution set to 600dpi. These scanned forms are available in "ImageStorage/RawImages/". 

Instructions:
Note: Make sure CMAKE and OPENCV is installed
- Use CMAKE to build a binary of DataAcquisiton.cpp present in the DataAcquistion folder.
- After that you can choose to extract individual images
by running "./DataAcquisition [raw image source file] [destination folder path]".
- If you want to extract all raw images simply run 
"./extract.sh" from the project root folder.
- The output images will be present in "ImageStorage/ResultantStorage".
- The writers have made some mistakes considering they wrote 247 letters, the wrongly written letters have been struck out and were written in the last column of the form, images extracted from the last column alone is saved as s*.png. Find and replace all these images appropriately.
- Also some of RawImages cannot be processed, when fed to the script they output less number of output images, a list of these RawImages are available in the RawImages folder. I didn't make a attempt to find why this happens are rectify this, I simply didn't use these RawImages,  out of the 172 I used only 151.

# Data Conversion
The output images are converted to a numpy array file which is stored in the DataBinaryStorage, there will be no file in the repository, you have to create this file by running the python script "DataAcquisition/DataConversion.py". Also to convert only particular characters to a numpy array file a mapping method is used, the maps are provided in "LabelMaps/".

# CNN training
A CNN model is trained using this data. I trained the model with 34827 images(141 persons * 247 letters) with 247 classes and tested using 2470 images(10 * 247) with 247 clasess. A test accuracy of 0.917 was achieved after 30 epochs. This CNN code is given in "NETWORKS/Recozhize.py", the output model files will be written to "Models/".

This repository contains no model files, the trained model files and a working demo can be found in another repository https://github.com/aravindarc/tamil_hocr 
