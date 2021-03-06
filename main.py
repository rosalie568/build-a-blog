import webapp2
import jinja2
import os

#for database
from google.appengine.ext import db

#set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

#for database handling
class Posts(db.Model):
    title = db.StringProperty(required=True)
    blog = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

# Shows index page to link to main blog page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("index.html")
        response = t.render()
        self.response.write(response)

# Shows permalink page
class Permalink(webapp2.RequestHandler):
    def get(self, post_id):
        key = db.Key.from_path('Posts', int(post_id) )
        post = db.get(key)

        if not post:
            self.error(404)
            return

        t = jinja_env.get_template("permalink.html")
        response = t.render( post=post )
        self.response.write(response)

# Shows most recent 5 posts on BLOG
class BlogPage(webapp2.RequestHandler):
    def get(self):
        post = db.GqlQuery("Select * from Posts order by created DESC Limit 5")
        t = jinja_env.get_template("mainblog.html")
        response = t.render( post=post )
        self.response.write(response)

# Shows New Post page
class NewPost(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("newpost.html")
        response = t.render(title ="", err_title="", blog="", err_blog="")
        self.response.write(response)

    def post(self):
        title = self.request.get("title")
        blog = self.request.get("blog")
        title_bool = True
        blog_bool = True
        err_title = ""
        err_blog = ""

        if not title or title.strip() == "":
            title_bool = False
            err_title = "Need value for subject!"

        if not blog or blog.strip() == "":
            blog_bool = False
            err_blog = "Need value for blog!"

        #if both values are not empty redirect to mainblog page & store values in database
        if title_bool and blog_bool:
            post = Posts(title=title, blog=blog)
            post.put()
            self.redirect('/blog/%s' % str(post.key().id()))
        else:
            t = jinja_env.get_template("newpost.html")
            response = t.render(title=title, err_title=err_title, blog=blog, err_blog=err_blog)
            self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog/?', BlogPage),
    ('/blog/newpost', NewPost),
    ('/blog/([0-9]+)', Permalink)
], debug=True)
