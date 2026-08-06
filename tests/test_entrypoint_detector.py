from services.architecture.entrypoint_detector import EntrypointDetector

detector = EntrypointDetector(
    "repositories/langgraph"
)

entrypoints = detector.detect()

print()
print("=" * 60)
print("Entry Points")
print("=" * 60)

for entry in entrypoints:
    print("•", entry)