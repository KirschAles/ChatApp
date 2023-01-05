from app.server.database.dbsql import Database


def printall(db: Database):
    print('messages')
    print(db.get_messages())
    print('chats')
    print(db.get_chats())
    print('users')
    print(db.get_users())
    print('user_chats')
    print(db.get_user_chats())


def test_run():
    db = Database()
    printall(db)
    db.insert_user('hovno', 'honva')
    db.insert_user('al', 'nal')
    printall(db)
    chat_id = db.insert_chat([1, 2])
    print('chat id: ')
    print(chat_id)
    printall(db)
    assert True
