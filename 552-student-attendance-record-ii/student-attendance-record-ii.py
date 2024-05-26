class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp_curr_state = [[0] * 3 for _ in range(2)]
        dp_next_state = [[0] * 3 for _ in range(2)]

        dp_curr_state[0][0] = 1

        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    dp_next_state[total_absences][0] = (
                        dp_next_state[total_absences][0] + 
                        dp_curr_state[total_absences][consecutive_lates]
                    ) % MOD
                    if total_absences < 1:
                        dp_next_state[total_absences + 1][0] = (
                            dp_next_state[total_absences + 1][0] + 
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD
                    if consecutive_lates < 2:
                        dp_next_state[total_absences][consecutive_lates + 1] = (
                            dp_next_state[total_absences][consecutive_lates + 1] + 
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD

            dp_curr_state = [row[:] for row in dp_next_state]
            dp_next_state = [[0] * 3 for _ in range(2)]

        count = sum(dp_curr_state[total_absences][consecutive_lates] \
                    for total_absences in range(2) \
                    for consecutive_lates in range(3)) % MOD
        return count 