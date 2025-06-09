# Buy And Sell Django Project

Authors: Parhomenco Kirill, Alec Phan, Castiel Le, Nael Louis

Development of a kijiji-like website for Python course

Heroku website name:
    https://djangobns.herokuapp.com/

Admin accounts (username:pass):
    student:student
    ruhlmann:laurent
Regular accounts:
    Monty:Announcements
    and any ohter user-created

Application allows to:
    Create profile, update profile, update profile image, reset password through email.
    Create post (title, description, image, price), udate post, delete post.
    Purchase a post (transfers ownership while allowing a direct change of price)
    See all posts (sorted by date, paginated by 10 per page), sort by user's posts.

Admin page has access to:
    Posts, Users, Comments, Imagess(this is responsible for multiple added images, can't be user-added), Profiles.

INSTRUCTIONS TO LAUNCH:
    Use master branch for a local deployment, clone it and open the bns folder inside with your IDE. Requirements.txt contain all neccesary modules for the app
    Heroku-deployment-overhaul is the repo that was used for heroku deployment. IT WILL NOT WORK ON LOCAL!
    
