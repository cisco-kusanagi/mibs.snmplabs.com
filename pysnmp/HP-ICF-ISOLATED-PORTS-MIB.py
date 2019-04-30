#
# PySNMP MIB module HP-ICF-ISOLATED-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-ISOLATED-PORTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qVlanStaticEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter64, Gauge32, ObjectIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, TimeTicks, MibIdentifier, NotificationType, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "TimeTicks", "MibIdentifier", "NotificationType", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfDot1qIsolatedPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109))
hpicfDot1qIsolatedPorts.setRevisions(('2014-04-14 00:00',))
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setLastUpdated('201404140000Z')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setOrganization('HP Networking')
hpicfDot1qIsolatedPortConfigurationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1))
hpicfDot1qIsolatedPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2))
hpicfDot1qIsolatedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1), )
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsTable.setStatus('current')
hpicfDot1qIsolatedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortsEntry"))
hpicfDot1qIsolatedPortsEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsEntry.setStatus('current')
hpicfDot1qVlanStaticIsolatedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1, 1), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDot1qVlanStaticIsolatedPorts.setStatus('current')
hpicfDot1qIsolatedPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1))
hpicfDot1qIsolatedPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2))
hpicfDot1qIsolatedPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortCompliance = hpicfDot1qIsolatedPortCompliance.setStatus('current')
hpicfDot1qIsolatedPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qVlanStaticIsolatedPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortGroup = hpicfDot1qIsolatedPortGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-ISOLATED-PORTS-MIB", hpicfDot1qIsolatedPorts=hpicfDot1qIsolatedPorts, hpicfDot1qIsolatedPortCompliance=hpicfDot1qIsolatedPortCompliance, hpicfDot1qIsolatedPortsEntry=hpicfDot1qIsolatedPortsEntry, hpicfDot1qIsolatedPortGroups=hpicfDot1qIsolatedPortGroups, PYSNMP_MODULE_ID=hpicfDot1qIsolatedPorts, hpicfDot1qIsolatedPortCompliances=hpicfDot1qIsolatedPortCompliances, hpicfDot1qIsolatedPortConfigurationObjects=hpicfDot1qIsolatedPortConfigurationObjects, hpicfDot1qIsolatedPortGroup=hpicfDot1qIsolatedPortGroup, hpicfDot1qIsolatedPortConformance=hpicfDot1qIsolatedPortConformance, hpicfDot1qVlanStaticIsolatedPorts=hpicfDot1qVlanStaticIsolatedPorts, hpicfDot1qIsolatedPortsTable=hpicfDot1qIsolatedPortsTable)
