from collections import deque
from typing import Deque

# Create a deque to represent the queue at the ticket counter
# will discart the oldest person if the queue is full
ticket_queue: Deque[str] = deque(maxlen=3)


# Function to add a person to the queue
def arrive(person):
    ticket_queue.append(person)

    print(f"{person} arrived. Queue: {list(ticket_queue)}")


# Function to serve a person from the queue
def serve():
    if ticket_queue:
        person = ticket_queue.popleft()
        print(f"{person} served. Queue: {list(ticket_queue)}")
    else:
        print("No one to serve. Queue is empty.")


arrive("Alice")
arrive("Bob")
arrive("Charlie")
arrive("David")

serve()
serve()
serve()
serve()
