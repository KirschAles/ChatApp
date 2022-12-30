CREATE TABLE IF NOT EXISTS chat (
    chat_id SERIAL NOT NULL
);
ALTER TABLE chat ADD CONSTRAINT pk_chat PRIMARY KEY (chat_id);
CREATE TABLE IF NOT EXISTS usser (
    user_id SERIAL NOT NULL,
    username VARCHAR(40),
    password VARCHAR(40)
);
ALTER TABLE usser ADD CONSTRAINT pk_user PRIMARY KEY (user_id);

CREATE TABLE IF NOT EXISTS user_chat (
    user_id INTEGER NOT NULL,
    chat_id INTEGER NOT NULL
);
ALTER TABLE user_chat ADD CONSTRAINT pk_user_chat PRIMARY KEY (user_id, chat_id);
ALTER TABLE user_chat ADD CONSTRAINT fk_user_chat_user FOREIGN KEY (user_id)
REFERENCES usser (user_id) ON DELETE CASCADE;
ALTER TABLE user_chat ADD CONSTRAINT fk_user_chat_chat FOREIGN KEY (chat_id)
REFERENCES chat (chat_id) ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS message (
    message_id SERIAL NOT NULL,
    chat_id INTEGER NOT NULL,
    message VARCHAR(1024)
);
ALTER TABLE message ADD CONSTRAINT pk_message PRIMARY KEY (message_id);
ALTER TABLE message ADD CONSTRAINT fk_message FOREIGN KEY (chat_id)
REFERENCES chat (chat_id) ON DELETE CASCADE;