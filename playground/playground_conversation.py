from services.memory.conversation_manager import ConversationManager

def print_history(session_id: str, manager: ConversationManager):
    """
    Print the conversation history for a session
    """
    
    history = manager.get_history(session_id)
    
    print("\n" + "=" * 80)
    print(f"SESSION : {session_id}")
    print("=" * 80)

    if not history.messages:

        print("No messages.")

        return
    
    for index,message in enumerate(history.messages, start=1):
        
        print(f"\nMessage {index}")

        print(f"Role      : {message.role}")

        print(f"Time      : {message.timestamp}")

        print(f"Content   : {message.content}")
    
def main():
        
    manager = ConversationManager()
    
    session_1 = "user_1"
    
    session_2 = "user_2"
    
    # ==================================================
    # Session 1
    # ==================================================

    manager.add_user_message(
        session_1,
        "What causes breast cancer?"
    )

    manager.add_assistant_message(
        session_1,
        "Breast cancer has multiple risk factors..."
    )

    manager.add_user_message(
        session_1,
        "What are its symptoms?"
    )

    # ==================================================
    # Session 2
    # ==================================================

    manager.add_user_message(
        session_2,
        "What causes diabetes?"
    )

    manager.add_assistant_message(
        session_2,
        "Diabetes develops due to..."
    )

    # ==================================================
    # Print histories
    # ==================================================

    print_history(
        session_1,
        manager
    )

    print_history(
        session_2,
        manager
    )

    # ==================================================
    # Clear session 1
    # ==================================================

    manager.clear(session_1)

    print("\n")
    print("=" * 80)
    print("AFTER CLEARING SESSION 1")
    print("=" * 80)

    print_history(
        session_1,
        manager
    )

    print_history(
        session_2,
        manager
    )


if __name__ == "__main__":
    main()
        