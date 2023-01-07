from app.server.database.dbsql import Database


def printall(database: Database):
    print('messages')
    print(database.get_messages())
    print('chats')
    print(database.get_chats())
    print('users')
    print(database.get_users())
    print('user_chats')
    print(database.get_user_chats())


db = Database()


class TestDbsql:
    def test_empty(self):
        assert db.get_messages() == []
        assert db.get_chats() == []
        assert db.get_users() == []
        assert db.get_user_chats() == []

    def test_users(self):

        db.insert_user('user', 'user')
        assert db.get_users() == [(1, 'user', 'user')]
        db.insert_user('ěščřžýáíé', 'ěščřžýáíé')
        assert db.get_users() == [(1, 'user', 'user'), (2, 'ěščřžýáíé', 'ěščřžýáíé')]
        db.insert_user('ahoj', 'nope')
        db.insert_user('noo', 'nah')
        assert db.get_users() == [(1, 'user', 'user'),
                                  (2, 'ěščřžýáíé', 'ěščřžýáíé'),
                                  (3, 'ahoj', 'nope'),
                                  (4, 'noo', 'nah')]

    def test_single_user(self):
        try:
            db.get_user_id('nonexistent')
            assert False
        except ValueError:
            pass

        try:
            assert db.get_username(35) is None
            assert False
        except ValueError:
            pass
        try:
            assert db.get_username(-256) is None
            assert False
        except ValueError:
            pass

        assert db.get_username(1) == 'user'
        assert db.get_username(2) == 'ěščřžýáíé'
        assert db.get_user_id('user') == 1

    def test_run(self):
        printall(db)
        user1 = 'man1'
        user2 = 'man2'
        db.insert_user(user1, 'honva')
        db.insert_user(user2, 'nal')
        printall(db)
        chat_id = db.insert_chat(user1)
        db.insert_user_chat(user2, chat_id)
        print('chat id: ')
        print(chat_id)
        printall(db)

        db.insert_message(chat_id=chat_id, sender_id=db.get_user_id(user1), message='Ahoj1')
        db.insert_message(chat_id=chat_id, sender_id=db.get_user_id(user2), message='ho2')
        print(db.get_chat(chat_id=chat_id))
        printall(db)
        assert True
