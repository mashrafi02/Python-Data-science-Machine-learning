from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import cv2
import numpy as np

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///files.db"

db = SQLAlchemy()
db.init_app(app)



class upload_file(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(100), nullable = False)
    data = db.Column(db.LargeBinary)


with app.app_context():
    db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        file = request.files['file']

        upload = upload_file(filename = file.filename, data = file.read())
        db.session.add(upload)
        db.session.commit()

        return redirect(url_for('image_processing', name=file.filename))
    return render_template('index.html', )

@app.route('/image/<name>')
def image_processing(name):
    file_data = db.session.execute(db.select(upload_file).where(upload_file.filename == name)).scalar()

    image_array = np.frombuffer(file_data.data, dtype=np.uint8)

    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return "Image processed and displayed (for local testing only)."




if __name__ == "__main__":
    app.run(debug=True)

        