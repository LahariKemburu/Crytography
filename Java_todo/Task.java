
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Task {
    private String taskName;
    private LocalDateTime deadline;
    private int priority; // 0 = None, 1 = High, 2 = Medium, 3 = Low
    private boolean isDone;

    // Constructor
    public Task(String taskName, LocalDateTime deadline, int priority) {
        this.taskName = taskName;
        this.deadline = deadline;
        this.priority = priority;
        this.isDone = false;
    }

    public String getTaskName() {
        return taskName;
    }

    public LocalDateTime getDeadline() {
        return deadline;
    }

    public int getPriority() {
        return priority;
    }

    public boolean isDone() {
        return isDone;
    }

    public void markAsDone() {
        isDone = !(isDone);
    }

    @Override
    public String toString() {
        String status = isDone ? "[✓]" : "[ ]";
        String priorityStr = (priority == 0) ? "None" : String.valueOf(priority);
        String deadlineStr = deadline.format(DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm"));
        return status + " " + taskName + " | Deadline: " + deadlineStr + " | Priority: " + priorityStr;
    }
}
