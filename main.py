from badge import make_badge

print("🏷️ README Badge Maker")
print("=" * 35)

label = input("Badge label: ").strip()
message = input("Badge message: ").strip()

badge = make_badge(label, message)

print("\n📋 Markdown:")
print(badge)
