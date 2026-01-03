from flask import Blueprint, jsonify, render_template, request
from config.database import Session
from models import ChatSession, ChatMessage
from utils import generate_session_id
from datetime import datetime

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'ai-chatbot'
    }), 200


@main_bp.route('/api/session/create', methods=['POST'])
def create_session():
    session = Session()
    try:
        data = request.get_json() or {}
        user_id = data.get('user_id')
        
        session_id = generate_session_id()
        
        chat_session = ChatSession(
            session_id=session_id,
            user_id=user_id
        )
        
        session.add(chat_session)
        session.commit()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'created_at': chat_session.created_at.isoformat()
        }), 201
        
    except Exception as e:
        session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        session.close()


@main_bp.route('/api/chat', methods=['POST'])
def chat():
    return jsonify({
        'success': True,
        'message': 'Chat endpoint - to be implemented',
        'response': 'This endpoint will handle chat messages with LLM integration'
    }), 200


@main_bp.route('/api/sessions/<session_id>/messages', methods=['GET'])
def get_messages(session_id):
    session = Session()
    try:
        messages = session.query(ChatMessage).filter_by(
            session_id=session_id
        ).order_by(ChatMessage.timestamp).all()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'messages': [
                {
                    'id': msg.id,
                    'role': msg.role,
                    'content': msg.content,
                    'timestamp': msg.timestamp.isoformat()
                }
                for msg in messages
            ]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        session.close()
