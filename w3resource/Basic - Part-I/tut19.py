prefix = "moje"
string_in = "modupsko"

if string_in[:len(prefix)] == prefix:
    string_out = string_in
else:
    string_out = prefix + string_in

print(string_out)
