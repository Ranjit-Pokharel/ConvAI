import json
import os

class memory:
    def __init__(self, memory_home_path:str):
        self.memory_path = memory_home_path

    def load(self, file_name:str):
        full_path = os.path.join(self.memory_path, file_name)
        if not os.path.exists(full_path):
            print(f"file name: {full_path} does not exist....")
            with open(full_path, "w") as f:
                json.dump([], f)
            print(f"file name: {full_path} empty file created....")

        with open(full_path) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"file corrupted: {full_path}. returning empty file")
                return []
            
    def save(self, datas, file_name:str):
        full_path = os.path.join(self.memory_path, file_name)
        try:
            with open(full_path, "w") as file:
                json.dump(datas, file, indent=4)
        except Exception as e:
            raise e

    @property
    def memory_path(self):
        return self._memory_path
    
    @memory_path.setter
    def memory_path(self, memory_path):
        if not os.path.exists(memory_path):
            print(f"Dir: {memory_path} does not exist...")
            os.makedirs(memory_path, exist_ok=True)
            print(f"Dir: {memory_path} created...")
        
        self._memory_path = memory_path

if __name__ == "__main__":
    pass
