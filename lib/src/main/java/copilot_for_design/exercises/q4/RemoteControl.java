package copilot_for_design.exercises.q4;

public interface RemoteControl {
    void setCommand(int slot, Command command);
    void executeCommand(int slot);
}
