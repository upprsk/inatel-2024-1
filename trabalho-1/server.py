import json
import socket
import sys
from dataclasses import dataclass
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET

import pyrqlite.dbapi2 as dbapi2

# Default port and address
PORT = 6969
ADDR = ""


def main() -> None:
    # Just in case...
    if any(s == "--help" for s in sys.argv):
        print(f"usage: {sys.argv[0]} <addr> <port>")
        sys.exit(0)

    # Use defaults if nothing is given
    if len(sys.argv) == 3:
        addr = sys.argv[1]
        port = int(sys.argv[2])
    else:
        addr = ADDR
        port = PORT

    # Connect to the database
    db = dbapi2.connect(host="localhost", port=4001)

    # Drop and re-create the table
    with db.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS questions;")
        cursor.execute(
            """\
CREATE TABLE IF NOT EXISTS questions (
    id      INTEGER NOT NULL PRIMARY KEY,
    prompt  TEXT,
    options TEXT,
    answer  INTEGER
);"""
        )

        qs = get_questions()
        for i, q in enumerate(qs):
            cursor.execute(
                "INSERT INTO questions(id, prompt, options, answer) VALUES(?, ?, ?, ?)",
                parameters=(i, q.prompt, json.dumps(q.options), q.answer),
            )

    # Open our listening socket
    with socket.socket(AF_INET, SOCK_STREAM) as sock:
        # make fast restarts work
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        sock.bind((addr, port))
        sock.listen(5)  # backlog of 5
        print(f"Server listening on {addr}:{port}")

        while True:
            try:
                client_socket, addr = sock.accept()
                print(f"Client connected from {addr}")

                with client_socket as c:
                    # Store all of the answers and if they are correct
                    answers: list[tuple[int, bool]] = []

                    # Get all of the questions from the database
                    with db.cursor() as cursor:
                        cursor.execute(
                            "SELECT `prompt`, `options`, `answer` FROM `questions`;"
                        )

                        questions = [
                            Question(prompt, json.loads(options), answer)
                            for prompt, options, answer in cursor.fetchall()
                        ]

                    for i, q in enumerate(questions):
                        msg = b"\n" + q.prompt.encode() + b"\n\n"
                        for i, o in enumerate(q.options):
                            msg += f"- {i}: {o}\n".encode()
                        msg += b"\n\n"

                        # Send the question
                        c.send(msg)

                        while True:
                            # Get the answer and repeat if invalid
                            answer_string = c.recv(1024).decode(errors="ignore").strip()

                            try:
                                a = int(answer_string)
                            except ValueError as e:
                                msg = f"Invalid input: {e}\n".encode()
                                c.send(msg)
                                continue

                            answers.append((i, a == q.answer))
                            break

                    # process the response and show info
                    msg = f"{len([ok for _, ok in answers if ok])} answers were correct.\n"
                    for i, ((ans, ok), q) in enumerate(zip(answers, questions)):
                        msg += f"Question {i}: {'correct' if ok else 'wrong'}\n"
                        if not ok:
                            msg += f"\tgiven: {q.options[ans]}\n"
                        msg += f"\tanswer: {q.options[q.answer]}\n"

                    if answers == 0:
                        msg += "How did you answer that wrong?\n"
                    else:
                        msg += "Bye!\n"

                    # use the code `0xFF` to exit the client when last send goes
                    msg = msg.encode() + b"\xFF"

                    c.send(msg)  # send the stats
                print("Client disconnected")
            except BrokenPipeError as e:
                print(f"Client disconnected: {e}")


@dataclass
class Question:
    prompt: str
    options: list[str]
    answer: int


def get_questions() -> list[Question]:
    return [
        Question("What is the magic number?", ["69", "4294967296" "420", "0"], 1),
        Question(
            "Qual é a capital da Itália?", ["Roma", "Paris" "Lisboa", "Londres"], 0
        ),
    ]


if __name__ == "__main__":
    main()
