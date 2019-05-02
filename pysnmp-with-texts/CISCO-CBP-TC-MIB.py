#
# PySNMP MIB module CISCO-CBP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CBP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:52:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, NotificationType, IpAddress, MibIdentifier, Bits, Integer32, iso, ObjectIdentity, Counter64, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "MibIdentifier", "Bits", "Integer32", "iso", "ObjectIdentity", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCbpTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 662))
ciscoCbpTcMIB.setRevisions(('2008-06-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCbpTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoCbpTcMIB.setLastUpdated('200806240000Z')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setDescription('This MIB module defines textual conventions used by the CISCO-CBP-BASE-CFG-MIB, CISCO-CBP-BASE-MON-MIB, and any MIB modules extending these MIB modules.')
class CbpElementName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = "A string-value that identifies an element used to specify a class-based policy. The semantics of the string-value are the same those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB [RFC3411]. Observe that the null string is reserved for cases when an instance of an object needs to specify 'no element'."
    status = 'current'
    displayHint = '127a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class CbpElementIdentifier(TextualConvention, Unsigned32):
    description = 'A positive, non-zero integer-value that uniquely identifies an element used to specify a class-based policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpElementIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the CbpElementIdentifier textual convention, which permits the value '0'. The use of the value '0' is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of its use."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpInstanceIdentifier(TextualConvention, Unsigned32):
    description = 'A positive, non-zero integer-value that uniquely identifies an instance of an element used to define a class-based policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the CbpInstanceIdentifier textual convention, which permits the value '0'. The use of the value '0' is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of its use."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpExecutionPriority(TextualConvention, Unsigned32):
    description = "An positive, integer-value denoting the relative priority of an element, where '1' represents the highest priority and greater values represent lower priorities. The priority assigned to an element determines the order in which the system processes the elements relative to like elements having the same parent, where the system processes elements having a greater priority first. The system processes sibling elements having the same priority in the order they were created."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpExecutionStrategy(TextualConvention, Integer32):
    description = "An enumerated integer-value describing how to execute an ordered set of actions: 'other' The implementation of the MIB using this textual convention does not recognize the specified execution strategy. 'doUntilSuccess' The system sequentially executes the actions in the set until one succeeds. 'doUntilFailure' The system sequentially executes the actions in the set until one fails. 'doAll' The system sequentially executes all actions in the set, regardless of whether they succeed or fail."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("doUntilSuccess", 2), ("doUntilFailure", 3), ("doAll", 4))

mibBuilder.exportSymbols("CISCO-CBP-TC-MIB", CbpInstanceIdentifierOrZero=CbpInstanceIdentifierOrZero, CbpElementIdentifierOrZero=CbpElementIdentifierOrZero, CbpElementIdentifier=CbpElementIdentifier, CbpExecutionPriority=CbpExecutionPriority, CbpElementName=CbpElementName, PYSNMP_MODULE_ID=ciscoCbpTcMIB, CbpExecutionStrategy=CbpExecutionStrategy, ciscoCbpTcMIB=ciscoCbpTcMIB, CbpInstanceIdentifier=CbpInstanceIdentifier)
