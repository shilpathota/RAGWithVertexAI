from flask import Flask, request, jsonify, render_template
from mcp_client import summarize_chat, ask_question, upload_doc
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    chat_log = request.json.get('chat_log')
    result = summarize_chat(chat_log)
    return jsonify(result)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    result = ask_question(question)
    return jsonify(result)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    result = upload_doc(file_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
