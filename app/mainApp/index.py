from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.load_cates()
    products = dao.load_products(kw)

    return render_template('index.html', header="Sang Mobile", cates=cates, products=products)


if __name__ == "__main__":
    app.run(debug=True)
