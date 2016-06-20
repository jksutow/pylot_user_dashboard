from system.core.model import Model


class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
        # Put queries in dictionary incase we want to use again
        self.queries = {
            'create_message': "INSERT INTO messages (user_id, author_id, message, created_at, updated_at) VALUES (:user_id, :author_id, :message, NOW(), NOW())",
            'create_comment': "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())",
            'fetch_messages_and_comments_by_user_id': "SELECT messages.id as message_id, messages.message, users.id as user_id, users2.name as message_author, group_concat(comments.comment SEPARATOR '----') as msg_comments, group_concat(users3.name SEPARATOR '----') as comment_author FROM messages LEFT JOIN users ON users.id = messages.user_id LEFT JOIN users AS users2 ON users2.id = messages.author_id LEFT JOIN comments ON comments.message_id = messages.id LEFT JOIN users AS users3 ON users3.id = comments.user_id WHERE users.id = :id GROUP BY messages.id"
        }

    def create_message(self, form_data, author_id):
        query = self.queries['create_message']
        data = {
            'user_id': form_data['user_id'],
            'author_id': author_id,
            'message': form_data['message']
        }
        result = self.db.query_db(query, data)
        return result

    def create_comment(self, form_data, user_id):
        query = self.queries['create_comment']
        data = {
            'user_id': user_id,
            'message_id': form_data['message_id'],
            'comment': form_data['comment']
        }
        result = self.db.query_db(query, data)
        return result

    def fetch_messages_by_user_id(self, id):
        query = self.queries['fetch_messages_and_comments_by_user_id']
        data = {
            'id': id
        }
        messages = self.db.query_db(query, data)

        for message in messages:
            if message['msg_comments']:
                message['msg_comments'] = message['msg_comments'].split('----')
                message['comment_author'] = message['comment_author'].split('----')
            else:
                message['msg_comments'] = []

        return messages
