# Opencv

* [nameWindow](####namedWindow("name",size))
* [imread](####imread(文件名,FLAG))
* [imwrite](####)
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

---

```python
def process(
      self, input_data: Union[np.ndarray, 
    Mapping[str, Union[np.ndarray,message.Message]]]
  ) -> NamedTuple:
    """Processes a set of RGB images data and output SolutionOutputs.

    Args:
      input_data: Either a single numpy ndarray object representing the solo
        images input of a graph or a mapping from the stream name to the images or
        proto data that represents every input streams of a graph.

    Raises:
      NotImplementedError: If input_data contains audio data or a list of proto
        objects.
      RuntimeError: If the underlying graph occurs any error.
      ValueError: If the input images data is not three channel RGB.

    Returns:
      A NamedTuple object that contains the output data of a graph run.
        The field names in the NamedTuple object are mapping to the graph output
        stream names.

    Examples:
      solution = solution_base.SolutionBase(graph_config=hand_landmark_graph)
      results = solution.process(cv2.imread('/tmp/hand0.png')[:, :, ::-1])
      print(results.detection)
      results = solution.process(
          {'video_in' : cv2.imread('/tmp/hand1.png')[:, :, ::-1]})
      print(results.hand_landmarks)
    """
    self._graph_outputs.clear()

    if isinstance(input_data, np.ndarray):
      if len(self._input_stream_type_info.keys()) != 1:
        raise ValueError(
            "Can't process single images input since the graph has more than one input streams."
        )
      input_dict = {next(iter(self._input_stream_type_info)): input_data}
    else:
      input_dict = input_data

    # Set the timestamp increment to 33333 us to simulate the 30 fps video
    # input.
    self._simulated_timestamp += 33333
    for stream_name, data in input_dict.items():
      input_stream_type = self._input_stream_type_info[stream_name]
      if (input_stream_type == PacketDataType.PROTO_LIST or
          input_stream_type == PacketDataType.AUDIO):
        # TODO: Support audio data.
        raise NotImplementedError(
            f'SolutionBase can only process non-audio and non-proto-list data. '
            f'{self._input_stream_type_info[stream_name].name} '
            f'type is not supported yet.')
      elif (input_stream_type == PacketDataType.IMAGE_FRAME or
            input_stream_type == PacketDataType.IMAGE):
        if data.shape[2] != RGB_CHANNELS:
          raise ValueError('Input images must contain three channel rgb data.')
        self._graph.add_packet_to_input_stream(
            stream=stream_name,
            packet=self._make_packet(input_stream_type,
                                     data).at(self._simulated_timestamp))
      else:
        self._graph.add_packet_to_input_stream(
            stream=stream_name,
            packet=self._make_packet(input_stream_type,
                                     data).at(self._simulated_timestamp))

    self._graph.wait_until_idle()
    # Create a NamedTuple object where the field names are mapping to the graph
    # output stream names.
    solution_outputs = collections.namedtuple(
        'SolutionOutputs', self._output_stream_type_info.keys())
    for stream_name in self._output_stream_type_info.keys():
      if stream_name in self._graph_outputs:
        setattr(
            solution_outputs, stream_name,
            self._get_packet_content(self._output_stream_type_info[stream_name],
                                     self._graph_outputs[stream_name]))
      else:
        setattr(solution_outputs, stream_name, None)

    return solution_outputs
```
