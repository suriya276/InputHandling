# from flask import Flask, request, jsonify
# import os

# app = Flask(__name__)

# @app.route('/api/process', methods=['POST'])
# def process():
#     # Get JSON data from the request
#     data = request.get_json()

#     # Extract the 'input' value
#     input_value = data.get('input')
#     if not input_value:
#         return jsonify({'error': 'Missing "input" in request'}), 400

#     # Reverse the input string
#     output_value = input_value[::-1]

#     # Save the output to a file
#     os.makedirs('outputs', exist_ok=True)
#     with open('outputs/result.txt', 'w') as f:
#         f.write(output_value)

#     # Return the output as JSON
#     return jsonify({'output': output_value})

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5001, debug=True)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process():
    # Get JSON data from the request
    data = request.get_json()

    # Extract the 'input' value
    input_value = data.get('input')
    if not input_value:
        return jsonify({'error': 'Missing "input" in request'}), 400

    # Reverse the input string
    output_value = input_value[::-1]

    # Save the output to a file
    os.makedirs('outputs', exist_ok=True)
    with open('outputs/result.txt', 'w') as f:
        f.write(output_value)

    # Return the output in the API response
    return jsonify({
        'input': input_value,
        'output': output_value,
        'message': 'Output successfully generated and saved.'
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
