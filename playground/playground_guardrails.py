from services.guardrails.guardrail_service import GuardrailService


def print_result(question, result):

    print("\n" + "=" * 80)

    print(f"Question : {question}")

    print(f"Allowed  : {result.allowed}")

    print(f"Reason   : {result.reason}")


def main():

    guardrail = GuardrailService()

    print("=" * 80)
    print("GUARDRAIL PLAYGROUND")
    print("=" * 80)

    while True:

        question = input("\nQuestion (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        result = guardrail.validate(question)

        print_result(question, result)


if __name__ == "__main__":
    main()