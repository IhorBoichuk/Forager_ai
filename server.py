from flask import Flask, render_template, request, jsonify
from storage import ResultStorage
from config import API_KEY, BASE_URL
from forms import EmailForm, DomainForm
from handlers import Email_Verifier_Handler, Domain_Search_Handler
from services import MyApiClient
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

storage: ResultStorage = ResultStorage()
api_client: MyApiClient = MyApiClient(BASE_URL, API_KEY)

@app.route('/email_verify', methods=['GET', 'POST'])
def email_verify():
    """
    Handles the email verification process.

    - Accepts POST requests with an email form.
    - Calls the Email_Verifier_Handler to verify the email.
    - Stores the result in the ResultStorage.
    - Returns the result as JSON.

    :return: JSON response with the verification result.
    """
    form: EmailForm = EmailForm()
    if form.validate_on_submit():
        email: str = form.email.data
        result: dict = Email_Verifier_Handler(api_client).execute(email)
        storage.create_result(email, result)
        return jsonify(result), 201

    return render_template('email_verify.html', form=form)

@app.route('/domain_search', methods=['GET', 'POST'])
def domain_search():
    """
    Handles the domain search process.

    - Accepts POST requests with a domain form.
    - Calls the Domain_Search_Handler to find domain.
    - Stores the result in the ResultStorage.
    - Returns the result as JSON.

    :return: JSON response with the verification result.
    """
    form: DomainForm = DomainForm()
    if form.validate_on_submit():
        domain: str = form.domain.data  # Updated variable name to 'domain'
        result: dict = Domain_Search_Handler(api_client).execute(domain)
        storage.create_result(domain, result)
        return jsonify(result), 201

    return render_template('domain_search.html', form=form)


@app.route('/email_verify/results/<key>', methods=['GET'])
def email_read_result(key: str):
    """
    Reads the result associated with the given key from ResultStorage.

    :param key: The key for the result.

    :return: JSON response with the result or a message if not found.
    """
    result: dict = storage.read_result(key)
    if result:
        return jsonify(result)
    return jsonify({'message': 'Result not found'}), 404

@app.route('/domain_search/results/<key>', methods=['GET'])
def domain_read_result(key: str):
    """
    Reads the result associated with the given key from ResultStorage.

    :param key: The key for the result.

    :return: JSON response with the result or a message if not found.
    """
    result: dict = storage.read_result(key)
    if result:
        return jsonify(result)
    return jsonify({'message': 'Result not found'}), 404

@app.route('/email_verify/update_results/<key>', methods=['PUT'])
def email_update_result(key: str):
    """
    Updates the result associated with the given key in ResultStorage.

    - Accepts PUT requests with a JSON payload containing 'new_value'.
    - Calls storage.update_result to update the result.

    :param key: The key for the result.

    :return: JSON response with a success or error message.
    """
    data: dict = request.get_json()
    new_value: any = data.get('new_value')
    if storage.update_result(key, new_value):
        return jsonify({'message': 'Result updated successfully'})
    return jsonify({'message': 'Result not found'}), 404

@app.route('/domain_search/update_results/<key>', methods=['PUT'])
def domain_update_result(key: str):
    """
    Updates the result associated with the given key in ResultStorage.

    - Accepts PUT requests with a JSON payload containing 'new_value'.
    - Calls storage.update_result to update the result.

    :param key: The key for the result.

    :return: JSON response with a success or error message.
    """
    data: dict = request.get_json()
    new_value: any = data.get('new_value')
    if storage.update_result(key, new_value):
        return jsonify({'message': 'Result updated successfully'})
    return jsonify({'message': 'Result not found'}), 404

@app.route('/email_verify/delete_results/<key>', methods=['DELETE'])
def email_delete_result(key: str):
    """
    Deletes the result associated with the given key from ResultStorage.

    :param key: The key for the result.

    :return: JSON response with a success or error message.
    """
    if storage.delete_result(key):
        return jsonify({'message': 'Result deleted successfully'})
    return jsonify({'message': 'Result not found'}), 404

@app.route('/domain_search/delete_results/<key>', methods=['DELETE'])
def domain_delete_result(key: str):
    """
    Deletes the result associated with the given key from ResultStorage.

    :param key: The key for the result.

    :return: JSON response with a success or error message.
    """
    if storage.delete_result(key):
        return jsonify({'message': 'Result deleted successfully'})
    return jsonify({'message': 'Result not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

