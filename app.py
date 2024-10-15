from flask import Flask, request, jsonify, render_template
import random

app = Flask(_name_)


# Route to serve the frontend
@app.route("/")
def home():
    return render_template("index.html")  # This will serve your HTML page


# Route to handle the generation of the 3D model
@app.route("/generate_3d_model", methods=["POST"])
def generate_3d_model():
    data = request.json  # Get the JSON data sent from the frontend
    description = data.get("description", "")

    # Simulated 3D model generation (this is where you'd integrate actual logic)
    if description:
        # Simulate the generation of a 3D model based on the description
        model_name = f"3d_model_{random.randint(1, 1000)}.obj"  # Placeholder file
        response = {
            "status": "success",
            "message": f"3D model generated for description: '{description}'.",
            "model": model_name,
        }
    else:
        response = {"status": "error", "message": "Description is missing."}

    return jsonify(response)


if _name_ == "_main_":
    app.run(debug=True)
