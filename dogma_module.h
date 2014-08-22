#include "dogma.h"

void pydogma_init();

typedef struct {
    dogma_context_t *ctx;
} Dogma;

Dogma *new_Dogma();
void delete_Dogma(Dogma *obj);

void Dogma_set_ship(Dogma *obj,int shipType);
double Dogma_get_ship_attribute(Dogma *obj,int);        
double Dogma_get_module_attribute(Dogma *obj,int, int);

double Dogma_get_charge_attribute(Dogma *obj, int, int);
void Dogma_set_module_state(Dogma *obj, int, int);
int Dogma_add_module_s(Dogma *obj, int, int);
int Dogma_add_module_c(Dogma *obj, int, int);
int Dogma_add_module_sc(Dogma *obj, int, int, int);

void Dogma_add_charge(Dogma *obj, int, int);
void Dogma_get_capacitor(Dogma *obj, bool include_reload_time, double* delta, bool* stable, double *value);
void Dogma_set_default_skill_level(Dogma *obj, int skillLevel);
void Dogma_set_skill_level(Dogma *obj, int skill, int skillLevel);
void Dogma_reset_skill_levels(Dogma *obj);