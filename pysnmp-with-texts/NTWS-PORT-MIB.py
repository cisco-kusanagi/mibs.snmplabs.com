#
# PySNMP MIB module NTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-PORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NtwsPhysPortNumberOrZero, NtwsPhysPortNumber = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumberOrZero", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Counter64, Gauge32, Counter32, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6))
ntwsPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2007-08-16 00:02', '2006-11-09 00:01', '2006-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsPortMib.setRevisionsDescriptions(("v1.2.0: Factored out the 'NtwsPhysPortNumber' textual convention (moved to the new module Basic TC). Added in Basic TC MIB an extension of 'NtwsPhysPortNumber' to permit a value of zero. The new textual convention is 'NtwsPhysPortNumberOrZero'. Using it in this MIB because 'ntwsPortConfigTrunkMaster' must be zero for a port that is not part of any port group.", 'v1.1.0: Clarified descriptions', 'v1.0.2, MRT v2: Made changes in order to make MIB compile cleanly and comply with corporate MIB conventions.', 'v1.0.1: Fixed imports and compliance group', 'v1.0: Initial version',))
if mibBuilder.loadTexts: ntwsPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: ntwsPortMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsPortMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsPortMib.setDescription("Port information MIB. Copyright 2008 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsPortMode(TextualConvention, Integer32):
    description = 'Enumeration for the port mode (administratively controlled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class NtwsPortPoeMode(TextualConvention, Integer32):
    description = 'Enumeration for the port PoE supply configuration: the availability of Power over Ethernet is administratively controlled, can be enabled or disabled. Some ports may not have the Power over Ethernet hardware: they should always appear as disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

ntwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1))
ntwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1))
ntwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigTable.setDescription('Port configuration table')
ntwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-PORT-MIB", "ntwsPortConfigPortNumber"))
if mibBuilder.loadTexts: ntwsPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigEntry.setDescription('Port configuration entry')
ntwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 1), NtwsPhysPortNumber())
if mibBuilder.loadTexts: ntwsPortConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigPortNumber.setDescription('Physical Port Number')
ntwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 2), NtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPortMode.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigPortMode.setDescription('Indicates whether this port is configured for directly attached AP, as network port, or for wired auth.')
ntwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 3), NtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigPoeMode.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigPoeMode.setDescription('Indicates whether this port is configured to supply PoE (Power over Ethernet).')
ntwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 1, 1, 1, 4), NtwsPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsPortConfigTrunkMaster.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigTrunkMaster.setDescription('The master port of the group this port belongs to (identified by the physical port number). A zero value means information is not available (usually if this port is not part of any port group).')
ntwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2))
ntwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1))
ntwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2))
ntwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 1, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortCompliance = ntwsPortCompliance.setStatus('current')
if mibBuilder.loadTexts: ntwsPortCompliance.setDescription('The compliance statement for devices that implement the Port MIB.')
ntwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 6, 1, 2, 2, 1)).setObjects(("NTWS-PORT-MIB", "ntwsPortConfigPortMode"), ("NTWS-PORT-MIB", "ntwsPortConfigPoeMode"), ("NTWS-PORT-MIB", "ntwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsPortConfigGroup = ntwsPortConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ntwsPortConfigGroup.setDescription('Mandatory group of objects implemented to provide Port configuration info.')
mibBuilder.exportSymbols("NTWS-PORT-MIB", ntwsPortConfigPoeMode=ntwsPortConfigPoeMode, ntwsPortConformance=ntwsPortConformance, ntwsPortMib=ntwsPortMib, ntwsPortConfigGroup=ntwsPortConfigGroup, ntwsPortGroups=ntwsPortGroups, ntwsPortCompliance=ntwsPortCompliance, NtwsPortMode=NtwsPortMode, ntwsPortDataObjects=ntwsPortDataObjects, ntwsPortConfigPortNumber=ntwsPortConfigPortNumber, ntwsPortObjects=ntwsPortObjects, ntwsPortConfigTrunkMaster=ntwsPortConfigTrunkMaster, ntwsPortConfigEntry=ntwsPortConfigEntry, NtwsPortPoeMode=NtwsPortPoeMode, PYSNMP_MODULE_ID=ntwsPortMib, ntwsPortConfigPortMode=ntwsPortConfigPortMode, ntwsPortConfigTable=ntwsPortConfigTable, ntwsPortCompliances=ntwsPortCompliances)
