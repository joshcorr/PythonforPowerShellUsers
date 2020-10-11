# if elif else
val = 4
if val == 5:
    # space characters are critical for
    # python interpreter
    print("This is something")
elif val == 3:
    print("Don't nest IF")
else:
    print("Default")

# Ternary flow control, i.e. one line if/else
val = 3
"something" if val is (None or '') else val