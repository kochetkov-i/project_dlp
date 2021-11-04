from flask import redirect, Blueprint, request
from cloudipsp import Api, Checkout
from yoomoney import Client, Quickpay
from webapp.config import Config
import uuid
from webapp.payment.models import Transactions
from webapp import db


blueprint = Blueprint('payment', __name__, url_prefix='/payment')


def get_label(id):
    return "{}-{}".format(id, uuid.uuid4().hex)


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


@blueprint.route('/yoomoney')
def yoomoney():
    client = Client(Config.YOOTOKEN)
    user = client.account_info()
    print("Account number:", user.account)
    amount = request.args.get('amount', None)
    id = request.args.get('id', None)
    if id and amount:
        quickpay = Quickpay(
            receiver=user.account,
            quickpay_form="shop",
            targets="Sponsor this project",
            paymentType="SB",
            sum=amount,
            label=get_label(id)
            )
        return redirect(quickpay.redirected_url)


def yoomoney_check(payment_label):
    client = Client(Config.YOOTOKEN)
    operation = client.operation_history(label=payment_label).first()
    if operation.status == '':
        transaction = Transactions(
            operation_id=operation.operation_id,
            status=operation.status,
            datetime=operation.datetime,
            title=operation.title,
            pattern_id=operation.pattern_id,
            direction=operation.direction,
            amount=operation.amount,
            label=operation.label,
            type=operation.type
        )

        db.session.add(transaction)
        db.session.commit()
