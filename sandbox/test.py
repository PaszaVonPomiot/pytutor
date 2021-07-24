favourite_colours = ["red"]
hats_by_colour = {"blue": ["panama", "baseball_cap"], "red": ["sombrero", "cylinder"]}
for hat_colour in hats_by_colour:
    hats = hats_by_colour[hat_colour]
    if hat_colour in favourite_colours:
        print(hats)
