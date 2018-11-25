types_of_people = 10
x = f"There are {types_of_people} of people"

binary = "binary"
do_not = "Don't"
y = f'Those who have {binary} and those who have not {do_not}'

print(x)
print(y)

print(f"I said : {x}")
print(f'I also said: {y}')

hilarious = False

joke_evaluation = "Isn't that jooke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of....."
e = "a string with right side."

print(w+e)
