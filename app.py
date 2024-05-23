from flask import Flask, request, jsonify
from flasgger import Swagger
from clustering import cluster_data  # Assuming your clustering code is in clustering.py

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def index():
    return "Welcome to the Clustering API!"


@app.route("/cluster", methods=["POST"])
def cluster():
    """
    Cluster data using KMeans
    ---
    tags:
      - clustering
    parameters:
      - name: data
        in: body
        type: array
        items:
          type: number
        required: true
        description: List of data points to cluster
    responses:
      200:
        description: Clustered data
        schema:
          id: Cluster
          properties:
            labels:
              type: array
              items:
                type: integer
              description: Cluster labels for each data point
    """
    data = request.get_json().get("data")
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        labels = cluster_data(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(labels=labels.tolist())


if __name__ == "__main__":
    app.run(debug=True)
