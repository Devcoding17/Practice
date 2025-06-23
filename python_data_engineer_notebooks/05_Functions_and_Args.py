# Functions, *args, **kwargs
def add_all(*args):
    return sum(args)

def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print(add_all(1, 2, 3))
show_info(name="Dev", role="Data Engineer")