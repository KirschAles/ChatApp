
INSERT_USER = '''INSERT INTO usser (user_id, username, password) VALUES (DEFAULT, '{0}', '{1}') RETURNING user_id;'''

GET_CHAT = '''SELECT sender_id, time_send, message FROM message JOIN chat USING(chat_id)
              WHERE chat_id={0} ORDER BY time_send ASC;'''
GET_USERNAME = '''SELECT username FROM usser WHERE user_id={0};'''

GET_USER_ID = '''SELECT user_id FROM usser WHERE username='{0}';'''

GET_PASSWORD = '''SELECT password FROM usser WHERE username='{0}';'''

INSERT_MESSAGE = '''INSERT INTO message (message_id, chat_id, time_send, sender_id, message)
                    VALUES (DEFAULT, {0}, NOW(), {1}, '{2}');'''
INSERT_USER_CHAT = 'INSERT INTO user_chat (user_id, chat_id) VALUES ({0}, {1});'

INSERT_CHAT = 'INSERT INTO chat (chat_id) VALUES (DEFAULT) RETURNING chat_id;'
GET_CHAT_MEMBERS = '''SELECT usser.username FROM usser JOIN user_chat USING(user_id) JOIN chat USING(chat_id)
                      WHERE chat.chat_id={0}'''

GET_MY_CHATS = '''SELECT chat_id FROM (SELECT user_id FROM usser WHERE username='{}') as users 
                    JOIN user_chat USING(user_id)'''
GET_CHAT_ID = 'SELECT chat_id FROM chat WHERE chat_id={0}'
GET_CHATS = 'SELECT * FROM chat'
GET_USERS = 'SELECT * FROM usser'
GET_MESSAGES = 'SELECT * FROM message'
GET_USER_CHATS = 'SELECT * FROM user_chat'