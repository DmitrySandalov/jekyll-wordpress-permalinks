# jekyll-wordpress-permalinks
Jekyll - old pages redirection

Creates HTML webpages with both `<meta http-equiv="refresh"` and `<link rel="canonical" href=` for simple permalink migration.

1. Looks for post names in _posts
2. Creates folders with `wordpress_id` name
3. Puts `index.markdown` to each of created folders with HTML redirects


http://stackoverflow.com/a/19717455
