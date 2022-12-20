import instaloader
ig = instaloader.Instaloader()
db = input("Enter the instagram id: ")
ig.download_profile(db,profile_pic_only=True)
