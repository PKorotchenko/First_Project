from flask import Flask, render_template, request, redirect, url_for
from models import PriceTracker

app = Flask(__name__)
tracker = PriceTracker()

@app.route('/')
def index():
    stores = tracker.get_stores()
    items = tracker.get_food_items()
    return render_template('index.html', stores=stores, items=items)

@app.route('/add_store', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        tracker.add_store(name, location)
        return redirect(url_for('index'))
    return render_template('add_store.html')

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    stores = tracker.get_stores()
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        store_id = int(request.form['store_id'])
        tracker.add_food_item(name, price, store_id)
        return redirect(url_for('index'))
    return render_template('add_item.html', stores=stores)

@app.route('/average_price', methods=['GET', 'POST'])
def average_price():
    if request.method == 'POST':
        item_name = request.form['item_name']
        avg_price = tracker.get_average_price(item_name)
        return render_template('average_price.html', item_name=item_name, avg_price=avg_price)
    return render_template('average_price.html')

if __name__ == '__main__':
    app.run(debug=True)