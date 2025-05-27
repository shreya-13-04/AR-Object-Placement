# 📱 Augmented Reality Object Placement System

This Python project simulates a **priority-driven AR object placement system** using core data structures like **AVL Trees** and **Min-Heaps**. The system allows users to add, update, manage, and render virtual objects in a 3D space, enforcing constraints like **collision avoidance** and **minimum distance**.

## 🚀 Project Overview

This CLI-based simulation mimics an AR backend system that handles:

- **Object Prioritization** (using Min-Heap): Ensures the most interactive, visible, and proximate objects are rendered first.
- **Spatial Management** (using AVL Tree): Efficiently stores and retrieves AR objects based on unique IDs.
- **Collision Detection & Constraint Handling**: Avoids overlaps and enforces minimum spatial distances between objects.
- **Scene Rendering & Filtering**: Objects are rendered based on calculated priority or custom filters.

---

## 🧠 Data Structures Used

| Component                | Data Structure | Purpose |
|--------------------------|----------------|---------|
| Priority Queue           | MinHeap        | Ensures lowest-priority value is rendered first |
| Object Lookup            | AVL Tree       | Fast search, insert, and delete based on object ID |
| 3D Spatial Validation    | Bounding Box & Distance Calculations | Avoids collisions & enforces placement rules |

---

## 📂 Project Structure

```plaintext
AR-Object-Placement/
├── FINALDSAPROJECT.py     # Main CLI application
├── sample_input.txt       # Test input that covers all features
├── sample_output.txt      # Output for the test input
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies (optional/future use)
```

## How to Run

```bash
python FINALDSAPROJECT.py < sample_input.txt > sample_output.txt

```
## 🧾 Features Covered in Menu

| Choice | Feature Description                                  |
|--------|------------------------------------------------------|
|   1    | Add AR object (priority-based)                       |
|   2    | Update object attributes or spatial constraints      |
|   3    | View object with highest priority                    |
|   4    | Search object by ID                                  |
|   5    | Remove AR object                                     |
|   6    | Display all AR objects in scene                      |
|   7    | Render AR objects in sorted priority                 |
|   8    | Add object with 3D position and constraints          |
|   9    | Detect collisions between two objects                |
|  10    | Check if object satisfies constraints                |
|  11    | Exit the program                                     |



## 🧠 Algorithms in Use

- MinHeap Insert & Remove: O(log n)
- AVL Tree Insert/Search/Delete: O(log n)
- Collision & Constraint Checks: O(n)

## 👩‍💻 Author
Shreya - 
3rd Year Engineering Student | Data Science Enthusiast | AR & AI Projects

This project was developed as a collaborative effort by a 👥 team of 6 engineering students as part of our Data Structures and Algorithms course.


## 📄 License
This project is open-source under the MIT License.
