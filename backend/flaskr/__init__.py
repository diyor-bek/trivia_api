import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = {category.id: category.type for category in Category.query.all()}
        return jsonify({
            'success': True,
            'categories': categories
        })


    @app.route('/categories/<int:category_id>/questions')
    def get_category_questions(category_id):
        page = request.args.get('page', 1, type=int)
        questions = [question.format() for question in Question.query.filter_by(category=category_id).all()]
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        selection = questions[start:end]
        if len(selection) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'questions': selection,
            'total_questions': len(questions),
            'current_category': category_id
        })

    @app.route('/questions', methods=['GET'])
    def get_questions():
        page = request.args.get('page', 1, type=int)
        questions = [question.format() for question in Question.query.order_by(Question.id).all()]
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        selection = questions[start:end]
        if len(selection) == 0:
            abort(404)
        categories = {category.id: category.type for category in Category.query.all()}
        return jsonify({
            'success': True,
            'questions': selection,
            'total_questions': len(questions),
            'categories': categories
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.get(question_id)
        if question is None:
            abort(404)
        question.delete()
        return jsonify({
            'success': True
        })

    @app.route('/questions', methods=['POST'])
    def post_questions():
        question = request.get_json().get('question', '')
        answer = request.get_json().get('answer', '')
        difficulty = request.get_json().get('difficulty', 0)
        category = request.get_json().get('category', 0)
        search_term = request.get_json().get('searchTerm', '')

        try:
            if question and answer and difficulty and category:
                new_question = Question(question, answer, category, difficulty)
                new_question.insert()
                return jsonify({
                    'success': True
                })
            elif search_term:
                questions = [question.format() for question in Question.query.order_by(Question.id).all() if search_term.lower() in question.question]
                return jsonify({
                    'success': True,
                    'questions': questions
                })
            else:
                abort(400)
        except:
            abort(400)

    @app.route('/quizzes', methods=['POST'])
    def post_quizzes():
        previous_questions = request.get_json().get('previous_questions')
        quiz_category = request.get_json().get('quiz_category')

        if quiz_category['id'] == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(category=quiz_category['id']).all()

        questions = [question.format() for question in questions]
        random.shuffle(questions)

        if len(questions) <= len(previous_questions):
            return jsonify({'success': True})

        while questions[len(previous_questions)]['id'] in previous_questions:
            random.shuffle(questions)

        return jsonify({
            'question': questions[len(previous_questions)]
        })
        
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 400,
            'message': 'bad request'
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 404,
            'message': 'not found'
        }), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'error': 422,
            'message': 'unprocessable'
        }), 422
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'error': 500,
            'message': 'server error'
        }), 500
    
    return app

        