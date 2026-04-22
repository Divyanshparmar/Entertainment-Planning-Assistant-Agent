class Scheduler:

    def __init__(self):
        self.dependencies = {
            "Get ratings": ["Fetch movies"],
            "Analyze reviews": ["Get ratings"],
            "Generate summary": ["Analyze reviews"],

            "Book venue": ["Select event"],
            "Send invitations": ["Book venue"],
            "Finalize schedule": ["Send invitations"]
        }

    def resolve_dependencies(self, tasks):
        resolved = []
        visited = set()

        def visit(task):
            if task in visited:
                return
            for dep in self.dependencies.get(task, []):
                visit(dep)
            visited.add(task)
            resolved.append(task)

        for task in tasks:
            visit(task)

        return resolved

    def create_schedule(self, tasks):
        return self.resolve_dependencies(tasks)