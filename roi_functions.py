# ===============================
# ROI FUNCTIONS
# ===============================

def calculate_roi(price, annual_rent, annual_expenses):
    net_profit = annual_rent - annual_expenses
    roi = (net_profit / price) * 100
    return roi, net_profit


def payback_period(price, annual_profit):
    if annual_profit <= 0:
        return None
    return price / annual_profit


def investment_rating(roi):
    if roi > 15:
        return "Excellent"
    elif roi > 8:
        return "Good"
    else:
        return "Risky"


def monthly_cashflow(annual_rent, annual_expenses):
    return (annual_rent - annual_expenses) / 12


# ===============================
# DYNAMIC RENT ESTIMATION
# ===============================
def estimate_rent(price, location):
    location_yield = {
        "Banana Island": 0.05,
        "Ikoyi": 0.06,
        "Victoria Island": 0.065,
        "Lekki": 0.08,
        "Ajah": 0.10,
        "Yaba": 0.085,
        "Ikeja": 0.075
    }

    yield_rate = location_yield.get(location, 0.08)
    return price * yield_rate


# ===============================
# INVESTMENT INSIGHT
# ===============================
def investment_insight(roi):
    if roi >= 12:
        return "💰 Strong Cashflow Investment (High rental returns)"
    elif roi >= 7:
        return "⚖️ Balanced Investment (Income + Appreciation)"
    else:
        return "🏡 Luxury / Appreciation Investment (Lower ROI, long-term value)"