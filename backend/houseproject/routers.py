class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "postgresql":
            return "postgresql"
        elif model._meta.app_label == "mongo":
            return "mongo"
        return "default"

    def db_for_write(self, model, **hints):
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
