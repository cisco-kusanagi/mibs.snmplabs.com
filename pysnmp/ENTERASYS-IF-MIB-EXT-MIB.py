#
# PySNMP MIB module ENTERASYS-IF-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IF-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Integer32, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress, TimeTicks, iso, Bits, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "iso", "Bits", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysIfMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57))
etsysIfMibExtMIB.setRevisions(('2011-05-12 14:15', '2005-01-13 21:35',))
if mibBuilder.loadTexts: etsysIfMibExtMIB.setLastUpdated('201105121415Z')
if mibBuilder.loadTexts: etsysIfMibExtMIB.setOrganization('Enterasys Networks, Inc.')
class EtsysIfOperStatusCauses(TextualConvention, Bits):
    reference = "RFC 2863, 'The Interfaces Group MIB' ENTERASYS-LINK-FLAP-MIB ENTERASYS-FLOW-LIMITING-MIB ENTERASYS-POLICY-PROFILE-MIB ENTERASYS-CLASS-OF-SERVICE-MIB ENTERASYS-ETH-OAM-EXT-MIB IEEE Std. 802.1X-2001 IEEE Std. 802.3-2002"
    status = 'current'
    namedValues = NamedValues(("adminStatus", 0), ("linkLoss", 1), ("linkFlap", 2), ("self", 3), ("initialization", 4), ("flowLimiting", 5), ("policy", 6), ("classOfService", 7), ("ieee8021x", 8), ("ieee8023lag", 9), ("enetOam", 10), ("enetOamLb", 11))

etsysIfMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1))
etsysIfMibExtSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1))
etsysIfMibExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2))
etsysIfOperStateLinkChange = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfOperStateLinkChange.setStatus('current')
etsysInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1), )
if mibBuilder.loadTexts: etsysInterfaceExtTable.setStatus('current')
etsysInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1), )
ifEntry.registerAugmentions(("ENTERASYS-IF-MIB-EXT-MIB", "etsysInterfaceExtEntry"))
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: etsysInterfaceExtEntry.setStatus('current')
etsysIfOperStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1, 1), EtsysIfOperStatusCauses()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIfOperStatusCause.setStatus('current')
etsysIfMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2))
etsysIfMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1))
etsysIfMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2))
etsysIfMibExtOperLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStateLinkChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperLinkGroup = etsysIfMibExtOperLinkGroup.setStatus('current')
etsysIfMibExtOperStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 2)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStatusCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperStatusGroup = etsysIfMibExtOperStatusGroup.setStatus('current')
etsysIfMibExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperLinkGroup"), ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtCompliance = etsysIfMibExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IF-MIB-EXT-MIB", etsysIfMibExtObjects=etsysIfMibExtObjects, etsysIfMibExtInterface=etsysIfMibExtInterface, etsysIfMibExtOperLinkGroup=etsysIfMibExtOperLinkGroup, etsysIfMibExtGroups=etsysIfMibExtGroups, PYSNMP_MODULE_ID=etsysIfMibExtMIB, etsysInterfaceExtTable=etsysInterfaceExtTable, etsysIfOperStatusCause=etsysIfOperStatusCause, EtsysIfOperStatusCauses=EtsysIfOperStatusCauses, etsysIfMibExtOperStatusGroup=etsysIfMibExtOperStatusGroup, etsysInterfaceExtEntry=etsysInterfaceExtEntry, etsysIfMibExtCompliance=etsysIfMibExtCompliance, etsysIfOperStateLinkChange=etsysIfOperStateLinkChange, etsysIfMibExtConformance=etsysIfMibExtConformance, etsysIfMibExtMIB=etsysIfMibExtMIB, etsysIfMibExtSystem=etsysIfMibExtSystem, etsysIfMibExtCompliances=etsysIfMibExtCompliances)
