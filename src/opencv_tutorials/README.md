# Opencv

* namedWindow 
* imread
* imwrite
* VideoCapture


#### namedWindow("name",size)
```python
import cv2
cv2.namedWindow("name",cv2.WINDOW_AUTOSIZE)  ## to create a window
cv2.imshow()
```
---

#### imread(文件名,FLAG)

The following codes:FLAG     

->  *imgcodecs.hpp*

```c
//! Imread flags
enum ImreadModes {
       IMREAD_UNCHANGED            = -1, //!< If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.
       IMREAD_GRAYSCALE            = 0,  //!< If set, always convert image to the single channel grayscale image (codec internal conversion).
       IMREAD_COLOR                = 1,  //!< If set, always convert image to the 3 channel BGR color image.
       IMREAD_ANYDEPTH             = 2,  //!< If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.
       IMREAD_ANYCOLOR             = 4,  //!< If set, the image is read in any possible color format.
       IMREAD_LOAD_GDAL            = 8,  //!< If set, use the gdal driver for loading the image.
       IMREAD_REDUCED_GRAYSCALE_2  = 16, //!< If set, always convert image to the single channel grayscale image and the image size reduced 1/2.
       IMREAD_REDUCED_COLOR_2      = 17, //!< If set, always convert image to the 3 channel BGR color image and the image size reduced 1/2.
       IMREAD_REDUCED_GRAYSCALE_4  = 32, //!< If set, always convert image to the single channel grayscale image and the image size reduced 1/4.
       IMREAD_REDUCED_COLOR_4      = 33, //!< If set, always convert image to the 3 channel BGR color image and the image size reduced 1/4.
       IMREAD_REDUCED_GRAYSCALE_8  = 64, //!< If set, always convert image to the single channel grayscale image and the image size reduced 1/8.
       IMREAD_REDUCED_COLOR_8      = 65, //!< If set, always convert image to the 3 channel BGR color image and the image size reduced 1/8.
       IMREAD_IGNORE_ORIENTATION   = 128 //!< If set, do not rotate the image according to EXIF's orientation flag.
     };
```
----
#### imwrite (save)
imwrite(name,img)
name: save_name
img: type = mat(numpy.ndarrary)

---

##### VideoCapture
source code -> *modules/videoio/include/opencv2/videoio.hp*  

<p>@brief Opens a camera for video capturing
Read the camera and get the pic</p>

cap.read(): return two value, one is Boolean, one is video frame, type of frame is __numpy.ndarray__

cap.release()
