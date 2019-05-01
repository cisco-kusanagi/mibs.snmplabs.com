#
# PySNMP MIB module RBTWS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-PORT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Bits, Counter32, iso, Counter64, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Bits", "Counter32", "iso", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsPortMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6))
rbtwsPortMib.setRevisions(('2008-05-19 00:04', '2006-11-09 00:01', '2006-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsPortMib.setRevisionsDescriptions(('v1.1.0: Clarified descriptions', 'v1.0.1: Fixed imports and compliance group', 'v1.0: Initial version, for 5.0 release',))
if mibBuilder.loadTexts: rbtwsPortMib.setLastUpdated('200805191722Z')
if mibBuilder.loadTexts: rbtwsPortMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsPortMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsPortMib.setDescription("Port information MIB. Copyright 2008 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class RbtwsPhysPortNumber(TextualConvention, Unsigned32):
    description = 'Physical port number'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class RbtwsPortMode(TextualConvention, Integer32):
    description = 'Enumeration for the port mode (administratively controlled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("directAttachAP", 1), ("networkPort", 2), ("wired", 3))

class RbtwsPortPoeMode(TextualConvention, Integer32):
    description = 'Enumeration for the port PoE supply configuration: the availability of Power over Ethernet is administratively controlled, can be enabled or disabled. Some ports may not have the Power over Ethernet hardware: they should always appear as disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("poeEnable", 1), ("poeDisable", 2))

rbtwsPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1))
rbtwsPortDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1))
rbtwsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigTable.setDescription('Port configuration table')
rbtwsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-PORT-MIB", "rbtwsPortConfigPortNumber"))
if mibBuilder.loadTexts: rbtwsPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigEntry.setDescription('Port configuration entry')
rbtwsPortConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 1), RbtwsPhysPortNumber())
if mibBuilder.loadTexts: rbtwsPortConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigPortNumber.setDescription('Physical Port Number')
rbtwsPortConfigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 2), RbtwsPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPortMode.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigPortMode.setDescription('Indicates whether this port is configured for directly attached AP, as network port, or for wired auth.')
rbtwsPortConfigPoeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 3), RbtwsPortPoeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigPoeMode.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigPoeMode.setDescription('Indicates whether this port is configured to supply PoE (Power over Ethernet).')
rbtwsPortConfigTrunkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 1, 1, 1, 4), RbtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsPortConfigTrunkMaster.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigTrunkMaster.setDescription('The master port of the group this port belongs to (identified by the physical port number). A zero value means information is not available (usually if this port is not part of any port group).')
rbtwsPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2))
rbtwsPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1))
rbtwsPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2))
rbtwsPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 1, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortCompliance = rbtwsPortCompliance.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortCompliance.setDescription('The compliance statement for devices that implement the Port MIB.')
rbtwsPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 6, 1, 2, 2, 1)).setObjects(("RBTWS-PORT-MIB", "rbtwsPortConfigPortMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigPoeMode"), ("RBTWS-PORT-MIB", "rbtwsPortConfigTrunkMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsPortConfigGroup = rbtwsPortConfigGroup.setStatus('current')
if mibBuilder.loadTexts: rbtwsPortConfigGroup.setDescription('Mandatory group of objects implemented to provide Port configuration info.')
mibBuilder.exportSymbols("RBTWS-PORT-MIB", PYSNMP_MODULE_ID=rbtwsPortMib, rbtwsPortMib=rbtwsPortMib, RbtwsPhysPortNumber=RbtwsPhysPortNumber, rbtwsPortConfigGroup=rbtwsPortConfigGroup, rbtwsPortConfigEntry=rbtwsPortConfigEntry, rbtwsPortConformance=rbtwsPortConformance, rbtwsPortConfigTable=rbtwsPortConfigTable, RbtwsPortMode=RbtwsPortMode, rbtwsPortConfigTrunkMaster=rbtwsPortConfigTrunkMaster, rbtwsPortCompliances=rbtwsPortCompliances, rbtwsPortGroups=rbtwsPortGroups, rbtwsPortObjects=rbtwsPortObjects, RbtwsPortPoeMode=RbtwsPortPoeMode, rbtwsPortCompliance=rbtwsPortCompliance, rbtwsPortConfigPortNumber=rbtwsPortConfigPortNumber, rbtwsPortConfigPortMode=rbtwsPortConfigPortMode, rbtwsPortDataObjects=rbtwsPortDataObjects, rbtwsPortConfigPoeMode=rbtwsPortConfigPoeMode)
