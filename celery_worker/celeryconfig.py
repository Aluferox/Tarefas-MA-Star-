from celery import Celery
from kombu import Queue
from kombu.utils.url import safequote

aws_access_key = safequote("AKIAQJ57JJK4MD4G4VFL")
aws_secret_key = safequote("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")

broker_url = f"sqs://{aws_access_key}:{aws_secret_key}@:80"
broker_transport_options = {
    'region':'sa-east-1',
}

app = Celery (
    'celery_worker',
    broker=broker_url,
    include=['celery_worker.tasks'],
)

app.conf.task_queues = (
    Queue('tarefas', routing_key='default'),
)

if __name__ == '__main__':
    app.start()
