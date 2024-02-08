class Buyer:
    def __init__(self, budget):
        self.budget = budget
    
    def make_offer(self):
        return self.budget

class Seller:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    
    def respond_to_offer(self, offer):
        if offer >= self.product_price * 0.9:  # Seller will not sell below 90% of the product price
            return "accept"
        elif offer >= self.product_price:  # Buyer buys instantly if offer is higher or equal to product price
            return "instant_buy"
        else:
            return "counteroffer"

def main():
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price: "))

    buyer_budget = int(input("Enter buyer's budget: "))
    buyer = Buyer(buyer_budget)
    seller = Seller(product_name, product_price)

    print(f"Buyer's budget: ${buyer.budget}")
    print(f"Seller's product: {seller.product_name} - ${seller.product_price}")

    while True:
        buyer_offer = buyer.make_offer()
        print(f"Buyer offers: ${buyer_offer}")

        response = seller.respond_to_offer(buyer_offer)
        if response == "accept":
            print("Seller accepts the offer. Transaction completed!")
            break
        elif response == "instant_buy":
            print("Buyer instantly buys the product!")
            break
        else:
            print("Seller makes a counteroffer.")

            new_price = int(input("Enter counteroffer price: "))
            seller.product_price = new_price

            print(f"Seller's new product price: ${seller.product_price}")

if __name__ == "__main__":
    main()
