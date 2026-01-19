#include <stdio.h>
#include <string.h>

typedef struct{
    int timestamp;
    char level[8];
    char module[16];
    char message[128];
}log_entry_t;

int main(){

    return 0;
}

// Parse a single log line (use int as return type for success/failure)
int parse_line(const char *line, log_entry_t *entry) 
{
    return sscanf(line,
                  "[%d][%7[^]]][%15[^]] %[^\n]",
                  &entry->timestamp,
                  entry->level,
                  entry->module,
                  entry->message) == 4;
}

// Analyze parsed log entries (Only considering error and warning levels for the summary report)
void analyze_logs(log_entry_t *entries, int count, int *errors, int *warnings, char *last_fsm_state)
{
    *errors = 0;
    *warnings = 0;
    last_fsm_state[0] = '\0';

    for (int i = 0; i < count; i++) {
        if (strcmp(entries[i].level, "ERROR") == 0)
            (*errors)++; // Dereference pointer to increment
        else if (strcmp(entries[i].level, "WARN") == 0)
            (*warnings)++; // Dereference pointer to increment

        if (strcmp(entries[i].module, "FSM") == 0) {
            strcpy(last_fsm_state, entries[i].message);
        }
    }
}