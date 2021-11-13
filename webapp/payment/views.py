from datetime import datetime
from flask import redirect, request, render_template, url_for, abort, flash
from flask import Blueprint
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


def get_collection(id):
    collection = Collections.query.filter_by(id=id).first()
    if collection:
        return collection
    abort(400)


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
    abort(400)


@blueprint.route('/checkout')
def checkout():
    try:
        amount = int(request.args.get('amount'))
    except(TypeError):
        abort(400)
    collection_id = request.args.get('id')
    if (amount > 0) and collection_id:
        checkout_form = CheckoutForm()
        checkout_form.amount.data = amount
        collection = get_collection(collection_id)
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
    if checkout_form.validate_on_submit:
        collection_id = checkout_form.collection_id.data
        collection = get_collection(collection_id)
        payment_label = get_label(collection_id)
        operation = get_payment_result(
            payment_label,
            checkout_form.amount.data,
            collection)
        if operation and (operation['status'] == 'success'):
            transaction = Transactions(**operation)

            db.session.add(transaction)
            db.session.commit()
            flash('Payment success')

            collection.current_amount = collection.current_amount + int(transaction.amount)
            db.session.add(collection)
            db.session.commit()

            return redirect(url_for('main.index'))
        abort(403)
    abort(400)


@blueprint.route('/fondy')
def fondy():
    try:
        amount = int(request.args.get('amount'))
    except(TypeError):
        abort(400)
    collection_id = request.args.get('id')
    if (amount > 0) and collection_id:
        api = Api(merchant_id=1396424, secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "RUB",
            "amount": amount
        }
        url = checkout.url(data).get('checkout_url')
        if url:
            return redirect(url)
        abort(404)
    abort(400)
