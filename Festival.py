# DEMCON FESTIVAL!
# 06-08-2024 - TEI + Copilot
# import
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import heapq


def min_stages(shows):
    # Convert shows to a list of tuples (start, end, name)
    intervals = [(show[1], show[2], show[0]) for show in shows]

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Use a min-heap to keep track of end times of shows currently using a stage
    heap = []
    stages = [[] for _ in range(len(shows))]

    for interval in intervals:
        # If the earliest ending show is finished before the current show starts, remove it from the heap
        if heap and heap[0][0] <= interval[0]:
            end_time, stage = heapq.heappop(heap)
        else:
            stage = len(heap)

        # Add the current show's end time to the heap
        heapq.heappush(heap, (interval[1], stage))
        stages[stage].append(interval)

    # Filter out empty stages
    stages = [stage for stage in stages if stage]

    return stages


def plot_stages(stages, stage_names):
    # Extend stage_names with numbers if there are not enough names
    if len(stage_names) < len(stages):
        stage_names.extend([f'Stage {i + 1}' for i in range(len(stage_names), len(stages))])

    fig, ax = plt.subplots(figsize=(10, 6))

    for stage_index, stage in enumerate(stages):
        for show in stage:
            start, end, name = show
            ax.add_patch(
                patches.Rectangle((start, stage_index), end - start, 0.8, edgecolor='black', facecolor='skyblue'))
            ax.text(start + (end - start) / 2, stage_index + 0.4, name, ha='center', va='center')

    ax.set_yticks(range(len(stages)))
    ax.set_yticklabels(stage_names[:len(stages)])
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Stages')
    ax.set_title('Shows per Stage - DEMCON Festival 2024')

    # Set x and y limits
    ax.set_xlim(0,  48)
    ax.set_ylim(-1, len(stages))

    # Add vertical lines for every hour
    for hour in range(int(ax.get_xlim()[1]) + 1):
        ax.axvline(x=hour, color='gray', linestyle='--', linewidth=0.5)

    plt.show()


# Input
shows = [
    ("show_1", 29, 33),
    ("show_2", 2, 9),
    ("show_3", 44, 47),
    ("show_4", 26, 30),
    ("show_5", 15, 20),
    ("show_6", 8, 15),
    ("show_7", 2, 9),
    ("show_8", 30, 34),
    ("DEMCON band", 1, 9),
    ("show_10", 20, 28),
    ("show_11", 1, 4),
    ("show_12", 2, 11),
    ("show_13", 26, 29),
    ("show_14", 5, 10),
    ("show_15", 37, 44),
    ("show_16", 27, 35),
    ("show_17", 36, 39),
    ("show_18", 4, 10),
    ("show_19", 35, 44),
    ("show_20", 22, 30),
    ("show_21", 15, 20),
    ("show_22", 42, 46),
    ("show_23", 6, 9),
    ("show_24", 19, 23),
    ("show_25", 31, 38),
    ("show_26", 37, 41),
    ("show_27", 30, 36),
    ("show_28", 14, 21),
    ("show_29", 5, 13),
    ("show_30", 33, 36)
]

stage_names = ["Enschede", "Delft", "Groningen", "Best", "Munster", "Singapore","Leiden", "Maastricht", "Tokyo"]

# Extend all shows by one hour (end time includes the full hour)
extended_shows = [(name, start, end + 1) for name, start, end in shows]

stages = min_stages(extended_shows)
plot_stages(stages, stage_names)
