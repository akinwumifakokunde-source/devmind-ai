from services.architecture.framework_detector import FrameworkDetector

detector = FrameworkDetector(
    "repositories/langgraph"
)

frameworks = detector.detect()

print()
print("=" * 60)
print("Detected Frameworks")
print("=" * 60)

for framework in frameworks:
    print("•", framework)


    