#
# PySNMP MIB module ENTERASYS-VLAN-AUTHORIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-VLAN-AUTHORIZATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, IpAddress, iso, ModuleIdentity, Bits, Counter32, Counter64, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Bits", "Counter32", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysVlanAuthorizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48))
etsysVlanAuthorizationMIB.setRevisions(('2004-06-02 19:22',))
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setLastUpdated('200406021922Z')
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setOrganization('Enterasys Networks, Inc')
class VlanAuthEgressStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("tagged", 2), ("untagged", 3), ("dynamic", 4))

etsysVlanAuthorizationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1))
etsysVlanAuthorizationSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1))
etsysVlanAuthorizationPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2))
etsysVlanAuthorizationEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationEnable.setStatus('current')
etsysVlanAuthorizationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1), )
if mibBuilder.loadTexts: etsysVlanAuthorizationTable.setStatus('current')
etsysVlanAuthorizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEntry"))
etsysVlanAuthorizationEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysVlanAuthorizationEntry.setStatus('current')
etsysVlanAuthorizationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationStatus.setStatus('current')
etsysVlanAuthorizationAdminEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 2), VlanAuthEgressStatus().clone('untagged')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationAdminEgress.setStatus('current')
etsysVlanAuthorizationOperEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 3), VlanAuthEgressStatus().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationOperEgress.setStatus('current')
etsysVlanAuthorizationVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationVlanID.setStatus('current')
etsysVlanAuthorizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2))
etsysVlanAuthorizationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1))
etsysVlanAuthorizationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2))
etsysVlanAuthorizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEnable"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationStatus"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationAdminEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationOperEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationVlanID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationGroup = etsysVlanAuthorizationGroup.setStatus('current')
etsysVlanAuthorizationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationCompliance = etsysVlanAuthorizationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-VLAN-AUTHORIZATION-MIB", PYSNMP_MODULE_ID=etsysVlanAuthorizationMIB, etsysVlanAuthorizationGroups=etsysVlanAuthorizationGroups, etsysVlanAuthorizationMIB=etsysVlanAuthorizationMIB, VlanAuthEgressStatus=VlanAuthEgressStatus, etsysVlanAuthorizationEntry=etsysVlanAuthorizationEntry, etsysVlanAuthorizationObjects=etsysVlanAuthorizationObjects, etsysVlanAuthorizationStatus=etsysVlanAuthorizationStatus, etsysVlanAuthorizationCompliances=etsysVlanAuthorizationCompliances, etsysVlanAuthorizationOperEgress=etsysVlanAuthorizationOperEgress, etsysVlanAuthorizationCompliance=etsysVlanAuthorizationCompliance, etsysVlanAuthorizationAdminEgress=etsysVlanAuthorizationAdminEgress, etsysVlanAuthorizationGroup=etsysVlanAuthorizationGroup, etsysVlanAuthorizationSystem=etsysVlanAuthorizationSystem, etsysVlanAuthorizationEnable=etsysVlanAuthorizationEnable, etsysVlanAuthorizationConformance=etsysVlanAuthorizationConformance, etsysVlanAuthorizationTable=etsysVlanAuthorizationTable, etsysVlanAuthorizationPorts=etsysVlanAuthorizationPorts, etsysVlanAuthorizationVlanID=etsysVlanAuthorizationVlanID)
