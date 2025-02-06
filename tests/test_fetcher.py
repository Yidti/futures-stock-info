import unittest
from app.fetcher import fetch_stock_data, fetch_futures_data

class TestFetcher(unittest.TestCase):
    def test_fetch_stock_data(self):
        data = fetch_stock_data("TSLA")
        self.assertIsNotNone(data)
        # 檢查新的 key
        self.assertIn("Open", data)
        self.assertIn("High", data)
        self.assertIn("Low", data)
        self.assertIn("Close", data)
        self.assertIn("Volume", data)

    def test_fetch_futures_data(self):
        data = fetch_futures_data("ES=F")
        self.assertIsNotNone(data)
        # 同樣檢查新的 key
        self.assertIn("Open", data)
        self.assertIn("High", data)
        self.assertIn("Low", data)
        self.assertIn("Close", data)
        self.assertIn("Volume", data)

if __name__ == '__main__':
    unittest.main()
