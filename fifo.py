def fifo_page_replacement(ref_str, num_frames):
    frames = []
    page_faults = 0
    page_hits = 0
    
    print("\nFIFO Page Replacement")
    print("Reference String:", ref_str)
    print("Frame Table:")
    
    for page in ref_str:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the oldest page
                frames.append(page)
            page_faults += 1
            print(f"Page: {page}, Frames: {frames} (Page Fault)")
        else:
            page_hits += 1
            print(f"Page: {page}, Frames: {frames} (Page Hit)")
    
    total_pages = len(ref_str)
    hit_ratio = page_hits / total_pages
    fault_ratio = page_faults / total_pages
    
    print(f"\nTotal Page Hits: {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
    print(f"Fault Ratio: {fault_ratio:.2f}")

# Example Input for FIFO
ref_str = list(map(int, input("Enter reference string: ").split()))
num_frames = int(input("Enter number of frames: "))
fifo_page_replacement(ref_str, num_frames)
