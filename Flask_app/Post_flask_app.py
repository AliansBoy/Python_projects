from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post'
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')    #/post/0
def post(post_id):
    post_get = posts.get(post_id)
    if not post_get:   #post will be None if not found; not None => True
        return render_template('404.html', message=f'A post with ID {post_id} was not found')
    # return f"Post: {post['title']}, content:\n\n{post['content']}"
    return render_template('post.html', post=post_get)

#While we get 'GET' method to creat function, we can delete this function
# @app.route('/post/form')
# def form():
#     return render_template('create.html')


@app.route('/post/create', methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'post_id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
