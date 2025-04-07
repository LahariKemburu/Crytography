
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class ToDoList {
    private static List<Task> tasks = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n--- To-Do List ---");
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task as Done");
            System.out.println("4. Delete Task");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1:
                    addTask();
                    break;
                case 2:
                    viewTasks();
                    break;
                case 3:
                    markTaskAsDone();
                    break;
                case 4:
                    deleteTask();
                    break;
                case 5:
                    System.out.println("Exiting... Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 5);
    }

    private static void addTask() {
        System.out.print("Enter task name: ");
        String taskName = scanner.nextLine();

        System.out.print("Enter deadline (dd-MM-yyyy HH:mm): ");
        String deadlineStr = scanner.nextLine();
        LocalDateTime deadline;
        try {
            deadline = LocalDateTime.parse(deadlineStr, DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm"));
        } catch (Exception e) {
            System.out.println("Invalid date/time format. Task not added.");
            return;
        }

        System.out.print("Enter priority (1 = High, 2 = Medium, 3 = Low, 0 = None): ");
        int priority = scanner.nextInt();
        if (priority < 0 || priority > 3) {
            priority = 0;
        }
        scanner.nextLine(); // Consume newline

        Task task = new Task(taskName, deadline, priority);
        tasks.add(task);
        System.out.println("Task added successfully.");
    }

    private static void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }

        // Sort tasks by priority and deadline
        tasks.sort(Comparator
                .comparingInt(Task::getPriority)  // Sort by priority (ascending)
                .thenComparing(Task::getDeadline) // If priority is same, sort by deadline
        );

        System.out.println("\nYour Tasks (Sorted by Priority and Deadline):");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

    private static void markTaskAsDone() {
        viewTasks();
        if (tasks.isEmpty()) return;

        System.out.print("Enter task number to mark as done: ");
        int taskNumber = scanner.nextInt();
        if (taskNumber > 0 && taskNumber <= tasks.size()) {
            tasks.get(taskNumber - 1).markAsDone();
            System.out.println("Task marked as done.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private static void deleteTask() {
        viewTasks();
        if (tasks.isEmpty()) return;

        System.out.print("Enter task number to delete: ");
        int taskNumber = scanner.nextInt();
        if (taskNumber > 0 && taskNumber <= tasks.size()) {
            tasks.remove(taskNumber - 1);
            System.out.println("Task deleted successfully.");
        } else {
            System.out.println("Invalid task number.");
        }
    }
}

