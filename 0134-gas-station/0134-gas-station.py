class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total cost (sum of costs) is greater than the available gas, then we can't complete the circuit
        # Rule is if at all the total sum of gains is negative, we don't have a solution
        total_gas_available = sum(gas)
        total_gas_cost_to_travel = sum(cost)
        if total_gas_cost_to_travel > total_gas_available:
            return -1
        
        curr_gain = 0
        start_point = 0
        for i in range(len(gas)):
            gain = gas[i]-cost[i]
            curr_gain+=gain
            if curr_gain < 0:
                start_point = i+1
                curr_gain = 0

        return start_point if curr_gain >=0 else -1
        """
        # Using total gain variable
        curr_gain, total_gain = 0, 0
        start_point = 0
        for i in range(len(gas)):
            gain = gas[i]-cost[i]
            curr_gain = curr_gain + gain
            total_gain = total_gain + gain
            if curr_gain < 0:
                start_point = i+1
                curr_gain = 0

        return start_point if total_gain >=0 else -1
        """
        
