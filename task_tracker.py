import json
import sys
import argparse
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path

# ==========================================
# Domain Layer (Entities)
# ==========================================

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str  # 'pending', 'in-progress', 'completed'
    created_at: str
    updated_at: str

    @classmethod
    def create(cls, id: int, title: str, description: str) -> 'Task':
        now = datetime.now().isoformat()
        return cls(
            id=id,
            title=title,
            description=description,
            status="pending",
            created_at=now,
            updated_at=now
        )

    def mark_complete(self) -> None:
        self.status = "completed"
        self.updated_at = datetime.now().isoformat()

# ==========================================
# Data Layer (Persistence)
# ==========================================

class TaskRepository:
    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = Path(storage_file)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        # Ensure the directory exists if specified
        if self.storage_file.parent != Path('.'):
            self.storage_file.parent.mkdir(parents=True, exist_ok=True)
            
        if not self.storage_file.exists():
            self._save_tasks([])

    def _save_tasks(self, tasks: List[Dict[str, Any]]) -> None:
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
            sys.exit(1)

    def load_all(self) -> List[Task]:
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                # Safely construct Task objects
                return [Task(**item) for item in data]
        except (IOError, json.JSONDecodeError, TypeError):
            # Return empty list on file errors or schema corruption
            return []

    def save_all(self, tasks: List[Task]) -> None:
        self._save_tasks([asdict(t) for t in tasks])

# ==========================================
# Service Layer (Business Logic)
# ==========================================

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repo = repository

    def add_task(self, title: str, description: str) -> Task:
        tasks = self.repo.load_all()
        new_id = 1 if not tasks else max(t.id for t in tasks) + 1
        new_task = Task.create(new_id, title, description)
        tasks.append(new_task)
        self.repo.save_all(tasks)
        return new_task

    def list_tasks(self, status_filter: Optional[str] = None) -> List[Task]:
        tasks = self.repo.load_all()
        if status_filter:
            return [t for t in tasks if t.status == status_filter]
        return tasks

    def complete_task(self, task_id: int) -> Optional[Task]:
        tasks = self.repo.load_all()
        for task in tasks:
            if task.id == task_id:
                task.mark_complete()
                self.repo.save_all(tasks)
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        tasks = self.repo.load_all()
        initial_count = len(tasks)
        tasks = [t for t in tasks if t.id != task_id]
        if len(tasks) < initial_count:
            self.repo.save_all(tasks)
            return True
        return False
    
    def edit_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
     tasks = self.repo.load_all()
     for task in tasks:
        if task.id == task_id:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            task.updated_at = datetime.now().isoformat()
            self.repo.save_all(tasks)
            return task
     return None

# ==========================================
# Presentation Layer (CLI)
# ==========================================

def main():
    parser = argparse.ArgumentParser(description="Professional Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument("--desc", type=str, default="", help="Task description")

    # List Command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", type=str, choices=["pending", "completed"], help="Filter by status")

    # Complete Command
    complete_parser = subparsers.add_parser("complete", help="Mark task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete Command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

# Edit Command
    edit_parser = subparsers.add_parser("edit", help="Edit a task")
    edit_parser.add_argument("id", type=int, help="Task ID")
    edit_parser.add_argument("--title", type=str, help="New title")
    edit_parser.add_argument("--desc", type=str, help="New description")
    args = parser.parse_args()
    
    repo = TaskRepository()
    service = TaskService(repo)

    if args.command == "add":
        task = service.add_task(args.title, args.desc)
        print(f"✅ Task created: [ID: {task.id}] {task.title}")

    elif args.command == "list":
        tasks = service.list_tasks(args.status)
        if not tasks:
            print("No tasks found.")
        else:
            print(f"\n{'ID':<5} {'STATUS':<12} {'TITLE':<30} {'DESCRIPTION'}")
            print("-" * 70)
            for t in tasks:
                status_icon = "✓" if t.status == "completed" else "○"
                print(f"{t.id:<5} {status_icon} {t.status:<10} {t.title:<30} {t.description}")
            print("-" * 70)

    elif args.command == "complete":
        task = service.complete_task(args.id)
        if task:
            print(f"🎉 Task {args.id} marked as completed!")
        else:
            print(f"❌ Task ID {args.id} not found.")

    elif args.command == "delete":
        if service.delete_task(args.id):
            print(f"🗑️  Task {args.id} deleted.")
        else:
            print(f"❌ Task ID {args.id} not found.")

    elif args.command == "edit":
     task = service.edit_task(args.id, args.title, args.desc)
     if task:
            print(f"✏️  Task {args.id} updated successfully!")
     else:
            print(f"❌ Task ID {args.id} not found.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()