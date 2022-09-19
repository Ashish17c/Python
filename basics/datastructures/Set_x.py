from xml.sax.handler import all_features


dry_fruits={"dates","almond","walnut","cashew"}
fruits = {"apple","Banana","Apple","Orange"}

all_features = dry_fruits | fruits

print(all_features)
print(fruits)
print(dry_fruits)

ans = dry_fruits.isdisjoint(fruits)
print(ans)

ans = dry_fruits.issubset(all_features)
print(ans)

ans = fruits.issuperset({'apple','banana'})
print(ans)