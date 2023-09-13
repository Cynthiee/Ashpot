with open('the_zen_of_python.txt') as f:
    contents = f.read()
    # print(contents)


    with open('the_zen_of_python.txt') as f:
     [print(line) for line in f.readlines()]


     with open('the_zen_of_python.txt') as f:
        [print(line.strip()) for line in f.readlines()]


        with open('the_zen_of_python.txt') as f:
            while True:
               line = f.readline()
        if not line:
            print(line.strip())


            with open('the_zen_of_python.txt') as f:
                for line in f:
                   print(line.strip())