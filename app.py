from flask import Flask, jsonify

app = Flask(__name__)

# Route with claimId parameter
@app.route('/api/roofingmodel/<claim_id>', methods=['GET'])
def roofing_model(claim_id):
    # Stub implementation - returns basic response with claim_id
    # FETCH PHOTO's HERE
    # CALL THE AI MODEL HERE.
    return jsonify({
        'claim_id': claim_id,
        'status': 'success',
        'message': f'Roofing model data for claim {claim_id}',
        'data': {
            # Add your model data here
            'placeholder': 'stub data'
        }
    })

# Optional: Basic health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)