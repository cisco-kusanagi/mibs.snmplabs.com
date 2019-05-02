#
# PySNMP MIB module CISCO-CBP-TARGET-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CBP-TARGET-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:52:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, NotificationType, Gauge32, Integer32, Unsigned32, iso, Bits, ObjectIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "NotificationType", "Gauge32", "Integer32", "Unsigned32", "iso", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCbpTargetTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 511))
ciscoCbpTargetTCMIB.setRevisions(('2006-03-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setLastUpdated('200603240000Z')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: cs-qos@cisco.com, cs-c3pl@cisco.com')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setDescription('This MIB module defines Textual Conventions for representing targets which have class based policy mappings. A target can be any logical interface or entity to which a class based policy is able to be associated.')
class CcbptTargetType(TextualConvention, Integer32):
    description = 'A Textual Convention that represents a type of target. genIf(1) A target of type interface defined by CcbptTargetIdIf Textual Convention. atmPvc(2) A target of type ATM PVC defined by the CcbptTargetIdAtmPvc Textual Convention. frDlci(3) A target of type Frame Relay DLCI defined by the CcbptTargetIdFrDlci Textual Convention. entity(4) A target of type entity defined by the CcbptTargetIdEntity Textual Convention. This target type is used to indicate the attachment of a Class Based Policy to a physical entity. fwZone(5) A target of type Firewall Security Zone defined by the CcbptTargetIdNameString Textual Convention. fwZonePair(6) A target of type Firewall Security Zone defined by the CcbptTargetIdNameString Textual Convention. aaaSession(7) A target of type AAA Session define by the CcbptTargetIdAaaSession Textual Convention. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("genIf", 1), ("atmPvc", 2), ("frDlci", 3), ("entity", 4), ("fwZone", 5), ("fwZonePair", 6), ("aaaSession", 7))

class CcbptTargetDirection(TextualConvention, Integer32):
    description = 'A Textual Convention that represents a direction for a target. undirected(1) Indicates that direction has no meaning relative to the target. input(2) Refers to the input direction relative to the target. output(3) Refers to the output direction relative to the target. inOut(4) Refers to both the input and output directions relative to the target. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("undirected", 1), ("input", 2), ("output", 3), ("inOut", 4))

class CcbptTargetId(TextualConvention, OctetString):
    description = 'Denotes a generic target ID. A CcbptTargetId value is always interpreted within the context of an CcbptTargetType value. Every usage of the CcbptTargetId Textual Convention is required to specify the CcbptTargetType object which provides the context. It is suggested that the CcbptTargetType object is logically registered before the object(s) which use the CcbptTargetId Textual Convention if they appear in the same logical row. The value of an CcbptTargetId object must always be consistent with the value of the associated CcbptTargetType object. Attempts to set a CcbptTargetId object to a value which is inconsistent with the associated targetType must fail with an inconsistentValue error. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdIf(TextualConvention, OctetString):
    description = 'Represents an interface target: octets contents encoding 1-4 ifIndex network-byte order '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdAtmPvc(TextualConvention, OctetString):
    description = 'Represents an ATM PVC target: octets contents encoding 1-4 ifIndex network-byte order 5-6 atmVclVpi network-byte order 7-8 atmVclVci network-byte order '
    status = 'current'
    displayHint = '4d:2d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CcbptTargetIdFrDlci(TextualConvention, OctetString):
    description = 'Represents a Frame Relay DLCI target: octets contents encoding 1-4 ifIndex network-byte order 5-6 DlciNumber network-byte order '
    status = 'current'
    displayHint = '4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CcbptTargetIdEntity(TextualConvention, OctetString):
    description = 'Represents the entPhysicalIndex of the physical entity target: octets contents encoding 1-4 entPhysicalIndex network-byte order '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdNameString(TextualConvention, OctetString):
    description = 'Represents a target identified by a name string. This is the ASCII name identifying this target. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdAaaSession(TextualConvention, OctetString):
    description = 'Represents a AAA Session target: octets contents encoding 1-4 casnSessionId network-byte order '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptPolicySourceType(TextualConvention, Integer32):
    description = 'This Textual Convention represents the types of sources of policies. ciscoCbQos(1) Cisco Class Based QOS policy source. The source of the policy is Cisco Class Based QOS specific. ciscoCbpCommon(2) Cisco Common Class Based Policy type. The source of the policy is Cisco Common Class Based. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ciscoCbQos", 1), ("ciscoCbpBase", 2))

class CcbptPolicyIdentifier(TextualConvention, Unsigned32):
    description = 'A type specific, arbitrary identifier uniquely given to a policy-map attachment to a target. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CcbptPolicyIdentifierOrZero(TextualConvention, Unsigned32):
    description = 'This refers to CcbptPolicyIdentifier values, as applies, or 0. The behavior of the value of 0 should be described in the description of objects using this type. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("CISCO-CBP-TARGET-TC-MIB", PYSNMP_MODULE_ID=ciscoCbpTargetTCMIB, CcbptTargetIdEntity=CcbptTargetIdEntity, CcbptPolicySourceType=CcbptPolicySourceType, CcbptTargetDirection=CcbptTargetDirection, CcbptTargetIdAaaSession=CcbptTargetIdAaaSession, ciscoCbpTargetTCMIB=ciscoCbpTargetTCMIB, CcbptTargetIdIf=CcbptTargetIdIf, CcbptTargetIdFrDlci=CcbptTargetIdFrDlci, CcbptTargetId=CcbptTargetId, CcbptTargetIdNameString=CcbptTargetIdNameString, CcbptTargetType=CcbptTargetType, CcbptTargetIdAtmPvc=CcbptTargetIdAtmPvc, CcbptPolicyIdentifierOrZero=CcbptPolicyIdentifierOrZero, CcbptPolicyIdentifier=CcbptPolicyIdentifier)
