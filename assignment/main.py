from pprint import pprint
from data_processing import file_reader
from data_processing import web_fetcher


url = "https://jsonplaceholder.typicode.com/users/"


if __name__ == "__main__":
    print(f"1\n{">>>"*20}")
    pprint(file_reader.read_data("data.txt"))
    print(">>>"*20)

    print(f"2\n{">>>"*20}")
    pprint(web_fetcher.fetch_user_data(url))
    print(">>>"*20)