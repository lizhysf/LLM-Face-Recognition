import subprocess
import os
import threading
import webbrowser

def run_in_environment(env_path, script_name):
    """Run a Python script within a specific virtual environment with terminal interaction."""
    python_executable = os.path.join(env_path, "Scripts", "python.exe")
    command = f'"{python_executable}" "{script_name}"'
    
    try:
        print(f"Using Python interpreter: {python_executable}")
        print(f"Running script: {script_name} in environment: {env_path}\n")

        subprocess.run(command, shell=True, check=True)
        print(f"Script {script_name} executed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def run_script_thread(env_path, script_name):
    """Run a script in a separate thread to allow parallel execution."""
    thread = threading.Thread(target=run_in_environment, args=(env_path, script_name))
    thread.start()
    return thread

if __name__ == "__main__":
    face_rec_env_path = r"D:\Coding\AI With Face Recognition\face_rec_env"
    general_env_path = r"D:\Coding\AI With Face Recognition\.venv"
    
    tts_script = r"D:\Coding\AI With Face Recognition\tts_service.py"
    embeddings_script = r"D:\Coding\AI With Face Recognition\embeddings.py"
    response_script = r"D:\Coding\AI With Face Recognition\response_generation.py"
    face_rec_script = r"D:\Coding\AI With Face Recognition\face_recognition.py"
    real_time_camera_script = r"D:\Coding\AI With Face Recognition\real_time_camera.py"
    real_time_chat_script = r"D:\Coding\AI With Face Recognition\real_time_chat.py"

    run_in_environment(general_env_path, response_script)
    run_in_environment(face_rec_env_path, face_rec_script)
    
    camera_thread = run_script_thread(face_rec_env_path, real_time_camera_script)
    function_thread = run_script_thread(general_env_path, real_time_chat_script)
    tts_thread = run_script_thread(general_env_path, tts_script)

    webbrowser.open('http://127.0.0.1:5000/')

    # Wait for both threads to finish
    camera_thread.join()
    function_thread.join()
    tts_thread.join()