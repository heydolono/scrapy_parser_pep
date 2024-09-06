import csv
import datetime
from collections import defaultdict


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
        filename = f'results/status_summary_{current_time}.csv'
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.status_count.items():
                writer.writerow([status, count])
            writer.writerow(['Total', self.total_count])
