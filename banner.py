print("=============================")
print("             Banner          ")
print("             By Gage         ")
print("=============================")
print("")

def banner(title, author):
    title_length = len(title)
    banner_length = title_length + 8
    byline = f"By {author}"
    print("===================================")
    print(f"{title}         ")
    print(f"              By {author}      ")
    print("===================================")
    banner_length = title_length + 8
    print("")

banner("sub to my youtube channel Gamerman", "Gage")