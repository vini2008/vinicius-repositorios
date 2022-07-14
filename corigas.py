
# SOLID - Single Resonsibility
def funcao(*args, timeout=10, **options):
    for item in  args:
        print(item)

    print(options)

    print(f"timeout {timeout}")


funcao("Bruno",1,True,[],timeout=99, nome="Janaina", cidade="carapicuiba", idade=91)


