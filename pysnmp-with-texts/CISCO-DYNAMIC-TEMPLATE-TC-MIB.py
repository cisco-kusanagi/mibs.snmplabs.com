#
# PySNMP MIB module CISCO-DYNAMIC-TEMPLATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DYNAMIC-TEMPLATE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:56:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Counter64, ModuleIdentity, Bits, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter64", "ModuleIdentity", "Bits", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDynamicTemplateTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 783))
ciscoDynamicTemplateTcMIB.setRevisions(('2007-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setLastUpdated('201201270000Z')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setDescription('This MIB module defines textual conventions used by the CISCO-DYNAMIC-TEMPLATE-MIB and MIB modules that use and expand on dynamic templates.')
class DynamicTemplateName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value that identifies a dynamic template. The semantics of the string-value are the same as those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class DynamicTemplateType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of dynamic template: 'other' The implementation of the MIB module using this textual convention does not recognize the type of dynamic template. 'derived' A configuration resulting from the union of the attributes contained by all the dynamic templates associated with a target. The system generates a derived configuration, and an EMS/NMS cannot directly modify it. An EMS/NMS can only affect a derived configuration by modifying one or more of the dynamic templates associated with the target. 'ppp' A PPP template is a set of locally-configured attributes relating to the configuration of a PPP interface. 'ethernet' An Ethernet template is a set of locally-configured attributes used by the system to configure dynamic interfaces initiated on Ethernet virtual interfaces (e.g., EoMPLS) or automatically created VLANs. 'ipSubscriber' An IP subscriber template is a set of locally-configured attributes used by the system to configure certain types of IP and L2 subscriber sessions. 'service' A service template is a set of locally-configured attributes used by the system to configure subscriber sessions. These attributes specifically relate to services, and the system applies these attributes in response to subscriber session life-cycle events."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("derived", 2), ("ppp", 3), ("ethernet", 4), ("ipSubscriber", 5), ("service", 6))

class DynamicTemplateTargetType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "An enumerated integer-value describing the type of target associated with one or more dynamic templates: 'other' The implementation of the MIB module using this textual convention does not recognize the type of target. 'interface' The target is a physical, logical, or virtual interface represented by an ifEntry (defined by the IF-MIB). An implementation must ensure that DynamicTemplateTargetType object and any associated DynamicTemplateTargetId objects are consistent. An attempt to set a DynamicTemplateTargetType object to a value inconsistent with the associated DynamicTemplateTargetId object must result in a response with an error-status of 'inconsistentValue'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("interface", 2))

class DynamicTemplateTargetId(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "An binary string-value in network byte order identifying a target associated with one or more dynamic templates. An implementation must interpret a DynamicTemplateTargetId value within the context of a DynamicTemplateTargetType. Every usage of the DynamicTemplateTargetId textual convention must have a corresponding object specifying the DynamicTemplateType that provides this context. It is most appropriate that a MIB module logical registers the DynamicTemplateType object before the use of the DynamicTemplateTargetId textual convention within the same logical row. The value of a DynamicTemplateTargetId object must always be consistent with the value of the associated DynamicTemplateTargetType object. An attempt to set a DynamicTemplateTargetId object to a value inconsistent with the with the associated DynamicTemplateTargetType object must result in a response with an error-status of 'inconsistentValue'. If the DynamicTemplateTargetType is 'interface', then the representation of DynamicTemplateTargetId is as below octets contents encoding 1-4 ifIndex network-byte order"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

mibBuilder.exportSymbols("CISCO-DYNAMIC-TEMPLATE-TC-MIB", DynamicTemplateName=DynamicTemplateName, DynamicTemplateType=DynamicTemplateType, ciscoDynamicTemplateTcMIB=ciscoDynamicTemplateTcMIB, DynamicTemplateTargetId=DynamicTemplateTargetId, PYSNMP_MODULE_ID=ciscoDynamicTemplateTcMIB, DynamicTemplateTargetType=DynamicTemplateTargetType)
