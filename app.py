from flask import Flask, request

app = Flask(__name__)

USD = 12236.74 # 1 USD = 11380.7 UZS

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    r=request.args
    amount=r.get('amount')
    uzs=float(amount)/USD
    return {
        "amount": f"{amount} USD",
        "currency": "UZS",
        "converted": round(float(uzs), max(6-amount.count('0'),2)),
        "convertedCurrency": "USD"
    }

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    r=request.args
    amount=r.get('amount')
    usd=float(amount)*USD
    return {
        "amount": amount,
        "currency": "UZS",
        "converted": round(float(usd), max(6-amount.count('0'),2)),
        "convertedCurrency": "USD"
    }
    

if __name__ == '__main__':
    app.run(port=5000,debug=True)