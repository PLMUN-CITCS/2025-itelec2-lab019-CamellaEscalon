# Function to get the student's score
def get_student_score() -> float:
    """
    This function prompts the user to input their score and ensures it is a valid number.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if score < 0 or score > 100:
                print("Please enter a score between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")

# Function to calculate the grade based on the score
def calculate_grade(score: float) -> str:
    """
    This function calculates the grade based on the score provided.
    
    Parameters:
        score (float): The score for which to calculate the grade.
        
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program flow
def main():
    score = get_student_score()  # Get the score from the user
    grade = calculate_grade(score)  # Calculate the grade
    print(f"Your Grade is: {grade}")  # Output the grade

# Run the program
if __name__ == "__main__":
    main()
