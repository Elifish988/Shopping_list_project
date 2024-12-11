from flask import  Blueprint, request, jsonify

from app.services.product_list_service import service_add_product, service_del_product, fetch_products_by_group

bp_producer = Blueprint('bp_producer', __name__)




@bp_producer.route('/api/add_product', methods=['POST'])
def add_product():
    #צריך לקבל את הערכיפ הבאים 'product_name', 'quantity', 'user_id', 'group_id'
    data = request.get_json()
    response, status_code = service_add_product(data)
    return jsonify(response), status_code


@bp_producer.route('/api/del_product/<product_id>', methods=['POST'])
def del_product(product_id):
    response, status_code = service_del_product(product_id)
    return jsonify(response), status_code


@bp_producer.route('/api/get_products_by_group/<int:group_id>', methods=['GET'])
def get_products_by_group(group_id):
    response, status_code = fetch_products_by_group(group_id)
    return jsonify(response), status_code








