import re
import sqlite3


class NedbankprivatewealthPipeline:
    conn = sqlite3.connect('nedbankprivatewealth.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `nedbankprivatewealth` (
                                                                                    title varchar(100),
                                                                                    description text,
                                                                                    date text
                                                                                    )''')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            title = item['title']
            title = re.sub('"', "'", title).strip()
        except:
            title = ''
        try:
            description = item['description']
            description = re.sub('"', "'", description)
        except:
            description = ''
        try:
            date = item['date'][9:].strip()
        except:
            date = ''

        self.cursor.execute(f'''select * from nedbankprivatewealth where title = "{title}" and date = "{date}"''')
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(
                f'''insert into `nedbankprivatewealth` (`title`, `description`, `date`) values ("{title}", "{description}", "{date}")''')
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
