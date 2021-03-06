#
# PySNMP MIB module RIVERSTONE-VLAN-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-VLAN-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, iso, Unsigned32, ModuleIdentity, NotificationType, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "Unsigned32", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier")
TruthValue, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeStamp", "DisplayString")
rsVlanExtensionsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 65))
rsVlanExtensionsMIB.setRevisions(('2004-12-06 00:00', '2002-08-06 00:00',))
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setLastUpdated('200412060000Z')
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setOrganization('Riverstone Networks, Inc')
rsVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1))
rsVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2))
rsVlanStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10))
rsVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1))
rsVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2))
rsPortVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1), )
if mibBuilder.loadTexts: rsPortVlanStatsTable.setStatus('current')
rsPortVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortVlanStatsEntry.setStatus('current')
rsPortVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanInOctets.setStatus('current')
rsPortVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 102), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanOutOctets.setStatus('current')
rsPortVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 103), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanInOverflowOctets.setStatus('current')
rsPortVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 104), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanOutOverflowOctets.setStatus('current')
rsPortVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2), )
if mibBuilder.loadTexts: rsPortVlanHCStatsTable.setStatus('current')
rsPortVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortVlanHCStatsEntry.setStatus('current')
rsPortVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 101), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanHCInOctets.setStatus('current')
rsPortVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 102), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanHCOutOctets.setStatus('current')
rsPortCustomerVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3), )
if mibBuilder.loadTexts: rsPortCustomerVlanStatsTable.setStatus('current')
rsPortCustomerVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortCustomerVlanStatsEntry.setStatus('current')
rsPortCustomerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rsPortCustomerIndex.setStatus('current')
rsPortCustomerVlanInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInFrames.setStatus('current')
rsPortCustomerVlanOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutFrames.setStatus('current')
rsPortCustomerVlanInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInDiscards.setStatus('current')
rsPortCustomerVlanInOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowFrames.setStatus('current')
rsPortCustomerVlanOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowFrames.setStatus('current')
rsPortCustomerVlanInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowDiscards.setStatus('current')
rsPortCustomerVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOctets.setStatus('current')
rsPortCustomerVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOctets.setStatus('current')
rsPortCustomerVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowOctets.setStatus('current')
rsPortCustomerVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowOctets.setStatus('current')
rsPortCustomerVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4), )
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsTable.setStatus('current')
rsPortCustomerVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsEntry.setStatus('current')
rsPortCustomerVlanHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInFrames.setStatus('current')
rsPortCustomerVlanHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutFrames.setStatus('current')
rsPortCustomerVlanHCInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInDiscards.setStatus('current')
rsPortCustomerVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInOctets.setStatus('current')
rsPortCustomerVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutOctets.setStatus('current')
rsCustomerVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5), )
if mibBuilder.loadTexts: rsCustomerVlanStatsTable.setStatus('current')
rsCustomerVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1), ).setIndexNames((0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsCustomerVlanStatsEntry.setStatus('current')
rsCustomerVlanInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInFrames.setStatus('current')
rsCustomerVlanOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutFrames.setStatus('current')
rsCustomerVlanInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInDiscards.setStatus('current')
rsCustomerVlanInOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowFrames.setStatus('current')
rsCustomerVlanOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowFrames.setStatus('current')
rsCustomerVlanInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowDiscards.setStatus('current')
rsCustomerVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOctets.setStatus('current')
rsCustomerVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOctets.setStatus('current')
rsCustomerVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowOctets.setStatus('current')
rsCustomerVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowOctets.setStatus('current')
rsCustomerVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6), )
if mibBuilder.loadTexts: rsCustomerVlanHCStatsTable.setStatus('current')
rsCustomerVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1), ).setIndexNames((0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsCustomerVlanHCStatsEntry.setStatus('current')
rsCustomerVlanHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInFrames.setStatus('current')
rsCustomerVlanHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCOutFrames.setStatus('current')
rsCustomerVlanHCInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInDiscards.setStatus('current')
rsCustomerVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInOctets.setStatus('current')
rsCustomerVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCOutOctets.setStatus('current')
rsVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1, 1)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsVlanCompliance = rsVlanCompliance.setStatus('current')
rsPortVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 1)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanStatsGroup = rsPortVlanStatsGroup.setStatus('current')
rsPortVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 2)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanStatsOverflowGroup = rsPortVlanStatsOverflowGroup.setStatus('current')
rsPortVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 3)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanHCStatsGroup = rsPortVlanHCStatsGroup.setStatus('current')
rsPortCustomerVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 4)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanStatsGroup = rsPortCustomerVlanStatsGroup.setStatus('current')
rsPortCustomerVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 5)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanStatsOverflowGroup = rsPortCustomerVlanStatsOverflowGroup.setStatus('current')
rsPortCustomerVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 6)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanHCStatsGroup = rsPortCustomerVlanHCStatsGroup.setStatus('current')
rsCustomerVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 7)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanStatsGroup = rsCustomerVlanStatsGroup.setStatus('current')
rsCustomerVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 8)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanStatsOverflowGroup = rsCustomerVlanStatsOverflowGroup.setStatus('current')
rsCustomerVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 9)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanHCStatsGroup = rsCustomerVlanHCStatsGroup.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-VLAN-EXTENSIONS-MIB", rsCustomerVlanInFrames=rsCustomerVlanInFrames, rsCustomerVlanInOctets=rsCustomerVlanInOctets, rsPortCustomerVlanHCStatsGroup=rsPortCustomerVlanHCStatsGroup, rsCustomerVlanHCStatsGroup=rsCustomerVlanHCStatsGroup, rsVlanConformance=rsVlanConformance, rsPortVlanHCStatsEntry=rsPortVlanHCStatsEntry, rsCustomerVlanStatsEntry=rsCustomerVlanStatsEntry, rsPortCustomerVlanStatsEntry=rsPortCustomerVlanStatsEntry, rsCustomerVlanStatsOverflowGroup=rsCustomerVlanStatsOverflowGroup, rsPortCustomerVlanStatsGroup=rsPortCustomerVlanStatsGroup, rsPortVlanOutOctets=rsPortVlanOutOctets, rsCustomerVlanStatsTable=rsCustomerVlanStatsTable, rsPortVlanStatsEntry=rsPortVlanStatsEntry, rsPortVlanInOverflowOctets=rsPortVlanInOverflowOctets, rsCustomerVlanInOverflowFrames=rsCustomerVlanInOverflowFrames, rsPortCustomerVlanHCOutOctets=rsPortCustomerVlanHCOutOctets, rsCustomerVlanHCInDiscards=rsCustomerVlanHCInDiscards, rsPortVlanOutOverflowOctets=rsPortVlanOutOverflowOctets, rsCustomerVlanHCStatsEntry=rsCustomerVlanHCStatsEntry, rsPortCustomerIndex=rsPortCustomerIndex, rsPortCustomerVlanHCOutFrames=rsPortCustomerVlanHCOutFrames, rsVlanExtensionsMIB=rsVlanExtensionsMIB, rsCustomerVlanOutOverflowOctets=rsCustomerVlanOutOverflowOctets, rsVlanStats=rsVlanStats, rsPortVlanStatsOverflowGroup=rsPortVlanStatsOverflowGroup, rsPortCustomerVlanStatsTable=rsPortCustomerVlanStatsTable, rsPortVlanStatsGroup=rsPortVlanStatsGroup, rsPortCustomerVlanOutOctets=rsPortCustomerVlanOutOctets, rsCustomerVlanInDiscards=rsCustomerVlanInDiscards, rsPortVlanHCStatsGroup=rsPortVlanHCStatsGroup, rsPortCustomerVlanInOverflowFrames=rsPortCustomerVlanInOverflowFrames, rsPortCustomerVlanInOverflowDiscards=rsPortCustomerVlanInOverflowDiscards, rsCustomerVlanHCOutOctets=rsCustomerVlanHCOutOctets, rsVlanCompliance=rsVlanCompliance, PYSNMP_MODULE_ID=rsVlanExtensionsMIB, rsPortCustomerVlanOutOverflowFrames=rsPortCustomerVlanOutOverflowFrames, rsPortCustomerVlanInOverflowOctets=rsPortCustomerVlanInOverflowOctets, rsPortCustomerVlanStatsOverflowGroup=rsPortCustomerVlanStatsOverflowGroup, rsPortCustomerVlanInFrames=rsPortCustomerVlanInFrames, rsCustomerVlanOutOctets=rsCustomerVlanOutOctets, rsCustomerVlanHCOutFrames=rsCustomerVlanHCOutFrames, rsVlanObjects=rsVlanObjects, rsPortVlanHCOutOctets=rsPortVlanHCOutOctets, rsCustomerVlanHCInFrames=rsCustomerVlanHCInFrames, rsPortCustomerVlanInOctets=rsPortCustomerVlanInOctets, rsVlanGroups=rsVlanGroups, rsCustomerVlanOutFrames=rsCustomerVlanOutFrames, rsCustomerVlanHCStatsTable=rsCustomerVlanHCStatsTable, rsPortCustomerVlanHCStatsTable=rsPortCustomerVlanHCStatsTable, rsVlanCompliances=rsVlanCompliances, rsCustomerVlanInOverflowDiscards=rsCustomerVlanInOverflowDiscards, rsPortCustomerVlanOutFrames=rsPortCustomerVlanOutFrames, rsCustomerVlanInOverflowOctets=rsCustomerVlanInOverflowOctets, rsCustomerVlanStatsGroup=rsCustomerVlanStatsGroup, rsPortCustomerVlanHCInFrames=rsPortCustomerVlanHCInFrames, rsPortCustomerVlanHCInDiscards=rsPortCustomerVlanHCInDiscards, rsCustomerVlanOutOverflowFrames=rsCustomerVlanOutOverflowFrames, rsPortCustomerVlanHCInOctets=rsPortCustomerVlanHCInOctets, rsPortCustomerVlanOutOverflowOctets=rsPortCustomerVlanOutOverflowOctets, rsPortCustomerVlanHCStatsEntry=rsPortCustomerVlanHCStatsEntry, rsPortVlanHCStatsTable=rsPortVlanHCStatsTable, rsCustomerVlanHCInOctets=rsCustomerVlanHCInOctets, rsPortVlanHCInOctets=rsPortVlanHCInOctets, rsPortVlanStatsTable=rsPortVlanStatsTable, rsPortCustomerVlanInDiscards=rsPortCustomerVlanInDiscards, rsPortVlanInOctets=rsPortVlanInOctets)
