# Function to solve Tower of Hanoi
def moveTower(height, fromPole, toPole, withPole):
    steps = []

    def moveTowerRecursive(height, fromPole, toPole, withPole):
        if height >= 1:
            moveTowerRecursive(height - 1, fromPole, withPole, toPole)
            steps.append(f"moving disk from {fromPole} to {toPole}")
            moveTowerRecursive(height - 1, withPole, toPole, fromPole)

    moveTowerRecursive(height, fromPole, toPole, withPole)
    return steps

# Run the function
for step in moveTower(3, "A", "B", "C"):
    print(step)
  
