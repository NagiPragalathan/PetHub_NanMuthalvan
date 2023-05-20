import ibm_db

# Assuming you have established a valid DB connection
conn =  ibm_db.connect("database=bludb;hostname=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; port=30426; uid = gtp43134;password = WrqarQrbVYVcaCA8;security =SSL;sslcertificate = SSL_Certificate.crt ","","")

# Create the User table
stmt_user = """
    CREATE TABLE "user" (
        id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
        username VARCHAR(100) NOT NULL,
        profile_pic VARCHAR(255),
        bio VARCHAR(160),
        cover VARCHAR(255),
        PRIMARY KEY (id)
    )
"""
ibm_db.exec_immediate(conn, stmt_user)

print("DB one created......")

# Create the Post table
stmt_post = """
    CREATE TABLE post (
        id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
        creater_id INTEGER NOT NULL,
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        content_text VARCHAR(140),
        content_image VARCHAR(255),
        comment_count INTEGER DEFAULT 0,
        PRIMARY KEY (id),
        FOREIGN KEY (creater_id) REFERENCES "user" (id)
    )
"""
ibm_db.exec_immediate(conn, stmt_post)

print("DB 2 created......")


# Create the Comment table
stmt_comment = """
    CREATE TABLE comment (
        id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
        post_id INTEGER NOT NULL,
        commenter_id INTEGER NOT NULL,
        comment_content VARCHAR(90),
        comment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (post_id) REFERENCES post (id),
        FOREIGN KEY (commenter_id) REFERENCES "user" (id)
    )
"""
ibm_db.exec_immediate(conn, stmt_comment)

print("DB 3 created......")


# Create the Follower table
stmt_follower = """
    CREATE TABLE follower (
        id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES "user" (id)
    )
"""
ibm_db.exec_immediate(conn, stmt_follower)

# Create the ManyToMany relationship tables
print("DB 4 created......")

# Likers
stmt_likers = """
    CREATE TABLE post_likers (
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (post_id) REFERENCES post (id),
        FOREIGN KEY (user_id) REFERENCES "user" (id),
        PRIMARY KEY (post_id, user_id)
    )
"""
ibm_db.exec_immediate(conn, stmt_likers)
print("DB 5 created......")

# Savers
stmt_savers = """
    CREATE TABLE post_savers (
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (post_id) REFERENCES post (id),
        FOREIGN KEY (user_id) REFERENCES "user" (id),
        PRIMARY KEY (post_id, user_id)
    )
"""
ibm_db.exec_immediate(conn, stmt_savers)
print("DB 6 created......")

# Close the DB connection
ibm_db.close(conn)
