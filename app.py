from flask import Flask, request, jsonify, render_template
from models import session, User, MBTIDescription

app = Flask(__name__)

compatibility = {
            'INTJ': 'ESFJ',
            'INTP': 'ESFP',
            'ENTJ': 'ISFJ',
            'ENTP': 'ISFP',
            'INFJ': 'ESTJ',
            'ENFJ': 'ISTJ',
            'INFP': 'ESTP',
            'INFP': 'ESTP',
            'ENFP': 'ISTP',
            'ISTJ': 'ENFJ',
            'ISFJ': 'ENTJ',
            'ESTJ': 'INFJ',
            'ESFJ': 'INTJ',
            'ESTP': 'INFP',
            'ISTP': 'ENFP',
            'ISFP': 'ENTP',
            'ESFP': 'INTP'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/good_relationship')
def good():
    return render_template('good.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    mbti = request.form['mbti']
    new_user = User(name=name, mbti=mbti)
    session.add(new_user)
    session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        mbti_description = session.query(MBTIDescription).filter_by(mbti=user.mbti).first()
        return jsonify({'name': user.name, 'mbti': user.mbti, 'description': mbti_description.description})
    return jsonify({'message': 'User not found'})

@app.route('/compatibility_data')
def compatibility_data():
    data = {}
    for type, best_match in compatibility.items():
        users = session.query(User).filter_by(mbti=type).all()
        data[type] = {'best_match': best_match, 'users': [user.name for user in users]}
    return jsonify(data)

# @app.route('/compatibility/<mbti_type>')
# def compatibility(mbti_type):
#     compatibilities = session.query(Compatibility).filter(or_(Compatibility.mbti_type1==mbti_type, Compatibility.mbti_type2==mbti_type)).all()
#     compatible_types = []
#     for compatibility in compatibilities:
#         if compatibility.mbti_type1 == mbti_type:
#             compatible_types.append(compatibility.mbti_type2)
#         else:
#             compatible_types.append(compatibility.mbti_type1)
#     return render_template('compatibility.html', mbti_type=mbti_type, compatible_types=compatible_types)


if __name__ == '__main__':
    app.run(debug=True)

