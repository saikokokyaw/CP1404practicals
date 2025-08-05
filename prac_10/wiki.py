import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(title, sentences=3))
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
