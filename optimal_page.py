def optimal_page_replacement(ref_str, num_frames):
    frames = []
    page_faults = 0
    page_hits = 0
    
    print("\nOptimal Page Replacement")
    print("Reference String:", ref_str)
    print("Frame Table:")
    
    for i in range(len(ref_str)):
        if ref_str[i] not in frames:
            if len(frames) < num_frames:
                frames.append(ref_str[i])
            else:
                future = ref_str[i + 1:]
                indices = []
                for page in frames:
                    if page in future:
                        indices.append(future.index(page))
                    else:
                        indices.append(float('inf'))
                
                replacement_idx = indices.index(max(indices))
                frames[replacement_idx] = ref_str[i]
            page_faults += 1
            print(f"Page: {ref_str[i]}, Frames: {frames} (Page Fault)")
        else:
            page_hits += 1
            print(f"Page: {ref_str[i]}, Frames: {frames} (Page Hit)")
    
    total_pages = len(ref_str)
    hit_ratio = page_hits / total_pages
    fault_ratio = page_faults / total_pages
    
    print(f"\nTotal Page Hits: {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
    print(f"Fault Ratio: {fault_ratio:.2f}")

# Example Input for Optimal
ref_str = list(map(int, input("Enter reference string: ").split()))
num_frames = int(input("Enter number of frames: "))
optimal_page_replacement(ref_str, num_frames)
