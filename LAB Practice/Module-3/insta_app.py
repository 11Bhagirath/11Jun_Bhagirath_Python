import instaloader 

instaID=input("Enter Any Instagram: ")

insta=instaloader.Instaloader()

insta.download_profile(instaID)
