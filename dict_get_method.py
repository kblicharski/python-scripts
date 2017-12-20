# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    # If there is no such user_id, then the value is "there"
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
# "Hi Alice!"

print(greeting(333333))
# "Hi there!"
