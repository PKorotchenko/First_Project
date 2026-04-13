from flask import Flask, render_template, request, redirect, url_for
from models import PriceTracker
from datetime import date, datetime

app = Flask(__name__)
tracker = PriceTracker()

@app.route('/')
def index():
    stores = tracker.get_stores()
    selected_store_id = request.args.get('store_id', type=int)
    selected_item_name = request.args.get('item_name', default=None, type=str)
    if selected_item_name == '':
        selected_item_name = None
    food_names = tracker.get_food_names()
    chart_item_name = selected_item_name or (food_names[0] if food_names else None)
    items = tracker.get_food_items(store_id=selected_store_id, item_name=selected_item_name)
    selected_store_name = None
    if selected_store_id:
        selected_store_name = next((store[1] for store in stores if store[0] == selected_store_id), None)
    history = None
    if chart_item_name:
        history = tracker.get_price_history(chart_item_name, store_id=selected_store_id)
    return render_template(
        'index.html',
        stores=stores,
        items=items,
        food_names=food_names,
        selected_store_id=selected_store_id,
        selected_item_name=selected_item_name,
        selected_store_name=selected_store_name,
        history=history,
        chart_item_name=chart_item_name,
    )

@app.route('/add_store', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        latitude = request.form.get('latitude') or None
        longitude = request.form.get('longitude') or None
        latitude = float(latitude) if latitude else None
        longitude = float(longitude) if longitude else None
        tracker.add_store(name, location, latitude, longitude)
        return redirect(url_for('index'))
    return render_template('add_store.html')

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    stores = tracker.get_stores()
    current_date = date.today().isoformat()
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        store_id = int(request.form['store_id'])
        date_recorded = request.form.get('date_recorded') or current_date
        tracker.add_food_item(name, price, store_id, date_recorded)
        return redirect(url_for('index'))
    return render_template('add_item.html', stores=stores, current_date=current_date)

@app.route('/average_price', methods=['GET', 'POST'])
def average_price():
    item_name = None
    avg_price = None
    if request.method == 'POST':
        item_name = request.form['item_name']
        avg_price = tracker.get_average_price(item_name)
    return render_template('average_price.html', item_name=item_name, avg_price=avg_price)

if __name__ == '__main__':
    app.run(debug=True)