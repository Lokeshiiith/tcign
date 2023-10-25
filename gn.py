import streamlit as st
import datetime
# Title and description
# st.title("How manufacturing companies like GN Enterprises dont pay attention to their customers")
st.title("How shipment companies like tci express cheat their customers and not deliver on time")

# add image of orders
st.image("gn.jpg", use_column_width=True)
# Date of actions

# Show order details
st.subheader("Order Details")
st.write("Full money given to dealer on: 10th Oct")
st.write("Ordered on: 10th Oct")
st.write("Dealer dispatched on: 10th Oct")
st.write("Reached nearest location on: 13th Oct")

# Get today's date
today = datetime.date.today()
# Format the date string
formatted_date = today.strftime("%B %d")
# Show the current date
st.write(f"Today is {formatted_date}th")

st.image("tci.jpg", use_column_width=True)

st.markdown("""
**Order Delay and Unresponsiveness:**

* **Dealer Unresponsive:** Mr. Rajesh Bhatia, our designated dealer, is unresponsive and has ceased taking our calls despite multiple attempts to reach him.

* **Shipment Issue:** TCI Express, the logistics provider, informed us that the initial booking was processed for a lesser amount, causing delivery issues.

* **Delayed Delivery:** The order was scheduled for delivery on October 17th, but as of October 25th, it has not reached its destination.

* **Financial Penalty:** The delay has resulted in a penalty of 10,000 rupees.

* **Lack of Resolution:** Neither the dealer nor TCI Express is responding to our concerns, leaving us without a resolution.

We urgently request assistance in resolving this matter and ensuring the prompt delivery of our order.
""")
st.markdown("[TCI Express Tracking](https://www.tciexpress.in/trackingdocket.aspx?trackshipment=455914675&dwb=dwb)")

 
st.write('All website through which gn enterprise is selling their products')
st.markdown("[GN Enterprise](https://www.gnenterprise.co.in/profile.html)")
st.markdown("[GN Playground Equipment](https://www.gnplaygroundequipment.in/search/rajesh-bhatia/1)")