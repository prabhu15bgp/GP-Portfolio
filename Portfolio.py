import webbrowser
import os
import re
#Styles and scripting for the page

main_page_head='''
<head>
<meta charset="utf-8">
<title>Portfolio</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content='''
<!DOCTYPE html>
<html lang="en">
<body>
<header>Random wishes to all of you !</header>
</body>
</html>
'''

def create_html_page():
    # The HTML content for this section of the page
    output_file = open('Portfolio.html','w')
    output_file.write(main_page_head + main_page_content)
    output_file.close()

    # Open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)


create_html_page() 
