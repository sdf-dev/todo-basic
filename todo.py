def main():
    print("How many tasks would you like to get through today?")
    a = int(input())
    total = a
    todo_list = []
    check_for_input(a, total, todo_list)
    print(todo_list)


def check_for_input(a, total, todo_list):
    limiter = 0
    while limiter <= total -1:
        print(f"{a} tasks to be added to your list..")
        x = input().lower()
        todo_list.append(x)
        limiter+=1
        a-=1   

main()