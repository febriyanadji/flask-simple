from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hai <b> febri</b>, ini perubahan, semoga saja, bismillah ...'
if __name__ == '__main__':
    app.run();