from flask import Flask, render_template
from flask.ext.socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

messages=[]

@app.route('/')
def index():
    return app.send_static_file('index.html')

@socketio.on('connect',namespace='/chat')
def makeConnection():
    print "Connected"

    for message in messages:
        print message
        emit('message',message)


@socketio.on('message',namespace='/chat')
def new_message(message,name):
    tmp={'text':message,'name':name}
    print ('\n\n'+ tmp['name']+' said: '+tmp['text']+'\n\n')
    messages.append(tmp)
    emit('message',tmp,broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
