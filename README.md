
# Vidyo assignment

A brief description of what this project does and who it's for


## Installation

Install my-project with npm

```bash
  git clone
  cd Vidyo_assignment
  pip install -r requirements.txt
```
Creating database
```bash
python3 createdb.py
```
Running flask app
```bash
python app.py
```

The api endpoint will be started at port 5000

## Sending/using service
```bash
# for extracting audio from video
curl -X POST http://localhost:5000/convert-video-to-audio -H "Content-Type: multipart/form-data" -F "video_file=@test.mp4" -H "username: test_user" -o uploaded_video.mp3

# For adding watermark to the video video_file
curl -X POST http://localhost:5001/watermark -H "Content-Type: multipart/form-data" -F "video_file=@test.mp4" -F "logo_file=@logo.jpg" -F "location_choice=right" -H "username: test_user" -o uploaded_video.mp4
```
## System Architecture Overview
![architecture_design drawio](https://github.com/chiragbiradar/PyMediaProcessor/assets/78417411/3db2441c-c349-4304-9dc7-f5d0dc4502d7)


The API follows a robust and scalable architecture to handle user requests for processing video files. The workflow is orchestrated through multiple components, ensuring efficient handling and processing of user requests.

1. **User Interaction:**
   - Users submit video files through the API endpoint.
   - Initial contact is made with the API Gateway.

2. **Gateway Processing:**
   - The Gateway receives the video file and acts as the entry point to the system.
   - It stores the video file in MongoDB, ensuring secure and reliable data persistence.

3. **Queue Messaging:**
   - After storing the video in MongoDB, a message is enqueued in RabbitMQ.
   - The message contains information about the video, indicating the required service (audio extraction or watermarking).

4. **Service Execution:**
   - Specialized services (Audio Extractor or Watermarking) subscribe to the RabbitMQ queue.
   - Upon receiving a message, the service extracts the video ID from the message and retrieves the corresponding video file from MongoDB.
   - The specified service is applied to the video, and the resulting output is stored back in MongoDB.

5. **Notification Handling:**
   - Once the processing is complete, another message is placed on the RabbitMQ queue for the Notification Service.
   - The Notification Service picks up the message, retrieves the necessary information, and sends an email to the user, notifying them that the requested task is finished.

6. **Authorization:**
   - Users are required to send a JWT token, obtained through email, for authentication.
   - The token, secured with the HS256 algorithm, is validated before providing access to the processed output.

7. **User Retrieval:**
   - Authenticated users can retrieve their processed video files directly through the API.

**Benefits of the Architecture:**
- **Scalability:** Each service operates independently, allowing for horizontal scaling to meet increasing demand.
- **Reliability:** Data persistence in MongoDB ensures robustness, while message queuing enables reliable communication between components.
- **Security:** JWT authentication safeguards access to processed files, maintaining a secure user experience.
- **Asynchronous Processing:** The use of queues enables asynchronous processing, improving system responsiveness.

This architecture ensures a seamless and efficient workflow, providing users with a reliable and secure video processing experience.
