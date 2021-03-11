# WebCam-Starter

Script developed for quick testing of cameras using OpenCv video capture.

Follow this excellent [tutorial](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)
(a simple pip-install method) to set up OpenCV first.

Then, install additional libraries (in the `cv` virtual env.):

```bash
pip install -r requirements.txt
```

Next, patch imutils lib., which does not allow to change the resolution of a USB webcam. Update 2 files:
- video/videostream.py
- video/usbwebcam.py

(Add support for res argument in the usbwebcam file, TODO: add detail changes above)

Note: the above step won't be required when maintainers start looking into PR's, or when I create a new forked package
with the functionality in place.
