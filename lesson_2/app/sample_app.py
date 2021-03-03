from lesson_2.app.config import load_config


def app():
    config = load_config("dev")

if __name__ == '__main__':
    app()
