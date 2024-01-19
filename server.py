"""
server.py.

This module provides server.
"""
import secrets

from flask import Flask, jsonify, render_template, request

from config import API_KEY, BASE_URL
from forms import DomainForm, EmailForm
from handlers import DomainSearchHandler, EmailVerifierHandler
from services import MyApiClient
from storage import ResultStorage

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

storage: ResultStorage = ResultStorage()
api_client: MyApiClient = MyApiClient(BASE_URL, API_KEY)


@app.route('/email_verify', methods=['GET', 'POST'])
def email_verify():
    """
    Handle the email verification process.

    - Accepts POST requests with an email form.
    - Calls the Email_Verifier_Handler to verify the email.
    - Stores the result in the ResultStorage.
    - Returns the result as JSON.

    Returns:
        JSON response with the verification result.
    """
    form: EmailForm = EmailForm()
    if form.validate_on_submit():
        email: str = form.email.data
        request_result: dict = EmailVerifierHandler(api_client).execute(email)
        storage.create_result(email, request_result)
        return jsonify(request_result), 201

    return render_template('email_verify.html', form=form)


@app.route('/domain_search', methods=['GET', 'POST'])
def domain_search():
    """
    Handle the domain search process.

    - Accepts POST requests with a domain form.
    - Calls the Domain_Search_Handler to find domain.
    - Stores the result in the ResultStorage.
    - Returns the result as JSON.

    Returns:
        JSON response with the verification result.
    """
    form: DomainForm = DomainForm()
    if form.validate_on_submit():
        domain: str = form.domain.data  # Updated variable name to 'domain'
        request_result: dict = DomainSearchHandler(api_client).execute(domain)
        storage.create_result(domain, request_result)
        return jsonify(request_result), 201

    return render_template('domain_search.html', form=form)


@app.route('/email_verify/results/<key>', methods=['GET'])
def email_read_result(key: str):
    """
    Read the result associated with the given key from ResultStorage.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with the result or a message if not found.
    """
    request_result: dict = storage.read_result(key)
    if request_result:
        return jsonify(request_result)
    return jsonify({'message': 'Result not found'}), 404


@app.route('/domain_search/results/<key>', methods=['GET'])
def domain_read_result(key: str):
    """
    Read the result associated with the given key from ResultStorage.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with the result or a message if not found.
    """
    request_result: dict = storage.read_result(key)
    if request_result:
        return jsonify(request_result)
    return jsonify({'message': 'Result not found'}), 404


@app.route('/email_verify/update_results/<key>', methods=['PUT'])
def email_update_result(key: str):
    """
    Update the result associated with the given key in ResultStorage.

    - Accepts PUT requests with a JSON payload containing 'new_value'.
    - Calls storage.update_result to update the result.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with a success or error message.
    """
    request_data: dict = request.get_json()
    new_value: any = request_data.get('new_value')
    if storage.update_result(key, new_value):
        return jsonify({'message': 'Result updated successfully'})
    return jsonify({'message': 'Result not found'}), 404


@app.route('/domain_search/update_results/<key>', methods=['PUT'])
def domain_update_result(key: str):
    """
    Update the result associated with the given key in ResultStorage.

    - Accepts PUT requests with a JSON payload containing 'new_value'.
    - Calls storage.update_result to update the result.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with a success or error message.
    """
    request_data: dict = request.get_json()
    new_value: any = request_data.get('new_value')
    if storage.update_result(key, new_value):
        return jsonify({'message': 'Result updated successfully'})
    return jsonify({'message': 'Result not found'}), 404


@app.route('/email_verify/delete_results/<key>', methods=['DELETE'])
def email_delete_result(key: str):
    """
    Delete the result associated with the given key from ResultStorage.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with a success or error message.
    """
    if storage.delete_result(key):
        return jsonify({'message': 'Result deleted successfully'})
    return jsonify({'message': 'Result not found'}), 404


@app.route('/domain_search/delete_results/<key>', methods=['DELETE'])
def domain_delete_result(key: str):
    """
    Delete the result associated with the given key from ResultStorage.

    Parameters:
        key: The key for the result.

    Returns:
        JSON response with a success or error message.
    """
    if storage.delete_result(key):
        return jsonify({'message': 'Result deleted successfully'})
    return jsonify({'message': 'Result not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
