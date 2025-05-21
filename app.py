from flask import Flask, request, jsonify  

app = Flask(__name__)  

@app.route('/approve', methods=['POST'])  
def approve_package():  
    package = request.json['package']  
    with open('approved_packages.txt', 'a') as f:  
        f.write(f"{package}\n")  
    return jsonify({"status": "approved", "package": package})  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000)  