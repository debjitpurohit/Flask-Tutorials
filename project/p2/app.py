from flask import Flask ,  render_template, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0) # use 0 for web camera

def generate_frmaes():
    while True: #for continuous stream/reading
        success , frame= camera.read()
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_detector = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces = detector.detectMultiScale(frame,1.1,7)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                roi_gray = frame[y:y+h,x:x+w]
                roi_color = frame[y:y+h,x:x+w]
                eyes = eye_detector.detectMultiScale(roi_gray,1.1,7)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frmaes() , mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)