from flask import Blueprint, jsonify

main=Blueprint('herr_blueprint',__name__)

@main.route('/')
def get_herrms():
    return jsonify({'message':"Josec"})