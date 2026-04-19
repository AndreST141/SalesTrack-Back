from flask import Flask
from flask_cors import CORS
from routes.api import auth_bp, produto_bp, cliente_bp, venda_bp, categoria_bp, dashboard_bp

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(auth_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(venda_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 SalesTrack Backend — Controller > Service > Repository")
    print("="*60)
    print("📍 http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
