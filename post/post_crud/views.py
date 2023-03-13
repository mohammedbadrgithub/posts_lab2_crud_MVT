from flask import render_template,redirect,url_for,request
from post.models import Post,Category
from post.post_crud import  post_blueprint
from post.models import  db
from werkzeug.utils import secure_filename
import os

@post_blueprint.route('/', endpoint='posts_all')
def all_Posts():
    posts = Post.query.all()
    return render_template('showPosts.html', posts=posts)


@post_blueprint.route('/posts/<id>', endpoint='post_details')
def post_info(id):
    post = Post.query.get_or_404(id)
    return render_template('showSpcificPost.html', post=post)

@post_blueprint.route('/posts/<id>/delete', endpoint='post_delete')
def post_delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')




@post_blueprint.route('/edit/<int:id>/', methods=('GET', 'POST'),endpoint="edit")
def edit(id):
    post=Post.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        description = request.form['description']
        # image=request.files['image']
        post.title=title
        post.body=body
        post.description= description
        # post.image= image
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('UpdatePost.html',post=post)



@post_blueprint.route('/addnewpost', methods = ['POST','GET'],endpoint="addnewpost")
def addNewPost():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        description = request.form['description']
        category = request.form['category']

        # image = request.files['image']
        # filename=secure_filename(image.filename)
        # image.save(os.path.join('static/images', filename))
        record = Post(title=title,
                          body=body,
                          description=description,category_id=category) 
        
        db.session.add(record)
        db.session.commit()
        return redirect('/')
    return render_template("addPost.html",category=Category.query.all())
  

@post_blueprint.route('/addnewcategory', methods = ['POST','GET'],endpoint="addnewcategory")
def addNewCategory():
    if request.method == 'POST':
        category = request.form['name']
        record = Category(cateoryName=category)
        db.session.add(record)
        db.session.commit()
        return redirect('/')
    return render_template("addCategory.html")













