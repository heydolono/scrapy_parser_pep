import csv
import datetime
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)
        self.total_count = 0

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        filename = os.path.join(
            BASE_DIR, 'results', f'status_summary_{current_time}.csv')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        rows = [[status, count] for status, count in self.status_count.items()]
        rows.append(['Total', self.total_count])
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(rows)
