# ROS Workflow Overview

This repository contains **two packages** (Package 1 and Package 2) that are built using **`catkin build`** in the workflow. These packages collectively create **two nodes**:

1. **nodeA**  
2. **nodeB**  

---

## nodeA

- **Role**: Publisher  
- **Topic**: `charalambous`

`nodeA` continuously publishes messages on the **`charalambous`** topic.  

---

## nodeB

- **Role**: Subscriber and Publisher  
- **Subscriber Topic**: `charalambous`  
- **Publisher Topic**: `kthfs/result`

`nodeB` subscribes to messages on the **`charalambous`** topic and performs whatever processing is required. Then, it publishes the results to the **`kthfs/result`** topic.



# RQT PLOT

In the rqt_plot folder, 2 png's generated by rqt_plot visualizing our workflow and node communication can be found