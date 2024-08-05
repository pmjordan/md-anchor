
-------

# 1 Introduction

The Topology and Orchestration Specification for Cloud Applications
(TOSCA) provides a language for describing components and
their relationships by means of a service topology, and for specifying
the lifecycle management procedures for creation or modification of
services using orchestration processes. The combination of topology
and orchestration enables not only the automation of deployment but
also the automation of the complete service lifecycle management. The
TOSCA specification promotes a model-driven approach, whereby
information embedded in the model structure (the dependencies,
connections, compositions) drives the automated processes.

The content in this section is non-normative.

## 1.1 Changes from Earlier Versions

This version of the specification includes significant changes from
TOSCA 1.3. In particular:

1. TOSCA v2.0 removes the *Simple Profile* type definitions from the
   standard. These type definitions are now managed as an open source
   project in the
   [tosca-community-contributions](https://github.com/oasis-open/tosca-community-contributions)
   github repository.
2. Rather than bundling Profiles with the TOSCA standard, TOSCA v2.0
   provides support for user-defined domain-specific profiles as follows:
   - It allows collections of type definitions to be bundled together
     into named profiles.
   - It supports importing profiles using their profile name.
3. TOSCA v2.0 formalizes support for in-life operation of a running
   service.
   - It formalizes the role of a representation model and clarifies
     how to create representation models from service templates.
   - It documents how to create multiple node representations from the
     same node template and multiple relationships from the same
     requirement assignment.
   - It defines an operational model that provides guidance for
     updating and/or upgrading a running service and for responding to
     notifications about state changes or errors.
4. TOSCA v2.0 introduces a new TOSCA Path syntax that allows a defined
   traversal of an arbitary graph of nodes and relationships to an
   attribute or property.
5. TOSCA v2.0 significantly enhances support for functions. It
   formalizes function syntax, it extends the set of built-in
   functions, and it introduces support for user-defined custom
   functions.
6. TOSCA v2.0 harmonizes constraint syntax, filter syntax, and
   condition syntax using boolean functions. 
7. TOSCA v2.0 addresses shortcomings of the v1.3 substitution mapping
   grammar.
8. TOSCA v2.0 simplifies and extends the CSAR file format.
9. TOSCA v2.0 includes a broad set of syntax clarifications,
   including but not limited to:
   - The service template is renamed TOSCA file and service template
     is redefined.
   - Grammar for relationship types, requirement definitions, and
     requirement assignments has been extended and clarified.
   - Short notation for entry_schema and key_schema has been
     documented

## 1.2 Document Conventions

- Naming conventions
- Font colors and styles
- Typographic conventions

## 1.3 Glossary

<!-- Optional section with suggested subsections -->

### 1.3.1 Definitions of terms
The following terms are used throughout this specification and have
the following definitions when used in context of this document.
