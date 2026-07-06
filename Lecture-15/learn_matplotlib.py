import matplotlib
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]

# plt.plot(x, y)
# plt.show()


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
patients = [12, 18, 25, 20, 30]

plt.plot(days, patients, marker="o")

plt.title("Weekly Patient Report")
plt.xlabel("Days")
plt.ylabel("Number of Patients")

plt.grid(True)
plt.show()

