from flask import Blueprint, request, jsonify
from .transcription import transcribe_audio

bp=Blueprint('routes', __name__)

@bp.route("/transcribe",methods=["POST"])
def transcribe():
    file = request.flies["file"]
    transcript=transcribe_audio(file)
    return jsonify({"transcript": transcript})

@bp.route("/", methods=["GET"])
def home():
    return "✅ Flask backend is running!"
