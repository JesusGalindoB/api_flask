from flask import jsonify 

def bad_request(message="Invalid request"):
    return jsonify({
        "success": False,
        "data": {},
        "message": message,
        "status_code": 400
        }, 400)


def not_found():
    return jsonify({
            "success": False, 
            "data": {},
            "messages": "Resource not found.",
            "status_code": 404
        }, 404)


def response(data):
    return jsonify({
            "success": True, 
            "data": data 
        }), 200