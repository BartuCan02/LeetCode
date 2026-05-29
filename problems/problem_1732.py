def largestAltitude(gain: List[int]) -> int:
    altitude = [0]
    for i in gain:
        altitude.append(i + altitude[-1])

    return max(altitude)