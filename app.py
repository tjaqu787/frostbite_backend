from flask import Flask, jsonify
from models.load_model import load_and_predict
from models.load_pictures import load_pictures

app = Flask(__name__)

# Load model once at startup (not on every request)
try:
    model = load_and_predict()
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Route with claimId parameter
@app.route('/api/roofingmodel/<claim_id>', methods=['GET'])
def roofing_model(claim_id):
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({
                'claim_id': claim_id,
                'status': 'error',
                'message': 'Model not loaded',
                'data': None
            }), 500
        
        # Load pictures for this specific claim
        # Note: You probably want to pass claim_id to load_pictures
        pictures = load_pictures(claim_id)  # Assuming you'll modify this to accept claim_id
        
        # Process all pictures and collect predictions
        predictions = []
        for picture in pictures:
            try:
                prediction = model.predict(picture)
                predictions.append({
                    'image_id': picture.get('id', 'unknown'),
                    'prediction': prediction
                })
            except Exception as e:
                predictions.append({
                    'image_id': picture.get('id', 'unknown'),
                    'error': str(e)
                })
        
        return jsonify({
            'claim_id': claim_id,
            'status': 'success',
            'message': f'Roofing model data for claim {claim_id}',
            'data': {
                'predictions': predictions,
                'total_images': len(pictures),
                'successful_predictions': len([p for p in predictions if 'prediction' in p])
            }
        })
    
    except Exception as e:
        return jsonify({
            'claim_id': claim_id,
            'status': 'error',
            'message': str(e),
            'data': None
        }), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

# Optional: Route to test model without pictures
@app.route('/test-model', methods=['GET'])
def test_model():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    # Add test logic here
    return jsonify({'status': 'Model is working'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)