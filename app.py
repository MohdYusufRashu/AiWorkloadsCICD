# app.py
# https://ai-workloads-cicd-ro4x.vercel.app/

from flask import Flask, request, render_template
#from google.cloud import aiplatform
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Initialize GCP AI Platform

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/mohdyusuf325/Downloads/majorproject-423008-545b126fcf7d.json"

#aiplatform.init(project="mtp-yusuf", location="us-central1")
#endpoint = aiplatform.Endpoint("5334924975969140736")

def predict_instances(instances):
    # Make predictions
    prediction = endpoint.predict(instances=instances)
    return prediction

flower_image_mapping = {
    "Iris-setosa": "static/iris-setosa.jpeg",
    "Iris-versicolor": "static/iris-versicolor.jpeg",
    "Iris-virginica": "static/iris-virginica.jpeg"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from form

        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        # Prepare instance data
        instances = [[sepal_length, sepal_width, petal_length, petal_width]]
        #data = request.form.get("data")

        # Process data (e.g., convert to list of floats)
        #instances = [[float(val) for val in data.split(",")]]
        
        # Get prediction

        data={}

        return render_template("index.html", data=data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
