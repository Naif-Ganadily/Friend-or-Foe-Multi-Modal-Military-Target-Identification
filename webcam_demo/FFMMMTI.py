import socket
import pickle
import cv2
from inference.models.utils import get_roboflow_model
import time
import threading
import CRS_clientSide_friendly
import CRS_clientSide_unknown

# Inference server is required. To run docker, launch Docker Desktop application
# and open a command terminal (powershell/zsh) then enter one of the following commands 
# to run inference server on CPU or GPU. 
# docker run -it --net=host roboflow/roboflow-inference-server-cpu:latest
# docker run -it --network=host --gpus=all roboflow/roboflow-inference-server-gpu:latest

targetChallenge = "<missionSpecificPassword>"
knownClientIDs = ["101", "237", "5582"]
lengthOfMission = 1  # days until timeout
isStealthModeEnabled = False

# Define flags for friendly and unknown targets
targetIsFriendlyFlag = False
targetIsUnknownFlag = False

class Payload:
    def __init__(self, isStealth, id, password):
        self.isStealth = isStealth
        self.id = id
        self.password = password

def serverMain(server_socket):
    hostname = socket.gethostname()
    port = 9999
    # server_socket = socket.socket()  # get instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allow the socket to be reused
    server_socket.settimeout(86400 * lengthOfMission)  # Only wait 3 seconds for data, otherwise determine no data is provided
    server_socket.bind((hostname, port))  # bind host address and port together
    server_socket.listen(1)  # configure how many clients the server can listen simultaneously (1 target at a time for our use)
    print("Server is online & awaiting connections. Point the firearm at a target.")

    try:
        while True:
            conn, address = server_socket.accept()
            global targetIsFriendlyFlag, targetIsUnknownFlag
            if conn:
                print("Connection from: " + str(address))

                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = pickle.loads(conn.recv(1024))
                if data:
                    try:
                        clientPayload = Payload(data.isStealth, data.id, data.password)
                        if clientPayload.password == targetChallenge and clientPayload.id in knownClientIDs:
                            targetIsFriendly(address)
                            if clientPayload.isStealth:
                                print("Stealth mode activated")
                                break
                        else:
                            targetIsUnknown(address)
                            # Why is target unknown if they fail the challenge/response test?
                            # A target may fail the challenge response check for several reasons, not all of which indicate a foe.
                            # For example, if a friendly target has become detached from his group and during which time, the passcode has changed, they are friendly and should not be killed, however they will fail CRS.
                        # What if the client sends an incomplete object?
                    except Exception:
                        print(Exception)
                        targetIsUnknown(address)
                else:
                    break
    except socket.timeout:
        onMissionTimeout()
    finally:
        try:
            conn.close()  # always close the connection
            print("Connection closed")
        except:
            pass


def targetIsFriendly(address):
    print(f"Target at address: {address} is a friendly. DO NOT SHOOT!")
    global targetIsFriendlyFlag
    targetIsFriendlyFlag = True
    # Update optic system to represent friendly target


def targetIsUnknown(address):
    print(f"Target at address: {address} is a unknown. Proceed with caution")
    global targetIsUnknownFlag
    targetIsUnknownFlag = True
    # Update optic system to represent unknown target


def onMissionTimeout():
    print("System has timed-out.")
    exit(1)


def main():
    # Dictionary for easy color modification of the 2 classes
    colors = {"US_military": (0, 255, 0),  # Green
              "RU_military": (0, 0, 255)}  # Red

    # Roboflow model
    # Version 7 is yolov8s
    # Version 8 is yolov8m
    # Version 10 is yolov8n 
    model_name = "friend_or_foe_class_consolidation_objdet"
    model_version = "7"

    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Get Roboflow face model (this will fetch the model from Roboflow)
    model = get_roboflow_model(
        model_id="{}/{}".format(model_name, model_version),
        # Replace ROBOFLOW_API_KEY with your Roboflow API Key
        api_key="API-KEY"
    )

    # Define flag for inference/AI mode
    AI_mode_flag = False
    # Define flag for challenge response mode
    CRS_mode_flag = False
    # Define time duration for challenge response before timeout
    # Think of this as a threshold, if the target does not respond
    # CRS socket is closed and identity is not verified.
    CRS_duration = 20  # seconds
    # Define challenge duration timer
    start_time = time.time()

    # Define flags for friendly and unknown
    global targetIsUnknownFlag, targetIsFriendlyFlag

    # Define and initialize CRS output display variables
    CRS_output_display_start_time = 0
    CRS_output_display_duration = 5 # seconds 

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame was read successfully, display it
        if ret:
            
            # inference/AI mode enabled because user selected 'A'
            if AI_mode_flag:
                # Display AI mode in the lower right corner
                cv2.putText(frame, "AI Mode", (1150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
                # Calculate elapsed time for CRS
                elapsed_time = time.time() - start_time

                # Run inference on the frame
                results = model.infer(image=frame,
                                       confidence=0.5,
                                       iou_threshold=0.5)
                # Iterate through the predictions made
                for result in results:
                    if result:
                        # Extract bounding box info from result
                        bounding_box = results[0][0]
                        x0, y0, x1, y1 = map(int, bounding_box[:4])

                        # Place colored bounding boxes and labels based on the class detected
                        if bounding_box[6] == 1.0:
                            cv2.rectangle(frame, (x0, y0), (x1, y1), colors.get("US_military"), 5)
                            cv2.putText(frame, "US_military", (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                        colors.get("US_military"), 2)
                        elif bounding_box[6] == 0.0:
                            cv2.rectangle(frame, (x0, y0), (x1, y1), colors.get("RU_military"), 5)
                            cv2.putText(frame, "RU_military", (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                        colors.get("RU_military"), 2)

                # CRS mode is enabled because user selected 'C'
                if CRS_mode_flag:
                    # Start calculating the time remaining and display it on the webcam
                    CRS_timeout_remaining = CRS_duration - elapsed_time
                    elapsed_time_text = f"Time Remaining: {CRS_timeout_remaining:.2f}"
                    # Display timer in upper right corner 
                    cv2.putText(frame, elapsed_time_text, (900, 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
                    # Display CRS mode in upper left corner
                    cv2.putText(frame, "Challenge Response Activated", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

                    if (targetIsUnknownFlag or targetIsFriendlyFlag):
                        # Based on the response to the CRS server (flag setting), then change the display to show
                        # either "Friendly" or "Unknown" on the cv2 webcam stream. 
                        if targetIsFriendlyFlag:
                            text = "FRIENDLY - DO NOT SHOOT!"
                            cv2.putText(frame, text, (350, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
                        elif targetIsUnknownFlag:
                            text = "UNKNOWN - CAUTION!"
                            cv2.putText(frame, text, (350, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)

                        # Start the CRS output display timer
                        if CRS_output_display_start_time == 0:
                            CRS_output_display_start_time = time.time()
                        # calculate elapsed timer for CRS output on the webcam    
                        CRS_elapsed_time = time.time() - CRS_output_display_start_time

                        # Reset all relevant flags and timer after the specified duration
                        # Close socket since respnse was received
                        if CRS_elapsed_time > CRS_output_display_duration:
                            targetIsFriendlyFlag = False
                            targetIsUnknownFlag = False
                            CRS_output_display_start_time = 0
                            print("Kill socket because response was received")
                            CRS_mode_flag = not CRS_mode_flag
                            server_socket.close()
                    # Close socket after X number of seconds
                    # Reset CRS flag and close the server socket
                    if CRS_mode_flag and elapsed_time > CRS_duration:
                        print("Kill socket because of timeout")
                        CRS_mode_flag = not CRS_mode_flag
                        server_socket.close()  

            # Display the resulting frame
            cv2.imshow('Webcam Feed', frame)
            # Capture keypress within opencv, 30 is number of ms that opencv will wait for any key press
            key = cv2.waitKey(30)
            # If ESC key is pressed, then stop the video capture
            if key == 27:
                server_socket.close()
                break
            # If 'A' is pressed, then Inference/AI mode is enabled.
            elif key == ord('A') or key == ord('a'):
                AI_mode_flag = not AI_mode_flag
                # If CRS was enabled, then reset flag and close socket
                if CRS_mode_flag:
                    CRS_mode_flag = not CRS_mode_flag
                    server_socket.close()

            # If 'C' is pressed, then challenge response server starts up
            elif (key == ord('C') or key == ord('c')) and AI_mode_flag:
                print("CRS time..")
                # Start the server in a separate thread so webcam stream is not interrupted
                server_socket = socket.socket()
                server_thread = threading.Thread(target=serverMain, args=(server_socket,))
                server_thread.daemon = True
                server_thread.start()
                # Enable CRS
                CRS_mode_flag = not CRS_mode_flag
                # Initialize challenge duration timer
                start_time = time.time()
            # If 'F' is pressed, a friendly response will be sent to the CRS server
            elif (key == ord('F') or key == ord('f')) and CRS_mode_flag:
                CRS_clientSide_friendly.clientMain()
            # If 'U' is pressed, an "unknown" response will be sent to the CRS server
            elif (key == ord('U') or key == ord('u')) and CRS_mode_flag:
                CRS_clientSide_unknown.clientMain()

        else:
            print("Error: Could not read frame.")
            break

    # When everything is done, release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()