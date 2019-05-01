#
# PySNMP MIB module ARISTA-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dot1qTpFdbAddress, dot1qFdbId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qTpFdbAddress", "dot1qFdbId")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, Gauge32, Counter64, ModuleIdentity, NotificationType, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "Gauge32", "Counter64", "ModuleIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 2))
aristaBridgeExtMIB.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2010-05-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaBridgeExtMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses', 'Updated postal address and telephone', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: aristaBridgeExtMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBridgeExtMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaBridgeExtMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaBridgeExtMIB.setDescription('This MIB contains extensions to the BRIDGE-MIB.')
aristaDot1qTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1), )
if mibBuilder.loadTexts: aristaDot1qTpFdbTable.setStatus('current')
if mibBuilder.loadTexts: aristaDot1qTpFdbTable.setDescription('A table that contains host move information about unicast entries for which the device has forwarding information.')
aristaDot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1), ).setIndexNames((0, "ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbTimeMark"), (0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: aristaDot1qTpFdbEntry.setStatus('current')
if mibBuilder.loadTexts: aristaDot1qTpFdbEntry.setDescription('Information about a specific unicast MAC address for which the device has some forwarding information.')
aristaDot1qTpFdbTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: aristaDot1qTpFdbTimeMark.setStatus('current')
if mibBuilder.loadTexts: aristaDot1qTpFdbTimeMark.setDescription("A TimeFilter that can be used to filter out entries that have not moved recently. If you don't want to filter, make sure to pass '0' for the value of this index component, otherwise pass the sysUpTime value representing the last time you queried the table.")
aristaDot1qTpFdbNumMoves = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbNumMoves.setStatus('current')
if mibBuilder.loadTexts: aristaDot1qTpFdbNumMoves.setDescription('The number of times a given MAC address has changed ports without having been aged out, or the value 1 for a MAC address that was not previously in the table before being learned.')
aristaDot1qTpFdbLastMove = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbLastMove.setStatus('current')
if mibBuilder.loadTexts: aristaDot1qTpFdbLastMove.setDescription('The value of sysUpTime the last time the value of aristaDot1qTpFdbNumMoves was incremented.')
aristaBridgeExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2))
aristaBridgeExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1))
aristaBridgeExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2))
aristaBridgeExtBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"), ("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbLastMove"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtBaseGroup = aristaBridgeExtBaseGroup.setStatus('current')
if mibBuilder.loadTexts: aristaBridgeExtBaseGroup.setDescription('A collection of objects providing MAC move count and times.')
aristaBridgeExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtCompliance = aristaBridgeExtCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaBridgeExtCompliance.setDescription('The compliance statement for device support of MAC move count and times.')
mibBuilder.exportSymbols("ARISTA-BRIDGE-EXT-MIB", aristaDot1qTpFdbNumMoves=aristaDot1qTpFdbNumMoves, aristaBridgeExtMIB=aristaBridgeExtMIB, aristaDot1qTpFdbTimeMark=aristaDot1qTpFdbTimeMark, aristaBridgeExtBaseGroup=aristaBridgeExtBaseGroup, aristaDot1qTpFdbLastMove=aristaDot1qTpFdbLastMove, aristaBridgeExtCompliance=aristaBridgeExtCompliance, aristaBridgeExtCompliances=aristaBridgeExtCompliances, aristaDot1qTpFdbEntry=aristaDot1qTpFdbEntry, PYSNMP_MODULE_ID=aristaBridgeExtMIB, aristaBridgeExtGroups=aristaBridgeExtGroups, aristaBridgeExtConformance=aristaBridgeExtConformance, aristaDot1qTpFdbTable=aristaDot1qTpFdbTable)
