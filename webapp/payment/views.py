from flask import redirect, Blueprint, request
from cloudipsp import Api, Checkout

blueprint = Blueprint('payment', __name__, url_prefix='/payment')


@blueprint.route('/fondy')
def fondy():
    amount = request.args.get('amount', None)
    id = request.args.get('id', None)
    if id and amount:
        api = Api(merchant_id=1396424, secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "RUB",
            "amount": amount
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)
