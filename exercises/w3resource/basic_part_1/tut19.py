prefix = "moje"
string_in = "modupsko"

string_out = string_in if string_in[:len(prefix)] == prefix else prefix + string_in

print(string_out)
