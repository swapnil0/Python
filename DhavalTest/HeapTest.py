import Heap as h
import PatientRecord as pat

user=pat.PatientRecord(69,"dhaval chu","dhavalchu69")
user1=pat.PatientRecord(79,"swapnil","swapnil79")
user2=pat.PatientRecord(89,"pavan","pavan61")
patl=[user,user1,user2];
p=h.MaxHeap(patl)
p.heapR()
