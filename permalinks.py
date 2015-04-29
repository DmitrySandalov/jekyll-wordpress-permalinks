import os
import glob


template = \
    """---
layout: null
---
<html>
    <head>
        <meta http-equiv="refresh" content="0; url={{{{ site.baseurl }}}}{{% post_url {0} %}}">
        <link rel="canonical" href="{{{{ site.baseurl }}}}{{% post_url {0} %}}" />
    </head>
</html>
"""


os.chdir("/tmp/blog/_posts")
for post in glob.glob("*.markdown"):
    wp_id = [line[14:-1] for line in open(post) if 'wordpress_id:' in line][0]
    if not os.path.exists(wp_id):
        os.makedirs(wp_id)
    with open(wp_id + '/index.markdown', 'w') as the_file:
        the_file.write(template.format(post))
        print "[post]: {0} -> {1}".format(post, wp_id)
