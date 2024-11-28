from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/myAPI', methods=['GET'])
def myAPI():
    """
    API endpoint that greets the user with a birthday message if the current date matches their birthday.

    Query Parameters:
        name (str): The name of the user.
        bday (int): The user's birthday in MMDD format (e.g., 1127 for November 27).

    Returns:
        JSON: A greeting message.
    """
    name = request.args.get('name')
    bday = request.args.get('bday')

    # Validate the input
    if not name or not bday:
        return jsonify({"error": "Missing 'name' or 'bday' query parameter"}), 400

    try:
        bday = int(bday)
    except ValueError:
        return jsonify({"error": "'bday' must be an integer in MMDD format"}), 400

    # Get the current month and day
    current_month = datetime.now().month
    current_date = datetime.now().day

    # Combine into MMDD format
    current_mmdd = int(f"{current_month:02}{current_date:02}")

    # Generate the greeting
    if current_mmdd == bday:
        message = f"Happy birthday, {name}"
    else:
        message = f"Hi {name}"

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=False,port=8080)
