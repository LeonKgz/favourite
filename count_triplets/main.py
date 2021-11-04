def countTriplets(array, r):
  count = 0
  counts = {}
  
  # dict pairs links array elements [a] to the [ar] elements that have a higher index
  # it stores the number of how many highers ars it is linked to 
  dictPairs = {}
  for a in reversed(array):

        # if we see that there is an 'ar' in dictPairs for encountered 'a', it means 
        # this 'ar' is linked to some 'arr' already through the dictPairs so we know  
        # there is a triplet (or triplets). Update the count by the value in dictPairs
        # which is the total number 'ar' has been linked up with respective 'arr's
          if a*r in dictPairs:
                  count += dictPairs[a*r]

         # we are going backwards. If we already encountered an 'ar' before (higher in inital index)
         # save it in dictPairs with 'a' as a key and number of times we saw 'ar' before
         # if encounter 'a' again in the future again add the number of 'ar's encountered before
         # because we are traversing the aray in this order it is correct. 
         # It is similar in effect to multiplication but here we are inceremntally adding counters

          if a*r in counts:
                  dictPairs[a] = dictPairs.get(a, 0) + counts[a*r]
          counts[a] = counts.get(a, 0) + 1

  return count


#print(countTriplets([1, 10, 10, 100, 1000, 1000], 10))

print(countTriplets([1, 3, 9, 9, 27, 81], 3))

#print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
#def read_input(name):
#  with open(name, 'r') as f:
#    content = [int(i) for i in f.readlines()[1].split(" ")]
#    print(countTriplets(content, 10))
#
#read_input("input10.txt")
#read_input("input06.txt")
