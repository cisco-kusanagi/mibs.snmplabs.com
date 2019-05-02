#
# PySNMP MIB module TRAPEZE-NETWORKS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-PORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Gauge32, Counter64, Counter32, iso, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Gauge32", "Counter64", "Counter32", "iso", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TrpzPhysPortNumber, TrpzPhysPortNumberOrZero = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumber", "TrpzPhysPortNumberOrZero")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 6))
trpzPortMib.setRevisions(('2008-10-23 00:10', '2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzPortMib.setRevisionsDescriptions(("v1.2.0: Factored out the 'TrpzPhysPortNumber' textual convention (moved to the new module Basic TC). Added in Basic TC MIB an extension of 'TrpzPhysPortNumber' to permit a value of zero. The new textual convention is 'TrpzPhysPortNumberOrZero'. Using it in this MIB because 'trpzPortConfigTrunkMaster' must be zero for a port that is not part of any port group. This will be published in 7.1 release.", 'v1.1.0: Clarified descriptions', 'v1.0.1: Fixed imports and compliance group', 'v1.0: Initial version, for 5.0 release',))
if mibBuilder.loadTexts: trpzPortMib.setLastUpdated('200810230010Z')
if mibBuilder.loadTexts: trpzPortMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzPortMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzPortMib.setDescription("Port information MIB. Copyright 2006-2008 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzPortMode(TextualConvention, Integer32):
    description = 'Enumeration for the port mode (administratively controlled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class TrpzPortPoeMode(TextualConvention, Integer32):
    description = 'Enumeration for the port PoE supply configuration: the availability of Power over Ethernet is administratively controlled, can be enabled or disabled. Some ports may not have the Power over Ethernet hardware: they should always appear as disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

trpzPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1))
trpzPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1))
trpzPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: trpzPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigTable.setDescription('Port configuration table')
trpzPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortNumber"))
if mibBuilder.loadTexts: trpzPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigEntry.setDescription('Port configuration entry')
trpzPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 1), TrpzPhysPortNumber())
if mibBuilder.loadTexts: trpzPortConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigPortNumber.setDescription('Physical Port Number')
trpzPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 2), TrpzPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPortMode.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigPortMode.setDescription('Indicates whether this port is configured for directly attached AP, as network port, or for wired auth.')
trpzPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 3), TrpzPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigPoeMode.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigPoeMode.setDescription('Indicates whether this port is configured to supply PoE (Power over Ethernet).')
trpzPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 1, 1, 1, 4), TrpzPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzPortConfigTrunkMaster.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigTrunkMaster.setDescription('The master port of the group this port belongs to (identified by the physical port number). A zero value means information is not available (usually if this port is not part of any port group).')
trpzPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2))
trpzPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1))
trpzPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2))
trpzPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortCompliance = trpzPortCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzPortCompliance.setDescription('The compliance statement for devices that implement the Port MIB.')
trpzPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 6, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPortMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigPoeMode"), ("TRAPEZE-NETWORKS-PORT-MIB", "trpzPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzPortConfigGroup = trpzPortConfigGroup.setStatus('current')
if mibBuilder.loadTexts: trpzPortConfigGroup.setDescription('Mandatory group of objects implemented to provide Port configuration info.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-PORT-MIB", trpzPortGroups=trpzPortGroups, TrpzPortMode=TrpzPortMode, trpzPortConfigPortMode=trpzPortConfigPortMode, trpzPortDataObjects=trpzPortDataObjects, trpzPortConfigEntry=trpzPortConfigEntry, trpzPortCompliances=trpzPortCompliances, trpzPortObjects=trpzPortObjects, TrpzPortPoeMode=TrpzPortPoeMode, trpzPortConfigPoeMode=trpzPortConfigPoeMode, trpzPortConfigGroup=trpzPortConfigGroup, trpzPortMib=trpzPortMib, trpzPortConformance=trpzPortConformance, trpzPortConfigTable=trpzPortConfigTable, PYSNMP_MODULE_ID=trpzPortMib, trpzPortConfigTrunkMaster=trpzPortConfigTrunkMaster, trpzPortCompliance=trpzPortCompliance, trpzPortConfigPortNumber=trpzPortConfigPortNumber)
