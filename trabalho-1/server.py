import json
import socket
import sys
from dataclasses import dataclass
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET

import pyrqlite.dbapi2 as dbapi2

PORT = 6969
ADDR = ""


def main() -> None:
    if len(sys.argv) == 3:
        addr = sys.argv[1]
        port = int(sys.argv[2])
    else:
        addr = ADDR
        port = PORT

    db = dbapi2.connect(host="localhost", port=4001)
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

    with socket.socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((addr, port))
        sock.listen(1)
        print(f"Server listening on {addr}:{port}")

        while True:
            try:
                client_socket, addr = sock.accept()
                print(f"Client connected from {addr}")

                with client_socket as c:
                    correct_answers = 0

                    with db.cursor() as cursor:
                        cursor.execute(
                            "SELECT `prompt`, `options`, `answer` FROM `questions`;"
                        )

                        questions = [
                            Question(prompt, json.loads(options), answer)
                            for prompt, options, answer in cursor.fetchall()
                        ]

                    for q in questions:
                        msg = b"\n" + q.prompt.encode() + b"\n\n"
                        for i, o in enumerate(q.options):
                            msg += f"- {i}: {o}\n".encode()
                        msg += b"\n\n"

                        c.send(msg)

                        while True:
                            answer_string = c.recv(1024).decode(errors="ignore").strip()

                            try:
                                a = int(answer_string)
                            except ValueError as e:
                                msg = f"Invalid input: {e}\n".encode()
                                c.send(msg)
                                continue

                            if a == q.answer:
                                correct_answers += 1
                            break

                    msg = f"{correct_answers} answers were correct. "
                    if correct_answers == 0:
                        msg += "How did you answer that wrong?\n"
                    else:
                        msg += "Bye!\n"
                    msg = msg.encode() + b"\xFF"

                    c.send(msg)
                    c.close()
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
            "Qual é a capital da Itália?", ["Roma;", "Paris" "Lisboa", "Londres"], 0
        ),
    ]


if __name__ == "__main__":
    main()
