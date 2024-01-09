import re

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
os.environ['API_KEY'] = 'https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY'

if not os.environ.get('API_KEY'):
    raise RuntimeError('API_KEY not set')


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    user_id = session['user_id']
    portfolio = db.execute('select * from portfolios where user_id = ?', user_id)
    cash_left = db.execute(
        'select cash from users where id = ?',
        user_id
        )

    if cash_left and 'cash' in cash_left[0]:
        cash_left = float(cash_left[0]['cash'])
    else:
        cash_left = 0.0
    total_amount = cash_left
    try:
        for stock in portfolio:
            symbol = stock['symbol']
            stock_info = lookup(
                symbol
                )
            current_price = float(
                stock_info['price']
                )
            stock_value = current_price * stock['shares']

            stock.update(
                {
                    'current_price': current_price, 'stock_value': stock_value
                })
            total_amount = total_amount + float(
                stock['stock_value']
                )

    except(LookupError, ValueError):
        return apology('Failed to update stock prices!')
    return render_template(
        'index.html',
        portfolio = portfolio,
        cash_left = cash_left,
        total_amount = total_amount
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':
        user_id = session['user_id']
        symbol = request.form.get('symbol')
        stock = lookup(symbol)
        shares = request.form.get('shares')
        if not symbol or not stock:
            return apology('symbol is not valid!')
        if not shares.isdigit():
            return apology('number of shares must be a positive digits.')

        user_cash = db.execute(
            'select cash from users where id = ?',
            user_id
            )
        user_cash = user_cash[0]['cash']
        transaction_value = int(shares) * stock['price']
        if user_cash < transaction_value + 1:
            return apology('not enough money!', 401)
        update_user_cash = user_cash - transaction_value
        db.execute(
            'update users set cash = ? where id = ?',
             update_user_cash,
             user_id
              )
        balance = f"${update_user_cash:,.2f} (-${transaction_value:,.2f})"

        db.execute(
            'insert into portfolios (user_id, symbol, shares) values (?, ?, ?)',
            user_id,
            symbol,
            shares,
        )

        db.execute(
            'insert into history (id, symbol, shares, price) values (?, ?, ?, ?)',
            user_id,
            symbol,
            shares,
            'BOUGHT'
        )

        flash(f'successfully bought {shares} shares of {symbol}!')
        return redirect('/')
    return render_template('buy.html')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session['user_id']
    portfolio = db.execute(
    'select * from history where id = ?',
     user_id
     )

    return render_template(
        'history.html',
        portfolio = portfolio
        )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'POST':
        stock = lookup(str(request.form.get('symbol')))
        if not stock:
            return apology('invalid symbol!')
        stock['price'] = usd(stock['price'])
        return render_template('quoted.html', stock = stock)
    return render_template('quote.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'POST':
        confirmation = request.form.get(
            'confirmation'
            )
        password = request.form.get(
            'password'
            )
        username = request.form.get(
            'username'
            )
        if any(not field for field in [username, password, confirmation]):
            return apology("Fields cannot be empty!")
        if len(username) < 4:
            return apology("Username must be at least 4 characters long!", 200)

        if len(password) < 8:
            return apology("Password must be at least 8 characters long!", 400)
        if (
            not re.search("[a-zA-Z]", password)
            or not re.search("[0-9]", password)
            or not re.search("[!@#$%^&*()]", password)
        ):
            return apology("Password must contain characters, digits and symbols!", 400)
        if password != confirmation:
            return apology("Passwords do not match!", 400)
        if len(db.execute("select * from users where username = ?", username)) > 0:
            return apology("Username already taken!", 400)
        hashed_password = generate_password_hash(password)
        db.execute(
            'insert into users (username, hash) values (?, ?)',
            username,
            hashed_password
        )
        row = db.execute(
            'select * from users where username = ?',
            username
            )
        session['user_id'] = row[0]['id']

        return redirect('/')
    return render_template('register.html')

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session['user_id']
    portfolio = db.execute(
        'select * from portfolios where user_id = ?',
        user_id
        )
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        stock = lookup(symbol)
        owned_stock = db.execute(
            'select shares from portfolios where user_id = ? and symbol = ?',
            user_id,
            symbol
        )
        shares = int(request.form.get('shares'))
        if not owned_stock:
            return apology(f"you dont't own any shares of {symbol}!")
        curernt_shares = sum([stock['shares'] for stock in owned_stock])
        if curernt_shares < shares:
            return apology("you don't have enough shares to sell!")
        current_price = stock['price']
        cash = db.execute(
                    'select cash from users where id = ?',
                    user_id
                    )
        cash = cash[0]['cash']
        cash = cash + (shares * current_price)

        for info in owned_stock:
            if info['shares'] > shares:
                db.execute(
                    'update portfolios set shares = ? where user_id = ? and symbol = ?',
                    info['shares'] - shares,
                    user_id,
                    symbol
                )
            else:
                db.execute(
                    'delete from portfolio where user_id = ? and symbol = ?',
                    user_id,
                    symbol
                )
        balance = f'${cash:,0.2f} (+${(shares * current_price):,0.2f})'
        db.execute(
            'update users set cash = ? where id = ?',
            cash,
            id
        )
        db.execute(
            'insert into history (user_id, name, symbol, shares, action, balance, date) values (?, ?, ?, ?, ?, ?, ?)',
            user_id,
            stock['name'],
            symbol,
            shares,
            'SOLD',
            balance,
            get_time()
        )
        flash(f'successfully {shares} shares of {symbol}!')
        return redirect('/')
    return render_template(
        'sell.html',
        portfolio = portfolio)

@app.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit():
    """Deposit funds to account."""
    if request.method == 'POST':

        user_id = session["user_id"]
        account = db.execute(
            'select * from users where id = ?',
             user_id)


        check_password(account[0]["hash"], request.form.get('password'))
        cash = account[0]["cash"] + amount
        db.execute(
            'update users set cash = ? where id = ?',
             cash, user_id
             )
        amount = int(request.form.get('sum'))

        flash(f'successfully added ${amount} to your balance!')
        return redirect('/')

    return render_template('deposit.html')


@app.route('/withdraw', methods=['GET', 'POST'])
@login_required
def withdraw():
    """Withdraw funds from account."""
    if request.method == 'POST':
        user_id = session['user_id']
        account = db.execute(
            'select * from users where id = ?',
             user_id
             )



        check_password(
            account[0]['hash'], request.form.get('password')
            )
        amount = int(request.form.get('sum'))

        if amount > account[0]['cash']:
            return apology(
                "can't withdraw more than cash left!"
                )

        cash = account[0]['cash'] - amount
        db.execute(
            'update users set cash = ? where id = ?',
             cash,
             user_id
             )


        flash(f'successfuly witdraw ${amount} from your balance!')
        return redirect("/")

    return render_template(
        'withdraw.html'
    )