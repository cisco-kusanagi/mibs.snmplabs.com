#
# PySNMP MIB module HP-ICF-ISOLATED-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-ISOLATED-PORTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
dot1qVlanStaticEntry, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStaticEntry", "PortList")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Counter64, ModuleIdentity, TimeTicks, Counter32, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfDot1qIsolatedPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109))
hpicfDot1qIsolatedPorts.setRevisions(('2014-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setRevisionsDescriptions(('Initial Revision.',))
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setLastUpdated('201404140000Z')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPorts.setDescription('This MIB module contains the HP proprietary objects for configuring and managing the isolated ports on the VLAN.')
hpicfDot1qIsolatedPortConfigurationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1))
hpicfDot1qIsolatedPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2))
hpicfDot1qIsolatedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1), )
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsTable.setDescription('A table that contains the information about all the isolated ports of the VLANs on a device. Each VLAN can have a single isolate-list. The isolate-list holds a list of isolated ports that cannot forward the traffic to other isolated ports on the same VLAN.')
hpicfDot1qIsolatedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortsEntry"))
hpicfDot1qIsolatedPortsEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortsEntry.setDescription('An entry in the table that contains the information about the isolated ports of a VLAN.')
hpicfDot1qVlanStaticIsolatedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 1, 1, 1, 1), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDot1qVlanStaticIsolatedPorts.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qVlanStaticIsolatedPorts.setDescription('This object contains a list of isolated ports in the VLAN. Traffic received on isolated ports will not be forwarded to other isolated ports in the VLAN, only to non-isolated ports.')
hpicfDot1qIsolatedPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1))
hpicfDot1qIsolatedPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2))
hpicfDot1qIsolatedPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 1, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qIsolatedPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortCompliance = hpicfDot1qIsolatedPortCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortCompliance.setDescription('The compliance statement for the Isolated Ports.')
hpicfDot1qIsolatedPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109, 2, 2, 1)).setObjects(("HP-ICF-ISOLATED-PORTS-MIB", "hpicfDot1qVlanStaticIsolatedPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDot1qIsolatedPortGroup = hpicfDot1qIsolatedPortGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qIsolatedPortGroup.setDescription('The collection of objects that provides the information about the isolated ports of the VLANs on a device.')
mibBuilder.exportSymbols("HP-ICF-ISOLATED-PORTS-MIB", hpicfDot1qIsolatedPortConfigurationObjects=hpicfDot1qIsolatedPortConfigurationObjects, hpicfDot1qIsolatedPortsTable=hpicfDot1qIsolatedPortsTable, hpicfDot1qIsolatedPortCompliances=hpicfDot1qIsolatedPortCompliances, PYSNMP_MODULE_ID=hpicfDot1qIsolatedPorts, hpicfDot1qVlanStaticIsolatedPorts=hpicfDot1qVlanStaticIsolatedPorts, hpicfDot1qIsolatedPortGroups=hpicfDot1qIsolatedPortGroups, hpicfDot1qIsolatedPortCompliance=hpicfDot1qIsolatedPortCompliance, hpicfDot1qIsolatedPortsEntry=hpicfDot1qIsolatedPortsEntry, hpicfDot1qIsolatedPortGroup=hpicfDot1qIsolatedPortGroup, hpicfDot1qIsolatedPorts=hpicfDot1qIsolatedPorts, hpicfDot1qIsolatedPortConformance=hpicfDot1qIsolatedPortConformance)
