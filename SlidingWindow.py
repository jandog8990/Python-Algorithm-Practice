# sliding window techniques
class SlidingWindow:
    def basic_slide(self, elements, window_size):
        # basic slide showing all elements in list regardless
        # of the input window size
        if len(elements) <= window_size:
            return elements

        for i in range(len(elements)):
            print(elements[i:i+window_size])
        print("\n")

    def slide_stop(self, elements, window_size):
        # slide that always shows window_size elements 
        if len(elements) <= window_size:
            return elements

        for i in range(len(elements)-window_size+1):
            print(elements[i:i+window_size])
        print("\n")

    def slide_generator(self, elements, window_size):
        # generator that only shows the window by calling yield
        if len(elements) <= window_size:
            return elements

        for i in range(len(elements)-window_size+1):
            yield elements[i:i+window_size]

slidingWindow = SlidingWindow()
lst = [item for item in range(1,9)]
print(f"List = {lst}")

# basic slider
slidingWindow.basic_slide(lst, 3)

# slide stop
slidingWindow.slide_stop(lst, 3)

# slide gen
gen = slidingWindow.slide_generator(lst, 3)
print(next(gen))
print(next(gen))

# slide to calc substring
S = "eidbarofghi"
slidingWindow.slide_stop(S, 3) 
