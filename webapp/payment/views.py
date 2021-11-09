from datetime import datetime
from flask import redirect, Blueprint, request, render_template, url_for, abort
from flask_login import current_user
from cloudipsp import Api, Checkout
import uuid
from webapp.payment.models import Transactions
from webapp.payment.forms import CheckoutForm
from webapp.collect.models import Collections
from webapp import db


blueprint = Blueprint('payment', __name__, url_prefix='/payment')


def get_label(id):
    return "{}-{}".format(id, uuid.uuid4().hex)


def get_payment_result(payment_label, amount, collection):
    if payment_label and amount == 666:
        return {
            'operation_id': uuid.uuid4().hex,
            'collections_id': collection.id,
            'status': 'failed',
            'datetime': datetime.now(),
            'title': collection.collection_name,
            'pattern_id': collection.id,
            'direction': 'None',
            'amount': '{}'.format(amount),
            'label': payment_label,
            'type': 'mixedcard'
        }
    elif payment_label and amount != 666:
        return {
            'operation_id': uuid.uuid4().hex,
            'collections_id': collection.id,
            'status': 'success',
            'datetime': datetime.now(),
            'title': collection.collection_name,
            'pattern_id': collection.id,
            'direction': 'None',
            'amount': '{}'.format(amount),
            'label': payment_label,
            'type': 'mixedcard'
        }


@blueprint.route('/checkout')
def checkout():
    amount = request.args.get('amount')
    collection_id = request.args.get('id')
    if (amount > 0) and collection_id:
        checkout_form = CheckoutForm()
        checkout_form.amount.data = amount
        collection = Collections.query.filter_by(id=collection_id).first()
        checkout_form.collection_id.data = collection_id
        checkout_form.collection_name.data = collection.collection_name
        title = "Подтвердить перевод"
        return render_template(
            'payment/checkout.html',
            page_title=title,
            form=checkout_form,
            current_user=current_user)
    abort(400)


@blueprint.route('/procces_pay', methods=['POST'])
def procces_pay():
    checkout_form = CheckoutForm()
    if checkout_form:
        collection_id = checkout_form.collection_id.data
        collection = Collections.query.filter_by(id=collection_id).first()
        payment_label = get_label(collection_id)
        operation = get_payment_result(
                payment_label,
                checkout_form.amount.data,
                collection
                )
        if operation['status'] == 'success':
            transaction = Transactions(**operation)

            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for('main.index'))
        abort(400)
    abort(400)


@blueprint.route('/fondy')
def fondy():
    amount = request.args.get('amount')
    id = request.args.get('id')
    if id and amount:
        api = Api(merchant_id=1396424, secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "RUB",
            "amount": amount
        }
        url = checkout.url(data).get('checkout_url')
        return redirect(url)
