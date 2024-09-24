success = True
for num in range(3):
    print(f"attempting {num}")
    if success:
        print("we did it")
        # break
else:
    print("we tried and tried and tried and failed.")
print("outside the loop")
print(range(3))
