version1 = "1.20"
version2 = "1.2"
def versionCompare(version1, version2):
    v1 = version1.split('.')
    v1 = [int(revision) for revision in v1]
    v2 = version2.split('.')
    v2 = [int(revision) for revision in v2]
    
    maxi = max(len(v1), len(v2))
    if len(v1) < len(v2):
        v1.extend([0] * (len(v1) - maxi))
    else:
        v2.extend([0] * (len(v2) - maxi))
        
    for i in range(maxi):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1 
    return 0

print(versionCompare(version1,version2))