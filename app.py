from flask import Flask, render_template, request

app = Flask(__name__)

bookings = []

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        source = request.form["source"]
        destination = request.form["destination"]
        date = request.form["date"]
        flight_class = request.form["flight_class"]
        passengers = int(request.form["passengers"])

        # Base Price
        price = 5000

        if flight_class == "Business":
            price = 9000

        elif flight_class == "First":
            price = 15000

        total = price * passengers

        booking = {
            "name": name,
            "email": email,
            "source": source,
            "destination": destination,
            "date": date,
            "class": flight_class,
            "passengers": passengers,
            "total": total
        }

        bookings.append(booking)

        message = f"Booking Successful! Total Ticket Price = ₹{total}"

    return render_template(
        "index.html",
        bookings=bookings,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)