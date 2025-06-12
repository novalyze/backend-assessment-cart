# run.py
from app import create_app

if __name__ == "__main__":
    # ensure .env is read
    from dotenv import load_dotenv

    load_dotenv()

    app = create_app()
    app.run(host="0.0.0.0", port=3003, debug=True)
