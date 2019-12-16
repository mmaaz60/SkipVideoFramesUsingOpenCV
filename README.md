# Skip Video Frames using OpenCV

In this repository, I will show you two pipelines to skip frames while processing a video in an application. I will provide a comparison of two practices in terms of speed. Let's get started.

## Requirements
The code has been tested with Python 3.7.4 and OpenCV 4.1.1.

## Skip Frames using VideoCapture.read() method

The script **"skip_frames_using_read.py"** implements video frames skip using VideoCapture.read() method of OpenCV. The code reads each frame of video and process it only if processing frame.

## Skip Frames using VideoCapture.grab() method

The script **"skip_frames_using_grab.py"** implements video frames skip using VideoCapture.grab() method of OpenCV. The code grabs each frame of video and encode only the processing frame.

Both scripts takes two command line arguments. The path to input video file and intended processing FPS. For further help please run the below commands,
```python
$ python skip_frames_using_read.py -h
$ python skip_frames_using_grab.py -h
```
To use with the video provided in this repository,
```python
$ python skip_frames_using_read.py -v video/GOT.mp4 -fps 5
$ python skip_frames_using_grab.py -v video/GOT.mp4 -fps 5
```
Both of the sripts make best efforts to process only the mentioned number of frames per second of video. The scripts print the prcessing time and processing speed (number of frames processed in one second) on the terminal. Note that the 'processing speed' depends upon the underline hardware.

## Experimental Results

The below table summarizes the experimental results. The experiments are performend on an **Intel(R) Core(TM) M-5Y10c CPU @ 0.80GHz 1.00 GHz based machine with 4 GB of RAM. The operating system was Windows 10 (64 bit).**

| Method | Video Resolution  | Video Duration | Video FPS | Processing FPS | Processing Time | Processing Speed | Speed Gain |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| VideoCapture.read()  | 1920*1080  | 54 sec  | 24.01  | 5  | 19.60 sec | 13.21 frames/sec | 1x |
| VideoCapture.grab()  | 1920*1080  | 54 sec  | 24.01  | 5  | 9.65 sec | **26.84 frames/sec** | **2.03x** |
| VideoCapture.read()  | 1920*1080  | 54 sec  | 24.01  | 1  | 17.20 sec | 3.14 frames/sec | 1x |
| VideoCapture.grab()  | 1920*1080  | 54 sec  | 24.01  | 1  | 5.31 sec | **10.17 frames/sec** | **3.24x** |

## Why using .grab() method outperforms using .read()?

VideoCapture.read() method grabs and encodes each video frame. However, while using VideoCapture.grab(), we grab each video frame but only encode the processing frame.

## CPU time of .read(), .grab() and .retrieve() calls
Below table summarizes the CPU time for .read(), .grab() and .retrieve() functions of VideoCapture object of OpenCV.

| Method | Video Resolution  | Average CPU Time per Call |
| ------------- | ------------- | ------------- |
| VideoCapture.read() | 1920*1080 | 12.68 ms |
| VideoCapture.grab() | 1920*1080 | 2.57 sms |
| VideoCapture.retrieve() | 1920*1080 | 12.05 ms |
| VideoCapture.read() | 1280*720 | 5.80 ms |
| VideoCapture.grab() | 1280*720 | 0.66 ms |
| VideoCapture.retrieve() | 1280*720 | 5.57 ms |

All benchmarks are performed on an **Intel(R) Core(TM) M-5Y10c CPU @ 0.80GHz 1.00 GHz based machine with 4 GB of RAM. The operating system was Windows 10 (64 bit).**

## Conclusion

The above experiments show that, the VideoCapture.grab() method is the finest choice over VideoCapture.read() method in applications where we have to process a fraction of video frames. Moreover, the processing speed decreases and speed gain increases with the increase in number of skip frames.

## References
- https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html