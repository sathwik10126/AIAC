def get_student_score(student_scores, student_name):
    """
    Retrieve the score of a student from the dictionary.

    Args:
        student_scores (dict): A dictionary with student names as keys and their scores as values.
        student_name (str): The name of the student whose score is to be retrieved.

    Returns:
        int or str: The score of the student if found, otherwise "Not Found".
    """
    return student_scores.get(student_name, "Not Found")

# Example usage
student_scores = {"Alice": 85, "Bob": 90}
print(get_student_score(student_scores, "Charlie"))