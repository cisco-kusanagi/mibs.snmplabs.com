#
# PySNMP MIB module RIVERSTONE-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-ATM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
dot1dTpFdbAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dTpFdbAddress")
riverstoneMibs, = mibBuilder.importSymbols("RSTONE-SMI-MIB", "riverstoneMibs")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, Gauge32, Bits, TimeTicks, ObjectIdentity, Counter64, Counter32, NotificationType, IpAddress, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "IpAddress", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsAtmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 16))
rsAtmMib.setRevisions(('2001-01-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsAtmMib.setRevisionsDescriptions(('Initial version of of Riverstone extensions to ATM Management.',))
if mibBuilder.loadTexts: rsAtmMib.setLastUpdated('200101310000Z')
if mibBuilder.loadTexts: rsAtmMib.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsAtmMib.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsAtmMib.setDescription('This MIB module defines enterprise extensions to IETF Standard MIB modules. rsAtmFdbObjects group defines a mapping from a MAC address to the ATM PVC on which it was learned. Copyright (C) Riverstone Networks, Inc 2001')
rsAtmFdbObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1))
rsAtmFdbMacsLearned = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbMacsLearned.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbMacsLearned.setDescription('Number of MAC addresses learned on ATM line cards system.')
rsAtmFdbTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2), )
if mibBuilder.loadTexts: rsAtmFdbTable.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbTable.setDescription('This table provides a mapping of a MAC address to the bridge port, plus Virtual Path Identifier/Virtual Channel Identifier (VPI/VCI) on which it was learned. A row will appear in this table for each row in dot1dTpFdbTable that maps to a bridge port (dot1dBasePortNum) which is of type ATM ifType(37). Rows in this table share the same fate as rows in dot1dTpFdbTable.')
rsAtmFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
if mibBuilder.loadTexts: rsAtmFdbEntry.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbEntry.setDescription('An entry in the table shares the same fate as an entry in dot1dTpFdbTable and uses the same indexing.')
rsAtmFdbVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 1), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbVpi.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbVpi.setDescription('The Virtual Path Identifier on which this MAC address was learned.')
rsAtmFdbVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 2), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbVci.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbVci.setDescription('The Virtual Channel Identifier on which this MAC address was learned.')
rsAtmFdbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10))
rsAtmFdbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1))
rsAtmFdbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2))
rsAtmFdbBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1, 1)).setObjects(("RIVERSTONE-ATM-MIB", "rsAtmFdbMacsLearned"), ("RIVERSTONE-ATM-MIB", "rsAtmFdbVpi"), ("RIVERSTONE-ATM-MIB", "rsAtmFdbVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAtmFdbBaseGroup = rsAtmFdbBaseGroup.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbBaseGroup.setDescription('A collection of objects providing a mapping between a MAC address and the ATM vpi/vci it was learned on.')
rsAtmFdbMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2, 1)).setObjects(("RIVERSTONE-ATM-MIB", "rsAtmFdbBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAtmFdbMibCompliance = rsAtmFdbMibCompliance.setStatus('current')
if mibBuilder.loadTexts: rsAtmFdbMibCompliance.setDescription('The compliance statement for device support of extension to dot1dTpFdbTable for ATM interfaces.')
mibBuilder.exportSymbols("RIVERSTONE-ATM-MIB", rsAtmFdbCompliances=rsAtmFdbCompliances, rsAtmFdbVpi=rsAtmFdbVpi, rsAtmFdbConformance=rsAtmFdbConformance, rsAtmFdbMibCompliance=rsAtmFdbMibCompliance, rsAtmFdbVci=rsAtmFdbVci, rsAtmFdbEntry=rsAtmFdbEntry, rsAtmFdbGroups=rsAtmFdbGroups, rsAtmFdbTable=rsAtmFdbTable, rsAtmFdbBaseGroup=rsAtmFdbBaseGroup, rsAtmMib=rsAtmMib, rsAtmFdbObjects=rsAtmFdbObjects, PYSNMP_MODULE_ID=rsAtmMib, rsAtmFdbMacsLearned=rsAtmFdbMacsLearned)
