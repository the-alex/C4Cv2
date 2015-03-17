from flask import *

alt = Blueprint('alt', __name__, template_folder='templates')

@alt.route('/alt', methods=['GET'])
def alt_route():
    return render_template('alt.html')
