# string_methods.py

def main():
    # 1. capitalize()
    result_1 = "hello world".capitalize()

    # 2. casefold()
    result_2 = "HeLLo".casefold()

    # 3. center()
    result_3 = "Hello".center(10, "-")

    # 4. count()
    result_4 = "hello hello".count("hello")

    # 5. encode()
    result_5 = "hello".encode("utf-8")

    # 6. endswith()
    result_6 = "hello.txt".endswith(".txt")

    # 7. expandtabs()
    result_7 = "hello\tworld".expandtabs(4)

    # 8. find()
    result_8 = "hello world".find("world")

    # 9. format()
    result_9 = "My name is {} and I am {} years old".format("Alice", 30)

    # 10. index()
    result_10 = "hello world".index("world")

    # 11. isalnum()
    result_11 = "hello123".isalnum()

    # 12. isalpha()
    result_12 = "hello".isalpha()

    # 13. isdigit()
    result_13 = "123".isdigit()

    # 14. islower()
    result_14 = "hello".islower()

    # 15. isupper()
    result_15 = "HELLO".isupper()

    # 16. isspace()
    result_16 = "   ".isspace()

    # 17. istitle()
    result_17 = "Hello World".istitle()

    # 18. isnumeric()
    result_18 = "123".isnumeric()

    # 19. join()
    result_19 = " ".join(["hello", "world"])

    # Print results
    print("1. capitalize():", result_1)
    print("2. casefold():", result_2)
    print("3. center():", result_3)
    print("4. count():", result_4)
    print("5. encode():", result_5)
    print("6. endswith():", result_6)
    print("7. expandtabs():", result_7)
    print("8. find():", result_8)
    print("9. format():", result_9)
    print("10. index():", result_10)
    print("11. isalnum():", result_11)
    print("12. isalpha():", result_12)
    print("13. isdigit():", result_13)
    print("14. islower():", result_14)
    print("15. isupper():", result_15)
    print("16. isspace():", result_16)
    print("17. istitle():", result_17)
    print("18. isnumeric():", result_18)
    print("19. join():", result_19)

if __name__ == "__main__":
    main()
