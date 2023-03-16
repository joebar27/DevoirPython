from flask import Flask, render_template
from SettingsPC import SettingsPC
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():

    settings = SettingsPC()

    print(json.dumps(settings.get_os_info(), indent=4))

    return render_template('settings.html', settings=settings.get_os_info())

if __name__ == '__main__':
    app.run(debug=False)