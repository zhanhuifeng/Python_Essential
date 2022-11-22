import pickle

a1 = "Felix"
a2 = 1985
a3 = [2022, 2023, 2024]

with open("data.dat", "wb") as f:
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)

with open("data.dat", "rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)

    print(b1)
    print(b2)
    print(b3)

    print(id(a1), id(b1))
    print(id(a2), id(b2))
    print(id(a3), id(b3))
    # The content before serialize and after unserialize is same, but IDs are different.
