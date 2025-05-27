#module 1
class MinHeap:
    def __init__(self):
        self.heap_list = [0]  # Dummy element at index 0
        self.current_size = 0

    def upheap(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                # Swap if the current element has a smaller priority
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, item):
        self.heap_list.append(item)  # Item is a tuple (key, element)1

        self.current_size += 1
        self.upheap(self.current_size)

    def downheap(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[i][0] > self.heap_list[min_child][0]:
                # Swap with the smaller child based on key
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i * 2  # Only left child exists
        else:
            if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def remove_min(self):
        if self.current_size == 0:
            return None
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.downheap(1)
        return root

    def min_key(self):
        if self.current_size == 0:
            return None
        return self.heap_list[1][0]  # Return the key of the min item

    def min_element(self):
        if self.current_size == 0:
            return None
        return self.heap_list[1][1]  # Return the element of the min item

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def display(self):
        print("Current heap:", self.heap_list[1:])  # Exclude the dummy element
    
    def update(self,k1,k2):
        for p in range(1,self.current_size+1):
            if self.heap_list[p][1]==k1:
                self.heap_list[p][1]==k2
                if k2<k1:
                    self.upheap(p)
                else:
                    self.downheap(p)
                return
    def checkHeap(self,alist):
        h1=alist
        l=len(h1)
        for i in range((l-2/2)+1):
            if h1[2*i+1]<h1[i]:
                return False
            if 2*i+2<l and h1[2*i+2]<h1[i]:
                return False
        return True
    def build_heap(self, lst):
        # Build a heap from a list of keys using a bottom-up approach
        i = len(lst) // 2
        self.current_size = len(lst)
        self.heap_list = [0] + lst[:]
        while i > 0:
            self.downheap(i)
            i -= 1

#module2
# This class defines AR objects with proximity, visibility, and interaction potential.
# These attributes determine the object's priority for placement in an AR environment.
class ARObject:
    def __init__(self, id, name, proximity, visibility, interaction_potential):
        # id: Unique identifier for the AR object
        # name: Name of the AR object
        # proximity: Distance from the user (lower values indicate closer proximity)
        # visibility: How visible the object is in the AR scene (higher values are better)
        # interaction_potential: How interactive the object is (higher values are better)
        self.id = id
        self.name = name
        self.proximity = proximity
        self.visibility = visibility
        self.interaction_potential = interaction_potential

    # This method calculates the object's priority based on proximity, visibility,
    # and interaction potential. This can be modified to fit the system's needs.
    def get_priority(self):
        return self.proximity + self.visibility + self.interaction_potential

    def __repr__(self):
        return f"ARObject({self.id}, {self.name}, priority={self.get_priority()})"

# This class extends the MinHeap to handle AR objects, prioritizing them based on
# their calculated priority (proximity + visibility + interaction potential).
# It allows insertion, update, and retrieval of the highest priority AR object.
class MinHeapAR(MinHeap):
    def insert_ar_object(self, ar_object):
        """
        Inserts an AR object into the min-heap.
        
        Time Complexity: O(log n) where n is the number of objects in the heap.
        """
        priority = ar_object.get_priority()
        # Insert the object as a tuple (priority, object) into the heap
        super().insert((priority, ar_object))

    def update_ar_object(self, ar_object, new_proximity, new_visibility, new_interaction_potential):
        """
        Updates an AR object's attributes (proximity, visibility, interaction_potential)
        and re-prioritizes it in the heap.
        
        Time Complexity: O(log n) for updating the heap structure after changing the priority.
        """
        # Get the old priority before updating the object
        old_priority = ar_object.get_priority()
        
        # Update the AR object with new attributes
        ar_object.proximity = new_proximity
        ar_object.visibility = new_visibility
        ar_object.interaction_potential = new_interaction_potential
        
        # Get the new priority and update it in the heap
        new_priority = ar_object.get_priority()
        super().update(old_priority, new_priority)

    def get_highest_priority_object(self):
        """
        Retrieves the AR object with the highest priority (i.e., minimum priority value).
        
        Time Complexity: O(1) as we are accessing the root element of the heap.
        """
        return self.min_element()

#module3
class AVLNode:
    def __init__(self, key, value):
        # Initialize an AVL node with key (spatial data), value (object data), and height
        self.key = key  # Key represents spatial data (e.g., position, distance)
        self.value = value  # Value represents the object data (e.g., AR object)
        self.height = 1  # Every new node starts with height 1
        self.left = None  # Left child node (initially None)
        self.right = None  # Right child node (initially None)

class AVLTree:
    def get_height(self, node):
        """
        Time complexity: O(1)
        Explanation: Return the height of a node or 0 if the node is None.
        """
        if not node:
            return 0
        return node.height

    def get_bal(self, node):
        """
        Time complexity: O(1)
        Explanation:Involves calling get_height on both child nodes, which are constant-time operations.
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right) #Difference in height between left and right subtrees

    def right_rotate(self, y):
        """
        Time complexity: O(1)
        Explanation: Performs a right rotation around the node 'y'.
        """
        x = y.left  # 'x' becomes the new root of the subtree
        T2 = x.right  # 'T2' is the right child of 'x', temporarily stored
        x.right = y  # Perform rotation: 'x' becomes parent of 'y'
        y.left = T2  # 'T2' is now the left child of 'y'
        # Update heights of the rotated nodes
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x  # Return new root of the subtree

    def left_rotate(self, x):
        """
        Time complexity: O(1)
        Explanation: Performs a left rotation around the node 'x'
        """
        y = x.right  # 'y' becomes the new root of the subtree
        T2 = y.left  # 'T2' is the left child of 'y', temporarily stored
        y.left = x  # Perform rotation: 'y' becomes parent of 'x'
        x.right = T2  # 'T2' is now the right child of 'x'
        # Update heights of the rotated nodes
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y  # Return new root of the subtree

    def insert(self, node, key, value):
        """
        Time complexity: O(log n)
        Explanation: Insertion requires traversing the tree from root to leaf (O(log n)).
                     Rebalancing involves rotations, each of which is O(1).
        """ 
        if not node:
            return AVLNode(key, value)  # If node is None, create a new AVLNode

        if key < node.key:
            node.left = self.insert(node.left, key, value)
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
        else:
            return node  # Duplicate keys are not allowed, return the same node

        # Update the height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get the balance to check if the node became unbalanced
        bal = self.get_bal(node)
        # Performing rotations if the node is unbalanced
        # Left Left Case
        if bal > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if bal < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if bal > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if bal < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  # Return the root of the subtree

    def delete(self, node, key):
        """
        Time complexity: O(log n)
        Explanation: Deletion requires traversing the tree (O(log n)) and rebalancing the tree with rotations (O(1)).
        """
        if not node:
            return node  # If the node is None, return None

        if key < node.key:
            # If key is less than node's key, delete from the left subtree
            node.left = self.delete(node.left, key)
        elif key > node.key:
            # If key is greater than node's key, delete from the right subtree
            node.right = self.delete(node.right, key)
        else:
            # If the node is found, handle the deletion
            if not node.left:
                # If the node has no left child, return the right child
                return node.right
            elif not node.right:
                # If the node has no right child, return the left child
                return node.left

            # If node has two children, find  inorder successor
            temp = self.get_min_value_node(node.right)
            # Replace the node's key and value with the inorder successor's key and value
            node.key = temp.key
            node.value = temp.value
            # Delete the inorder successor from the right subtree
            node.right = self.delete(node.right, temp.key)

        # Update height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        bal = self.get_bal(node)

        # Left Left Case
        if bal > 1 and self.get_bal(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if bal > 1 and self.get_bal(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if bal < -1 and self.get_bal(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if bal < -1 and self.get_bal(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  # Return the root of the subtree


    def search(self, node, key):
        """
        Time complexity: O(log n)
        Explanation:Searching involves traversing the tree from root to leaf (O(log n)).
        """
        if not node or node.key == key:
            return node  
        if key < node.key: #Search in left subtree, if not right subtree
            return self.search(node.left, key)  
        return self.search(node.right, key)  


    def get_min_value_node(self, node):
        """
        Time complexity: O(log n)
        Explanation: Finding the minimum key involves traversing the leftmost path in a balanced tree O(log n)).
        """
        current = node
        while current.left:
            current = current.left  # Traverse to leftmost node
        return current
#module4
class ARSceneInteractionManager:
    def __init__(self):
        self.priorityqueue = MinHeapAR()
        self.avltree = AVLTree()

    def add_ar_object(self,object):
        """
        Function : To add arobject into avl tree and priority queue
        Time Complexity: O(log n) for both heap insertion and AVL insertion.
        """
        self.priorityqueue.insert_ar_object(object) #insertion of ar object to priority queue
        self.avltree.insert(None,object.id,object) #insertion of ar object to avl tree by object id w.r.t the avl tree

    def update_ar_object(self,object,proximity,visibility,interaction_potential):
        """
        Function : Updates an ar object's attributes in heap and AVL tree.
        Time Complexity: O(log n) for both heap and AVL tree update operations.
        """
        self.priorityqueue.update_ar_object(object,proximity,visibility,interaction_potential) #updating the object in priority queue
        self.avltree.delete(None,object.id) # after updation, delete the old object
        self.avltree.insert(None,object.id,object) #insertion of object after deletion 

    def get_highest_priority_object(self):
        """
        Function: To retrieve the ar object with the highest priority
        Time Complexity: O(1) as this operation only retrieves the min element from the heap.
        """
        return self.priorityqueue.get_highest_priority_object() #return the object with highest priority queue
    
    def get_ar_object_by_id(self,objectID):
        """
        Function : To get the ar object by its id using avl tree
        Time Complexity: O(log n) due to the balanced nature of the AVL tree.
        """
        id = self.avltree.search(None,objectID)
        if id:
            return id.value #if the id exists for the avl tree , then it return the id
        return None
    
    def remove_ar_object(self,objectID):
        """
        Function : Removes ar object from avl tree and priority queue
        Time Complexity: O(log n) for both heap and AVL tree deletion operations.
        """
        object = self.get_ar_object_by_id(objectID)
        if object:
            self.priorityqueue.remove_min() #removing the min object 
            self.avltree.delete(None,object) #deleting the object w.r.t its object id

    def display_scene(self):
        """
        Displays all AR objects in the current scene based on their priority.
        """
        print("AR Scene Objects :")
        self.priorityqueue.display()

#module5
class ARObjectConstraints:
    def __init__(self, obj_id, name, position, width, height, depth, constraints):

        """
        Initializes an AR object with constraints.
        :param obj_id: Unique ID of the object.
        :param name: Name of the object.
        :param position: Position of the object in 3D space (x, y, z).
        :param width: Width of the object in AR space.
        :param height: Height of the object in AR space.
        :param depth: Depth of the object in AR space.
        :param constraints: Object placement constraints (e.g., no overlap).

         
        Time Complexity: O(1) - Constant time for object initialization.
        """
        self.obj_id = obj_id
        self.name = name
        self.position = position  # Tuple (x, y, z) position in 3D space
        self.width = width
        self.height = height
        self.depth = depth
        self.constraints = constraints  # Constraints such as allowable proximity or specific areas

    def get_bounding_box(self):

        """
        Returns the bounding box of the object for collision detection.
        :return: A tuple representing the bounding box (min_x, max_x, min_y, max_y, min_z, max_z).

        Time Complexity: O(1) - Constant time as it only computes values based on the object's attributes.
        
        """

        x, y, z = self.position
        return (x, x + self.width, y, y + self.height, z, z + self.depth)

    def check_collision(self, other_obj):

        """
        Detects collision between this object and another AR object.
        :param other_obj: Another ARObjectConstraints instance.
        :return: True if collision occurs, False otherwise.

        Time Complexity: O(1) - Constant time as it only compares the bounding boxes of two objects.
        
        """

        box1 = self.get_bounding_box()
        box2 = other_obj.get_bounding_box()
        return not (box1[1] < box2[0] or box1[0] > box2[1] or
                    box1[3] < box2[2] or box1[2] > box2[3] or
                    box1[5] < box2[4] or box1[4] > box2[5])

    def satisfies_constraints(self, other_obj):
        """
        Checks if the object satisfies its constraints when placed in the AR scene.
        :param other_obj: Another ARObjectConstraints instance.
        :return: True if constraints are satisfied, False otherwise.
        

        Time Complexity: O(1) for checking the minimum distance constraint.
        """

        min_distance = self.constraints.get('min_distance', 0)
        distance = self.calculate_distance(other_obj)
        if distance < min_distance:
            return False
        return True

    def calculate_distance(self, other_obj):

        """
        Calculates the Euclidean distance between this object and another AR object.
        :param other_obj: Another ARObjectConstraints instance.
        :return: The Euclidean distance between the objects.
        

         Time Complexity: O(1) - Constant time to calculate the distance between two points in 3D space.
        """
        x1, y1, z1 = self.position
        x2, y2, z2 = other_obj.position
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    def __repr__(self):

        """
        Provides a string representation of the AR object for easy identification.
        
        Time Complexity: O(1) - Constant time for string formatting and display.
        """
        return f"ARObjectConstraints({self.obj_id}, {self.name}, pos={self.position})"


class ARScene:
    def __init__(self):
        self.objects = []  # List of ARObjectConstraints in the scene

    """
    Time Complexity: O(1) - Constant time to create an empty list for objects.
    """
    def add_object(self, ar_object):
        """
        Adds an AR object to the scene, checking for collisions and constraints.
        :param ar_object: ARObjectConstraints instance to add.
        :return: True if added successfully, False if there's a collision or constraint violation.
        

        Time Complexity: O(n) - Where n is the number of objects in the scene.
        The function iterates over each existing object in the scene to check for collisions and constraints.
        """
        for existing_object in self.objects:
            if ar_object.check_collision(existing_object):
                print(f"Collision detected between {ar_object.name} and {existing_object.name}.")
                return False

            if not ar_object.satisfies_constraints(existing_object):
                print(f"Constraints violated between {ar_object.name} and {existing_object.name}.")
                return False

        self.objects.append(ar_object)
        return True

    def display_scene(self):
        """
        Displays all objects in the AR scene.

         Time Complexity: O(n) - Where n is the number of objects in the scene.
        The function iterates over each object in the scene and prints its representation.
        
        """
        for obj in self.objects:
            print(obj)

#module6
class ARObjectRenderer:
    def __init__(self, interaction_manager):
        """
        Initializes the renderer with an interaction manager.
        
        :param interaction_manager: An instance of ARSceneInteractionManager to access AR objects.
        """
        self.interaction_manager = interaction_manager

    def render(self):
        """
        Renders all AR objects in the current scene based on their priority.
        
        This method retrieves AR objects from the priority queue and sorts them by priority before rendering.
        """
        print("Rendering AR Scene Objects:")
        
        # Retrieve objects from the priority queue, excluding the dummy element
        objects = self.interaction_manager.priorityqueue.heap_list[1:]  
        
        # Sort objects by priority and render each one
        sorted_objects = sorted(objects, key=lambda x: x[0])
        
        for priority, ar_object in sorted_objects:
            self._render_object(ar_object)

    def _render_object(self, ar_object):
        """
        Renders a single AR object. This is a placeholder for actual rendering logic.
        
        :param ar_object: The ARObject instance to render.
        """
        try:
            # Check if the object is valid for rendering
            if not isinstance(ar_object, ARObject):
                raise ValueError("Invalid AR object provided for rendering.")
                
            print(f"Rendering {ar_object.name} with ID {ar_object.id} at priority {ar_object.get_priority()}")
            
            # Placeholder for actual rendering logic
            # For example: ar_object.render() or some graphics library call
            
        except Exception as e:
            print(f"Error rendering object {ar_object.id}: {str(e)}")

    def filter_objects(self, criteria):
        """
        Filters AR objects based on specified criteria.
        
        :param criteria: A function that takes an ARObject and returns True if it meets the criteria.
        :return: A list of filtered AR objects.
        """
        all_objects = self.interaction_manager.priorityqueue.heap_list[1:]  # Exclude dummy element
        filtered_objects = [ar_object for _, ar_object in all_objects if criteria(ar_object)]
        
        return filtered_objects

    def render_filtered(self, criteria):
        """
        Renders only the AR objects that meet specified criteria.
        
        :param criteria: A function that takes an ARObject and returns True if it meets the criteria.
        """
        print("Rendering Filtered AR Scene Objects:")
        
        filtered_objects = self.filter_objects(criteria)
        
        for ar_object in filtered_objects:
            self._render_object(ar_object)

def main():
    # Initialize all managers and scenes
    interaction_manager = ARSceneInteractionManager()
    renderer = ARObjectRenderer(interaction_manager)
    ar_scene = ARScene()
    ar_objects_dict = {}

    while True:
        print("\n=== AR System Menu ===")
        print("1. Add AR Object")
        print("2. Update AR Object")
        print("3. Get Highest Priority Object")
        print("4. Find Object by ID")
        print("5. Remove AR Object")
        print("6. Display Scene")
        print("7. Render Scene")
        print("8. Add Object with Constraints")
        print("9. Check Object Collisions")
        print("10. Check Object Constraints")
        print("11. Exit")

        choice = input("\nEnter your choice (1-11): ")

        try:
            if choice == '1':
                try:
                    # Add basic AR object
                    obj_id = input("Enter object ID: ")
                    
                    existing_obj = interaction_manager.get_ar_object_by_id(obj_id)
                    if obj_id in ar_objects_dict or existing_obj:
                        print(f"Error: Object with ID {obj_id} already exists. Please use a different ID.")
                    else:
                        name = input("Enter object name: ")
                        proximity = float(input("Enter proximity (lower is closer): "))
                        visibility = float(input("Enter visibility (higher is better): "))
                        interaction_potential = float(input("Enter interaction potential (higher is better): "))
                        
                        ar_object = ARObject(obj_id, name, proximity, visibility, interaction_potential)
                        interaction_manager.add_ar_object(ar_object)
                        ar_objects_dict[obj_id] = ar_object
                        #print(f"Object {obj.name} added successfully with ID {obj_id}")
                        print(f"Added AR Object: {ar_object}")
                    
                except ValueError as e:
                    print(f"Error: Invalid input - {e}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '2':
                # Update AR object
                obj_id = input("Enter object ID to update: ")
                obj_id = input("Enter object ID to update: ")
                
                for obj in ar_objects_list:
                    if obj[0]==obj_id:
                        print("\nSelect update type:")
                        print("1. Update priority attributes")
                        print("2. Update position and constraints")
                        update_choice = input("Enter choice (1-2): ")
                        
                        
                        if update_choice == '1':
                            new_proximity = float(input("Enter new proximity: "))
                            new_visibility = float(input("Enter new visibility: "))
                            new_interaction = float(input("Enter new interaction potential: "))
                       
                        elif update_choice == '2':
                            x = float(input("Enter new X position: "))
                            y = float(input("Enter new Y position: "))
                            z = float(input("Enter new Z position: "))
                        min_distance = float(input("Enter new minimum distance constraint: "))
                        # Update position and constraints in ar_objects_dict if it exists
                        if obj_id in ar_objects_dict:
                            ar_objects_dict[obj_id].position = (x, y, z)
                            ar_objects_dict[obj_id].constraints['min_distance'] = min_distance
                    print("Object updated successfully")
                else:
                    print("Object not found")

            elif choice == '3':
                # Get highest priority object
                highest_priority_obj = interaction_manager.get_highest_priority_object()
                if highest_priority_obj:
                    print(f"Highest priority object: {highest_priority_obj}")
                else:
                    print("No objects in scene")

            elif choice == '4':
                # Find object by ID
                obj_id = input("Enter object ID to find: ").strip()  # Remove any whitespace
                print(f"Available objects: {list(ar_objects_dict.keys())}")  # Debug line
                if obj_id in ar_objects_dict:
                    obj = ar_objects_dict[obj_id]
                    print(f"\nObject found:")
                    print(f"ID: {obj_id}")
                    print(f"Name: {obj.name}")
                    
                    # Add other properties as needed
                else:
                    print(f"No object found with ID: '{obj_id}'")

            elif choice == '5':
                # Remove AR object
                obj_id = input("Enter object ID to remove: ")
                interaction_manager.remove_ar_object(obj_id)
                if obj_id in ar_objects_dict:
                    del ar_objects_dict[obj_id]
                print("Object removed if it existed")

            

            elif choice == '6':
                # Display scene
                print(ar_objects_dict)
            
            
            elif choice == '7':
                for i in ar_objects_dict:
                    if i== ar_object.id:
                        print(i)
                if len(ar_objects_dict) == 0:
                    print("No objects rendered.")


            elif choice == '8':
                # Add object with constraints
                obj_id = input("Enter object ID: ")
                name = input("Enter object name: ")
                
                # Get position
                x = float(input("Enter X position: "))
                y = float(input("Enter Y position: "))
                z = float(input("Enter Z position: "))
                position = (x, y, z)
                
                # Get dimensions
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                depth = float(input("Enter depth: "))
                
                # Get constraints
                min_distance = float(input("Enter minimum distance from other objects: "))
                constraints = {'min_distance': min_distance}
                
                # Create constrained AR object
                ar_object_constrained = ARObjectConstraints(
                    obj_id, name, position, width, height, depth, constraints
                )
                
                # Add to scene if constraints are satisfied
                if ar_scene.add_object(ar_object_constrained):
                    ar_objects_dict[obj_id] = ar_object_constrained
                    print(f"Added constrained AR Object: {ar_object_constrained}")
                else:
                    print("Failed to add object due to constraints or collisions")

            elif choice == '9':
                # Check collisions between objects
                obj_id1 = input("Enter first object ID: ")
                obj_id2 = input("Enter second object ID: ")
                
                if obj_id1 in ar_objects_dict and obj_id2 in ar_objects_dict:
                    obj1 = ar_objects_dict[obj_id1]
                    obj2 = ar_objects_dict[obj_id2]
                    
                    if obj1.check_collision(obj2):
                        print(f"Collision detected between {obj1.name} and {obj2.name}")
                    else:
                        print("No collision detected between the objects")
                else:
                    print("One or both objects not found")

            elif choice == '10':
                # Check constraints for an object
                obj_id = input("Enter object ID to check constraints: ")
                if obj_id in ar_objects_dict:
                    obj = ar_objects_dict[obj_id]
                    all_constraints_satisfied = True
                    
                    # Check constraints against all other objects
                    for other_id, other_obj in ar_objects_dict.items():
                        if other_id != obj_id:
                            if not obj.satisfies_constraints(other_obj):
                                print(f"Constraints violated with object {other_obj.name}")
                                all_constraints_satisfied = False
                    
                    if all_constraints_satisfied:
                        print("All constraints are satisfied")
                else:
                    print("Object not found")

            elif choice == '11':
                # Exit program
                print("Exiting AR System...")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 11.")

        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()