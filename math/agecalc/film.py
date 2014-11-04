print("The Film Quiz")

print("Which is first Disney movie to use CGI?")
answer = input().strip()

if answer.startswith('tron'):
    print("Correct!")
elif answer.startswith('matrix'):
    print('Clever but wrong.')
else:
    print("Incorrect!")
