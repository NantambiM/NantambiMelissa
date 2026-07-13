class VotingEligibilityError(Exception):
    # Raised when a person is not eligible to vote.
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise VotingEligibilityError("You must be at least 18 years old to vote in Uganda.")

    print("You are eligible to vote.")

except VotingEligibilityError as e:
    print(e)
except ValueError:
    print("Please enter a valid whole number.")
finally:
    print('Thank you for participating in the voting eligibility check!')