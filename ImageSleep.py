import cv2
import time
import os
def vidcapture():

    # Load the video capture object and read first frame
    cap = cv2.VideoCapture(0)
    _, prev_frame = cap.read()
    
    no_motion_start = None
    
    while True:
        # Read the current frame
        _, curr_frame = cap.read()
    
        # Calculate the difference between the two frames
        frame_diff = cv2.absdiff(prev_frame, curr_frame)
    
        # Convert the difference to grayscale
        gray = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    
        # Apply threshold to the grayscale image to highlight the motion
        # To adjust threshold of pixels, only adjust the second argument of the following line
        _, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    
        # Calculate the number of non-zero pixels in the thresholded image
        non_zero_pixels = cv2.countNonZero(thresh)
    
        if non_zero_pixels == 0:
            if no_motion_start is None:
                no_motion_start = time.time()
            else:
                elapsed_time = time.time() - no_motion_start
                if elapsed_time >= 30: # Elapsed time in seconds
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # Call for sleep state if timer reaches defined elapsed time
                    quit(0) #Closes program to avoid error on wakeup
                    
        else:
            no_motion_start = None
    
        # Update the previous frame
        prev_frame = curr_frame
    
        # Display the difference between the frames
        cv2.imshow("Motion Detection", thresh)
    
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object
    cap.release()
    
    # Destroy all windows
    cv2.destroyAllWindows()


def main():
    vidcapture()
if __name__ == "__main__":
    main()