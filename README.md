1. # Mobile Explorer Robot - ROS2 Jazzy & Gazebo Sim

This project features a differential drive robot designed for university academic research. It includes a complete physical model with a chassis, a neck, a head (eyes), and a functional drive system simulated in Gazebo.

## 🤖 Robot Features
*   **Differential Drive System:** Two active wheels and one caster wheel for balance.
*   **Humanoid Structure:** Elevated head and neck design for future sensor integration (Lidar/Camera).
*   **Physics-Ready:** Includes inertial, collision, and visual properties for realistic Gazebo simulation.
*   **ROS2 Controller:** Uses the `gz-sim-diff-drive-system` plugin for movement.

## 🛠️ Prerequisites
*   **OS:** Ubuntu 24.04 LTS
*   **ROS2 Version:** Jazzy Jalisco
*   **Simulator:** Gazebo Sim (Harmonic)

## 🚀 How to Run the Simulation

Follow these steps in separate terminal tabs:

### 1. Build and Launch Robot State
```bash
cd ~/robot_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch my_robot_description rsp.launch.py
2. Open Gazebo World
Bash

gz sim -r empty.sdf

3. Spawn the Robot
Bash

ros2 run ros_gz_sim create -topic robot_description -name explorer_bot -z 0.5

4. Control the Robot (Teleop)

First, start the bridge:
Bash

ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist

Then, run the keyboard controller:
Bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard

- Project Structure

    urdf/robot.urdf: The physical description of the robot.

    launch/rsp.launch.py: Python launch script to process the URDF and publish the robot state.

Developed by: Cerine and Hiba

University: USTHB / FGE


---

### How to save this to GitHub:

1.  **Create the file:**
    ```bash
    cd ~/robot_ws
    nano README.md
    ```
2.  **Paste the code above**, then save and exit (**Ctrl+O**, **Enter**, **Ctrl+X**).
3.  **Push to GitHub:**
    
```bash
    git add README.md
    git commit -m "Added professional README for university presentation"
    git push origin main
    ```
