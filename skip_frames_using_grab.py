import cv2
import time

video_name = "video/GOT.mp4"
processing_fps = 5

video = cv2.VideoCapture(video_name)
video_fps = video.get(cv2.CAP_PROP_FPS)

if video_fps > processing_fps:
	skip_rate = round(video_fps/processing_fps)
else:
	skip_rate = 1

frame_no = 0
processed_frame_count = 0

start = time.time()
while True:
	ret = video.grab()
	if not ret:
		break
	frame_no += 1
	
	if (frame_no % skip_rate == 0):
		processed_frame_count += 1
		status, frame = video.retrieve()
		frame = cv2.resize(frame, (1280,720))
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow("Frame", frame)
		cv2.waitKey(1)

end = time.time()
print("Processing FPS (.grab() & .retrieve()): " + str(processed_frame_count/(end - start)))