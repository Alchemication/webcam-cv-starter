"""
Usage: python main.py --display [n|y] --fps [n|y]
Flags:
    --display: this switch is used to display video in the CLI (default = n)
    --fps: this switch is used to display the FPS when script is terminated (default = n)
"""

from imutils.video import VideoStream
from imutils.video import FPS
from time import sleep
import logging
import traceback
import cv2
import sys
import click


fps_checker = None


@click.command()
@click.option('--display', '-d', 'display', default='n')
@click.option('--fps', '-f', 'fps', default='n')
def start(display='n', fps='n'):
    global fps_checker
    logging.info(f"Starting stream...")
    vs = VideoStream(src=0, resolution=(1280, 960), framerate=30).start()  # 720p
    sleep(0.2)  # might be needed to warm up camera sensor
    if fps.lower() == 'y':
        fps_checker = FPS().start()

    logging.info(f"Receiving frames...")
    while True:
        # read the frame from the camera
        frame = vs.read()

        # check if image needs to be displayed (usually for debugging)
        # logging.info(f'Read frame: {frame.shape}')
        if display.lower() == 'y':
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info('Quitting...')
            break
        # update the FPS counter and display FPS
        if fps.lower() == 'y':
            fps_checker.update()


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s.%(msecs)03f %(levelname)s %(message)s",
                        level=logging.INFO, datefmt="%H:%M:%S")
    try:
        start()
    except (KeyboardInterrupt, SystemExit):
        logging.info('Exit due to keyboard interrupt')
    except Exception as ex:
        logging.error('Python error with no Exception handler:')
        logging.error(f'Exception msg: {str(ex)}')
        traceback.print_exc()
    finally:
        # stop the timer and display FPS information
        if fps_checker is not None:
            fps_checker.stop()
            logging.info(f"Elapsed time: {fps_checker.elapsed():.2f}")
            logging.info(f"Approx. FPS: {fps_checker.fps():.2f}")
        cv2.destroyAllWindows()
        sys.exit()
