    This simple blog site was built on the basis Harrison Kinsley`s video tutorial 
    (you can watch it here https://www.youtube.com/user/sentdex/videos)

    I have added base API functions via Django Rest Framework,
    they can be used at - site/api/blog  (list of posts)
                        - site/api/blog/post_id (post create,edit, 
                                                    detail view, delete).
    Only authorized users can manipulate via api functions, except list view and detail view of posts.
    It runs as standard on the Django`s test server
    Please, run python manage.py migrate --run-syncdb before first start.
    Django admin interface can be used to add posts to the blog.
