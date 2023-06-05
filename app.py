from flask import Flask, render_template
import serial

# Configure the serial port settings
serial_port = 'COM7'  # Replace with your serial port
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<state>')
def control(state):
    if state == 'on':
        # Send command to turn the relay on
        ser.write(b'ON\n')
    elif state == 'off':
        # Send command to turn the relay off
        ser.write(b'OFF\n')

    return state

if __name__ == '__main__':
    app.run(debug=True)
