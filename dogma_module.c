
#include <dogma.h>
#include <dogma-names.h>
#include <dogma-extra.h>
#include <assert.h>
#include "dogma_module.h"

void pydogma_init() {
    //printf("init dogma\n");
    assert(dogma_init() == DOGMA_OK);
}

Dogma *new_Dogma() {
    Dogma *v = (Dogma *) malloc(sizeof(Dogma));
    dogma_init_context(&v->ctx);
    return v;
}

void delete_Dogma(Dogma *obj) {
    dogma_free_context(obj->ctx);
    free(obj);
}

void Dogma_set_ship(Dogma *obj, int ship_type) {
    assert(dogma_set_ship(obj->ctx, ship_type) == DOGMA_OK);
}

double Dogma_get_ship_attribute(Dogma *obj, int attribute) {
    double value;
    assert(dogma_get_ship_attribute(obj->ctx, attribute, &value) == DOGMA_OK);
    return value;
}

double Dogma_get_module_attribute(Dogma *obj, int module, int attribute) {
    double value;
    int err = dogma_get_module_attribute(obj->ctx, module, attribute, &value);
    if (err != DOGMA_OK) {
        char error [250];
        sprintf(error,"get_module_attribute module %d  attribute %d failed error: %d",module,attribute,err);        
        printf("%s\n",error);
    };
    return value;
}

double Dogma_get_charge_attribute(Dogma *obj, int module, int attribute) {
    double value;
    int err = dogma_get_charge_attribute(obj->ctx, module, attribute, &value);
    if (err != DOGMA_OK) {
        char error [250];
        sprintf(error,"get_charge_attribute module %d  attribute %d failed error: %d",module,attribute,err);
        printf("%s\n",error);
    };
    return value;
}

void Dogma_set_module_state(Dogma *obj, int slot, int state)
{
    assert(dogma_set_module_state(obj->ctx, slot, (dogma_state_t)state) == DOGMA_OK);
}

int Dogma_add_module_s(Dogma *obj, int id, int state)
{
    dogma_key_t index;
    assert(dogma_add_module_s(obj->ctx, id, &index, (dogma_state_t)state) == DOGMA_OK);
    return index;
}

int Dogma_add_module_c(Dogma *obj, int id, int charge)
{
    dogma_key_t index;
    assert(dogma_add_module_c(obj->ctx, id, &index, charge));
    return index;
}

int Dogma_add_module_sc(Dogma *obj, int id, int state, int charge)
{
    dogma_key_t index;
    assert(dogma_add_module_sc(obj->ctx, id, &index, (dogma_state_t)state, charge) == DOGMA_OK);
    return index;
}

void Dogma_add_charge(Dogma *obj, int slot, int charge)
{
    assert(dogma_add_charge(obj->ctx, slot, charge) == DOGMA_OK);
}

void Dogma_get_capacitor(Dogma *obj, bool include_reload_time, double* delta, bool* stable, double* value)
{
    dogma_get_capacitor(obj->ctx, include_reload_time, delta, stable, value);
    //printf("get_capacitor D:%f S:%d V:%f\n",*delta,*stable,*value);
}

void Dogma_set_default_skill_level(Dogma *obj, int skillLevel)
{
    assert(dogma_set_default_skill_level(obj->ctx, skillLevel) == DOGMA_OK);
}

void Dogma_set_skill_level(Dogma *obj, int skill, int skillLevel)
{
    assert(dogma_set_skill_level(obj->ctx, skill, skillLevel) == DOGMA_OK);
}

void Dogma_reset_skill_levels(Dogma *obj)
{
    assert(dogma_reset_skill_levels(obj->ctx) == DOGMA_OK);
}







