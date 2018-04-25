
from ens import ens
from ens.registrar import Status

# Check to see which test-names were already checked
try:
    with open('Available-Names.txt', 'r') as f:
        prev_names = f.read().strip().split()
except IOError:
    text = ""
    print("No previously available names")

f = open('Available-Names.txt', 'a')
names = []

try:
    with open("test-names.txt", 'r') as test_names:
        urls = open("test-names.txt", 'r')
except OSError as e:
    raise

for line in urls:
    name = line.split('.')[0]
    # Make sure name is longer than 7 characters
    if len(name) > 7:
        if name not in prev_names:
            names.append(name)

for name in names:
    try:
        # you don't need to strip out .eth as ens.py will do it for you
        status = ens.registrar.status(name)
        # these are the possible statuses
        assert status in (
            Status.Open,
            Status.Auctioning,
            Status.Owned,
            Status.Forbidden,
            Status.Revealing,
            Status.NotYetAvailable
        )

        if status == Status.Open:
            print(name + ": Available")
            f.write(name + "\n")
        if status == Status.Auctioning:
            # I have it printing, but not writing to a file
            print(name + ": Auctioning")
            f.write(name + "\n")
        #if status == Status.Owned:
            #print(name + ": Owned")
    except:
        pass

f.close()
