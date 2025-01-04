def main():
    tasks = []

    while True:
        print("\n===== Lista de Tarefas =====")
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        print("3. Marcar Tarefa como Feita")
        print("4. Sair")

        choice = input("Insira sua escolha: ")

        if choice == '1':
            print()
            n_tasks = int(input("Quantas tarefas você deseja adicionar?: "))
            
            for i in range(n_tasks):
                task = input("Insira sua Tarefa: ")
                tasks.append({"Tarefa": task, "Feito": False})
                print("Tarefa Adicionada!")

        elif choice == '2':
            print("\nTarefas:")
            for index, task in enumerate(tasks):
                status = "Feito" if task["Feito"] else "Não feito"
                print(f"{index + 1}. {task['Tarefa']} - {status}")

        elif choice == '3':
            task_index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Feito"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número de tarefa inválido.")

        elif choice == '4':
            print("Saindo da lista de tarefas.")
            break

        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()