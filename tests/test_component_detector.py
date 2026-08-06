from services.architecture.component_detector import ComponentDetector

detector = ComponentDetector(
    "repositories/langgraph"
)

components = detector.detect()

print()

print("=" * 60)
print("Detected Components")
print("=" * 60)

for component, folders in components.items():

    print()

    print(component.upper())

    for folder in folders:
        print("  •", folder)