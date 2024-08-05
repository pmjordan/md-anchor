![OASIS Logo](http://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# TOSCA Version 2.0

## Committee Specification Draft 07

## 16 July 2024 <a name="july-2024"></a>

&nbsp;

#### This stage:

https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd06/TOSCA-v2.0-csd06.md (Authoritative) \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd06/TOSCA-v2.0-csd06.html \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd06/TOSCA-v2.0-csd06.pdf

#### Previous stage:

https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd05/TOSCA-v2.0-csd05.docx (Authoritative) \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd05/TOSCA-v2.0-csd05.html \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd05/TOSCA-v2.0-csd05.pdf

#### Latest stage:

https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.md (Authoritative) \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.html \
https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.pdf

#### Technical Committee:

[OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC](https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=f9412cf3-297d-4642-8598-018dc7d3f409)

#### Chair:

Chris Lauwers (lauwers@ubicity.com), Individual Member

#### Editors:

Chris Lauwers (lauwers@ubicity.com), Individual Member \
Calin Curescu (calin.curescu@ericsson.com), [Ericsson](http://ericsson.com/)

#### Related work:

This specification replaces or supersedes:
* _Topology and Orchestration Specification for Cloud Applications Version 1.0._ Edited by Derek Palma and Thomas Spatzier. OASIS Standard. Latest version: http://docs.oasis-open.org/tosca/TOSCA/v1.0/TOSCA-v1.0.html.
* _TOSCA Simple Profile in YAML Version 1.3._ Edited by Matt Rutkowski, Chris Lauwers, Claude Noshpitz, and Calin Curescu. Latest stage: https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/TOSCA-Simple-Profile-YAML-v1.3.html.

This specification is related to:
* _Introduction to TOSCA Version 2.0._ Edited by Chris Lauwers and Calin Curescu. Work in progress.

#### Abstract:

The Topology and Orchestration Specification for Cloud Applications (TOSCA) provides a language for describing application components and their relationships by means of a service topology, and for specifying the lifecycle management procedures for creation or modification of services using orchestration processes. The combination of topology and orchestration enables not only the automation of deployment but also the automation of the complete service lifecycle management. The TOSCA specification promotes a model-driven approach, whereby information embedded in the model structure (the dependencies, connections, compositions) drives the automated processes.

#### Status:

This document was last revised or approved by the OASIS Topology and Orchestration Specification for Cloud Applications (TOSCA) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://groups.oasis-open.org/communities/tc-community-home2?CommunityKey=f9412cf3-297d-4642-8598-018dc7d3f409#technical.

TC members should send comments on this specification to the TC's email list. Any individual may submit comments to the TC by sending email to Technical-Committee-Comments@oasis-open.org. Please use a Subject line like "Comment on TOSCA".

This specification is provided under the [RF on Limited Terms](https://www.oasis-open.org/policies-guidelines/ipr/#RF-on-Limited-Mode) of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (https://www.oasis-open.org/committees/tosca/ipr.php).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process-2017-05-26/#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### Key words:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](#rfc2119)] and [[RFC8174](#rfc8174)] when, and only when, they appear in all capitals, as shown here.

#### Citation format:

When referencing this specification the following citation format should be used:

**[TOSCA-v2.0]**

_TOSCA Version 2.0_.
Edited by Chris Lauwers and Calin Curescu.
20 June 2024.
OASIS Committee Specification Draft 06.
https://docs.oasis-open.org/tosca/TOSCA/v2.0/csd06/TOSCA-v2.0-csd06.html.
Latest stage: https://docs.oasis-open.org/tosca/TOSCA/v2.0/TOSCA-v2.0.html.

#### Notices

Copyright &copy; OASIS Open 2024. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in an Appendix below.

-------

# Table of Contents

> Provide later
[[TOC will be inserted here]]

-------

# 1 Introduction <a name="introduction"></a>
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

## 1.1 Changes from Earlier Versions <a name="changes-from-earlier-versions"></a>

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

## 1.2 Document Conventions <a name="document-conventions"></a>

- Naming conventions
- Font colors and styles
- Typographic conventions

## 1.3 Glossary <a name="glossary"></a>

<!-- Optional section with suggested subsections -->

### 1.3.1 Definitions of terms <a name="definitions-of-terms"></a>
The following terms are used throughout this specification and have
the following definitions when used in context of this document.

|Term|Definition|
|---|---|
|Representation Model|A deployed service is a running instance of a service template. The instance is typically derived by running a declarative workflow that is automatically generated based on the node templates and relationship templates defined in the service template.|
|Node Template| A *node template* specifies the occurrence of a component node as part of a service template. Each node template refers to a node type that defines the semantics of the node (e.g., properties, attributes, requirements, capabilities, interfaces). Node types are defined separately for reuse purposes.                                                          |
|Relationship Template| A *relationship template* specifies the occurrence of a relationship between nodes in a service template. Each relationship template refers to a relationship type that defines the semantics of the relationship (e.g., properties, attributes, interfaces, etc.). relationship types are defined separately for reuse purposes.                                           |
|Service Template| A *service template* is used to specify the *topology* (or structure) and *orchestration* (or invocation of management behavior) of services so that they can be provisioned and managed in accordance with constraints and policies.                                                                                                                   |
|Topology Model| A Topology Model defines the structure of a service in the context of a service template. A Topology model consists of a set of node template and relationship template definitions that together define the topology of a service as a (not necessarily connected) directed graph.                                                                                  |
|Abstract Node Template | An abstract node template is a node template that doesn’t define any implementations for the TOSCA lifecycle management operations. Service designers explicitly mark node templates as abstract using the substitute directive. TOSCA orchestrators provide implementations for abstract node templates by finding substituting templates for those node templates. |

### 1.3.2 Acronyms and Abbreviations <a name="acronyms-and-abbreviations"></a>
Defined in this document
- TOSCA Topology and Orchestration Specification for Cloud Applications
- CSAR  Cloud Service Archive A file format defined by OASIS TOSCA to contain TOSCA files

Used by this specification
- YAML  Yet Another Markup Language The Language TOSCA uses for files
- MACD  Moves, Adds, Changes, and Deletions
- DSL  Domain Specific Language

Used as examples
- DBMS  Database Management System
- EJB Enterprise Java Beans
- SD-WAN Software Defined Wide Area Network
- SQL Structured Query Language
- TAR Tape Archive A file format originally used in unix
- VPN Virtual Private Network
- USD United States Dollar
-------
# 2 TOSCA Overview <a name="tosca-overview"></a>

The *Topology and Orchestration Specification for Cloud Applications*
(TOSCA) is a *domain-specific language* (DSL) for automating
*Lifecycle Management* of large complex systems.

The TOSCA language allows service designers to describe system
components and their relationships by means of a service topology, and
to specify the lifecycle management procedures for the creation and
modification of services using orchestration processes. The
combination of *topology* and *orchestration* enables not only the
automation of deployment but also the automation of the complete
service lifecycle management (including scaling, patching, upgrading,
monitoring, etc.).

The content in this section is non-normative.

## 2.1 Objectives <a name="objectives"></a>

