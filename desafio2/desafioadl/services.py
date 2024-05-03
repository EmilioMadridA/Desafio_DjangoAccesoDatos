from .models import Tarea, SubTarea
from django.core.exceptions import ObjectDoesNotExist

def recupera_tareas_y_sub_tareas():
    return Tarea.objects.prefetch_related('subtarea_set').filter(eliminada=False)

def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(descripcion, tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
    except ObjectDoesNotExist:
        print(f"No se encontró la Tarea con id {tarea_id}.")
        return
    subtarea = SubTarea(tarea=tarea, descripcion=descripcion)
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
    except ObjectDoesNotExist:
        print(f"No se encontró la Tarea con id {tarea_id}.")
        return
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    try:
        subtarea = SubTarea.objects.get(id=subtarea_id)
    except ObjectDoesNotExist:
        print(f"No se encontró la SubTarea con id {subtarea_id}.")
        return
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas):
    for tarea in tareas:
        # Comprobar si la tarea está eliminada
        if not tarea.eliminada:
            print(f"[{tarea.id}] {tarea.descripcion}")
            # Filtrar y iterar solo sobre subtareas que no estén eliminadas
            for subtarea in tarea.subtarea_set.filter(eliminada=False):
                print(f"    ...[{subtarea.id}] {subtarea.descripcion}")