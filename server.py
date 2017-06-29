def nayta():
    cgitb.enable()
    first_name = "baba"
    last_name = "yaga"
    print("Content-type:text/html\n\n\n")

    print("<html>")

    print("<head>")

    print("<title>Hello - Second CGI Program</title>")

    print("</head>")

    print("<body>")

    print("<h2>Hello %s %s</h2>" % (first_name, last_name))

    print("</body>")

    print("</html>")
nayta()