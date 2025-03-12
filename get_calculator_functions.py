def get_student_score() -> float:

    while True:
        try:
            score = float(input("Enter your score: "))
            if score < 0 or score > 100:
                print("Please enter a score between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")


def calculate_grade(score: float) -> str:
   
    
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


def main():
    score = get_student_score()  
    grade = calculate_grade(score)  
    print(f"Your Grade is: {grade}")  

if __name__ == "__main__":
    main()
 