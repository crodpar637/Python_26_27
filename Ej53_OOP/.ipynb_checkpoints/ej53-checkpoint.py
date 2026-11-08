from factory import Product, MetalPiece, PlasticPiece

m = MetalPiece("M01", 300, 12.5, "http://metal.com", "steel")
pl = PlasticPiece("PL01", 50, 3.2, "http://plastic.com", 7)

prod = Product("P001", "Desk lamp")
print(prod.add_piece(m))
print(prod.add_piece(pl))

print(prod.piece_listing())
print("Price:", prod.product_price())     # expected 15.7
print("Weight:", prod.product_weight())   # expected 350

for action in (
    lambda: MetalPiece("M2", -5, 1.0, "x", "iron"),
    lambda: MetalPiece("M3", 5, None, "x", "iron"),
    lambda: PlasticPiece("", 5, 1.0, "x", 3),
    lambda: prod.add_piece("hello"),
    lambda: m.__weight,
):
    try:
        action()
        print("NOT rejected")
    except (ValueError, TypeError, AttributeError) as e:
        print("Rejected:", e)