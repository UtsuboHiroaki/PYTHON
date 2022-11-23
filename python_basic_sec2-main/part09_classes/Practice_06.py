class Metal:
    asset_type = '貴金属'

    def __init__(self, type_name, base_price, weight):
        self.type_name = type_name
        self.total_weight = weight
        self.total_price = base_price * weight

silver = Metal('silver', 2000, 100)
platinum = Metal('platinum', 3000, 50)

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

platinum.asset_type = 'プラチナ'

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

Metal.asset_type = '地金'

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)
print(platinum.__class__.asset_type)