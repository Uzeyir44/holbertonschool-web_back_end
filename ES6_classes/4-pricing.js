import Currency from './3-currency'

export default class Price {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    get currency() {
        return this._currency;
    }

    set amount(value) {
        this._amount = value;
    }

    set currency(value) {
        this._currency = value;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency}`
    }

    convertPrice(amount, conversionRate) {
        return amount*conversionRate;
    }
}
