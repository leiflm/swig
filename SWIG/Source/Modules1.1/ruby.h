/********************************************************************
 * Ruby module for SWIG
 *
 * $Header$
 *
 * Copyright (C) 2000  Network Applied Communication Laboratory, Inc.
 * Copyright (C) 2000  Information-technology Promotion Agency, Japan
 *
 * Masaki Fukushima
 *
 ********************************************************************/

class RUBY : public Language {
 protected:
  virtual String *make_wrapper_name(char *cname);
  virtual char *validate_const_name(char *name);
  virtual char *ruby_typemap_lookup(char *, SwigType *, String_or_char *, char *, char *, Wrapper * = 0);
  virtual int to_VALUE(SwigType *, char *, DOHString *, int = 0);
  virtual int from_VALUE(SwigType *, char *, char *, DOHString *);
 public:
  /* Virtual functions required by the SWIG parser */
  virtual void parse_args(int, char *argv[]);
  virtual void parse();
  virtual void function(DOH *node);
  virtual void variable(DOH *node);
  virtual void constant(DOH *node);
  virtual void initialize(void);
  virtual void close(void);
  virtual void set_module(char *);
  virtual void nativefunction(DOH *);
  virtual void create_command(char *, char *, int);
  virtual void import(char *);

  /* C++ language extensions. */
  virtual void cpp_memberfunction(DOH *);
  virtual void cpp_constructor(DOH *);
  virtual void cpp_destructor(DOH *);
  virtual void cpp_open_class(char *classname, char *rname, char *ctype, int strip);
  virtual void cpp_close_class();
  virtual void cpp_inherit(char **baseclass, int mode = INHERIT_ALL);
  virtual void cpp_variable(DOH *);
  virtual void cpp_staticfunction(DOH *);
  virtual void cpp_constant(DOH *);
  virtual void cpp_staticvariable(DOH *);

  /* Declaration of a class, but not a full definition */
  virtual void cpp_class_decl(char *, char *, char *);

  /* Pragma directive  */
  virtual void pragma(char *, char *, char *);
  virtual void cpp_pragma(Pragma *);
};

/*
 * Local Variables:
 * c-basic-offset: 2
 * End:
 */
