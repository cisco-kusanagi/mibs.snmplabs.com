#
# PySNMP MIB module TPLINK-LLDPCOUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-LLDPCOUNT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Unsigned32, Bits, iso, TimeTicks, Counter64, ObjectIdentity, IpAddress, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Unsigned32", "Bits", "iso", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkLldpMIBNotifications, tplinkLldpMIBObjects = mibBuilder.importSymbols("TPLINK-LLDP-MIB", "tplinkLldpMIBNotifications", "tplinkLldpMIBObjects")
lldpCount = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

lldpGlobalCount = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1))
lldpGlobalCountUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpGlobalCountUpdateTime.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalCountUpdateTime.setDescription('The time how long the information has updated.')
lldpGlobalCountNeighborInserted = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpGlobalCountNeighborInserted.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalCountNeighborInserted.setDescription('Display the newest number of the neighbor.')
lldpGlobalCountNeighborDeleted = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpGlobalCountNeighborDeleted.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalCountNeighborDeleted.setDescription('Display how many neighbors the local device has deleted.')
lldpGlobalCountNeighborDroped = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpGlobalCountNeighborDroped.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalCountNeighborDroped.setDescription('Display how many neighbors the local device has discarded.')
lldpGlobalCountNeighborAged = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpGlobalCountNeighborAged.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalCountNeighborAged.setDescription('Display how many neighbors was time out in the local device.')
lldpCountNeighborInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2), )
if mibBuilder.loadTexts: lldpCountNeighborInfoTable.setStatus('current')
if mibBuilder.loadTexts: lldpCountNeighborInfoTable.setDescription('The statistic information entries of the neighbor device.')
lldpCountNeighborInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lldpCountNeighborInfoEntry.setStatus('current')
if mibBuilder.loadTexts: lldpCountNeighborInfoEntry.setDescription('An entry contains of the information of the neighboe device.')
lldpCountNeighborPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpCountNeighborPortId.setStatus('current')
if mibBuilder.loadTexts: lldpCountNeighborPortId.setDescription('Displays the port ID of the switch.')
lldpNeighborFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborFramesOut.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborFramesOut.setDescription('Displays the number of the frames sent by this port.')
lldpNeighborFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborFramesIn.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborFramesIn.setDescription('Displays the number of the frames received by this port.')
lldpNeighborFramesDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborFramesDiscarded.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborFramesDiscarded.setDescription('Displays the number of the frams discarded by this port.')
lldpNeighborFramesInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborFramesInErrors.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborFramesInErrors.setDescription('Displays the number of the error frames recived by this port.')
lldpNeighborAgeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborAgeOuts.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborAgeOuts.setDescription('Displays the number of the time out neighbor which connected to this port.')
lldpNeighborTlvDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborTlvDiscarded.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborTlvDiscarded.setDescription('Displays the number of discarded TLV when this port received LLDPDU.')
lldpNeighborTlvUnrecognized = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpNeighborTlvUnrecognized.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborTlvUnrecognized.setDescription('Displays the number of the unrecognized TLV when this port received LLDPDU.')
lldpNeighborChange = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 35, 2, 1)).setObjects(("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborInserted"), ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborDeleted"), ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborDroped"), ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborAged"))
if mibBuilder.loadTexts: lldpNeighborChange.setStatus('current')
if mibBuilder.loadTexts: lldpNeighborChange.setDescription('')
mibBuilder.exportSymbols("TPLINK-LLDPCOUNT-MIB", lldpCountNeighborPortId=lldpCountNeighborPortId, lldpNeighborFramesOut=lldpNeighborFramesOut, lldpNeighborFramesDiscarded=lldpNeighborFramesDiscarded, lldpNeighborFramesInErrors=lldpNeighborFramesInErrors, lldpCountNeighborInfoEntry=lldpCountNeighborInfoEntry, lldpGlobalCountUpdateTime=lldpGlobalCountUpdateTime, lldpNeighborTlvUnrecognized=lldpNeighborTlvUnrecognized, MacAddress=MacAddress, lldpNeighborTlvDiscarded=lldpNeighborTlvDiscarded, lldpNeighborChange=lldpNeighborChange, lldpGlobalCountNeighborDroped=lldpGlobalCountNeighborDroped, lldpCount=lldpCount, lldpGlobalCountNeighborAged=lldpGlobalCountNeighborAged, lldpNeighborAgeOuts=lldpNeighborAgeOuts, lldpCountNeighborInfoTable=lldpCountNeighborInfoTable, lldpNeighborFramesIn=lldpNeighborFramesIn, lldpGlobalCountNeighborInserted=lldpGlobalCountNeighborInserted, lldpGlobalCountNeighborDeleted=lldpGlobalCountNeighborDeleted, lldpGlobalCount=lldpGlobalCount)
