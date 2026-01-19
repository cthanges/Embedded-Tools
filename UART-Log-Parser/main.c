#include <stdio.h>
#include <string.h>

#define MAX_LOGS 100

typedef struct{
    int timestamp;
    char level[8];
    char module[16];
    char message[128];
}log_entry_t;

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

int main(int argc, char *argv[])
{
    FILE *pFile = fopen("sample_logs.txt", "r");
    if (pFile == NULL) {
        printf("ERROR: Could not open file.\n");
        return 1;
    }

    log_entry_t logs[MAX_LOGS];
    int log_count = 0;
    char line[256] = {0}; // In case of uninitialized data

    while (fgets(line, sizeof(line), pFile) && log_count < MAX_LOGS) {
        if (parse_line(line, &logs[log_count])) {
            log_count++;
        }
    }
    fclose(pFile);

    // Filter by level if provided as command line argument
    const char *filter_level = NULL;
    if (argc > 1) {
        filter_level = argv[1];
    }

    for (int i = 0; i < log_count; i++) {
        if (filter_level && strcmp(logs[i].level, filter_level) != 0)
            continue; // Skip the entries that don't match the filter level

        printf("[%d][%s][%s] %s\n",
               logs[i].timestamp,
               logs[i].level,
               logs[i].module,
               logs[i].message);
    }

    int errors;
    int warnings;
    char last_fsm_state[128] = {0};

    analyze_logs(logs, log_count, &errors, &warnings, last_fsm_state);

    // Print the system summary
    printf("\nSystem Summary\n");
    printf("----------------\n");
    printf("Errors: %d\n", errors);
    printf("Warnings: %d\n", warnings);
    printf("Last FSM State: %s\n", last_fsm_state);

    return 0;
}