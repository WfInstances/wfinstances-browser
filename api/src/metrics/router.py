from fastapi import APIRouter

from src.database import wf_instance_metrics_collection, wf_instance_collection
from src.metrics.schema import serialize_wf_instances_metrics, serialize_wf_instance_metrics
from src.metrics.service import generate_graph_metrics
from src.wfinstances.schema import serialize_wf_instance

router = APIRouter()


@router.get('/')
async def get_wf_instance_metrics():
    return serialize_wf_instances_metrics(wf_instance_metrics_collection.find())


@router.get('/{id}')
async def get_wf_instance_metrics(id: str):
    return serialize_wf_instance_metrics(wf_instance_metrics_collection.find_one({'_id': id}))


@router.get('/{id}/metrics')
async def get_wf_instance_metrics_metrics(id: str):
    wf_instance_metrics = serialize_wf_instance(wf_instance_collection.find_one({'_id': id}))
    depth, min_width, max_width = generate_graph_metrics(wf_instance_metrics['workflow']['tasks'])
    return {
        'depth': depth,
        'min_width': min_width,
        'max_width': max_width
    }
