%module dogma
%feature("autodoc","3");
%include "exception.i"
%include "typemaps.i"

%{
#define SWIG_FILE_WITH_INIT
#include "dogma.h"
#include "dogma_module.h"
%}

%init %{
    pydogma_init();
%}

%apply double *OUTPUT { double* delta, double* value };
%apply bool *OUTPUT { bool*stable};

typedef struct {
    dogma_context_t *ctx;
} Dogma;

%extend Dogma {  
  Dogma();
  ~Dogma();

  void set_ship(int shipType);
  double get_ship_attribute(int);
  double get_module_attribute(int, int);

  double get_charge_attribute(int, int);
  void set_module_state(int, int);
  int add_module_s(int, int);
  int add_module_c(int, int);
  int add_module_sc(int, int, int);

  void add_charge(int, int);
  void get_capacitor(bool include_reload_time, double* delta, bool* stable, double *value);
  void set_default_skill_level(int skillLevel);
  void set_skill_level(int skill, int skillLevel);
  void reset_skill_levels();

};


enum dogma_state_s {
	/* These values are actually bitmasks: if bit of index i is set,
	 * it means effects with category i should be evaluated. */
	DOGMA_STATE_Unplugged = 0,   /* 0b00000000 */
	DOGMA_STATE_Offline = 1,     /* 0b00000001 */
	DOGMA_STATE_Online = 17,     /* 0b00010001 */
	DOGMA_STATE_Active = 31,     /* 0b00011111 */
	DOGMA_STATE_Overloaded = 63, /* 0b00111111 */
};

/*

%apply double *OUTPUT { double* delta, double* value };
%apply bool *OUTPUT { bool*stable};


class Dogma {
    private:
        dogma_context_t *ctx;
    public:
        Dogma();
        ~Dogma();

        void set_ship(int shipType);

        double get_ship_attribute(int );
        double get_module_attribute(int, int);
        double get_charge_attribute(int, int);
        void set_module_state(int, int);
        int add_module_s(int, int);
        int add_module_c(int, int);
        int add_module_sc(int, int, int);

        void add_charge(int, int);
		    void get_capacitor(bool include_reload_time, double* delta, bool* stable, double *value);
        void set_default_skill_level(int skillLevel);
        void set_skill_level(int skill, int skillLevel);
        void reset_skill_levels();

};
*/