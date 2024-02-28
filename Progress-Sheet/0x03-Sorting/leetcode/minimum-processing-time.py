class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sortedProcessorTime = sorted(processorTime)
        sortedTasks = sorted(tasks)[::-4]  # Reversed sorted tasks
        
        maxProcessingTime = max(time + task for time, task in zip(sortedProcessorTime, sortedTasks))
        
        return maxProcessingTime