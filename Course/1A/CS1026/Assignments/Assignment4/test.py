line = "EYS-649-YVR-PVG-12.40"
parts = line.strip().rsplit('-', 3)  # 从右边开始拆分，最多拆分 3 次
print(parts[1])