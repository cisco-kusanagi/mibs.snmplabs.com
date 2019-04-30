#
# PySNMP MIB module INNOMINATE-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INNOMINATE-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, iso, Counter64, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, enterprises, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "iso", "Counter64", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "enterprises", "IpAddress", "Integer32")
TruthValue, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention")
innominateLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 15450, 3, 7))
innominateLldpMIB.setRevisions(('2005-08-24 00:00',))
if mibBuilder.loadTexts: innominateLldpMIB.setLastUpdated('200508240000Z')
if mibBuilder.loadTexts: innominateLldpMIB.setOrganization('Innominate Security Technologies AG')
class TimeFilter(TextualConvention, TimeTicks):
    status = 'current'

innominateLLDPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1))
innominateLLDPStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2))
innominateLLDPAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: innominateLLDPAdminStatus.setStatus('current')
innominateLLDPInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2), )
if mibBuilder.loadTexts: innominateLLDPInterfaceTable.setStatus('current')
innominateLLDPIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1), ).setIndexNames((0, "INNOMINATE-LLDP-MIB", "innominateLLDPIfaceGroupID"), (0, "INNOMINATE-LLDP-MIB", "innominateLLDPIfaceID"))
if mibBuilder.loadTexts: innominateLLDPIfEntry.setStatus('current')
innominateLLDPIfaceGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPIfaceGroupID.setStatus('current')
innominateLLDPIfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPIfaceID.setStatus('current')
innominateLLDPIfaceHirmaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4))).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: innominateLLDPIfaceHirmaMode.setStatus('current')
innominateLLDPIfaceFDBMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lldpOnly", 1), ("macOnly", 2), ("both", 3), ("autoDetect", 4))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: innominateLLDPIfaceFDBMode.setStatus('current')
innominateLLDPIfaceMaxNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: innominateLLDPIfaceMaxNeighbors.setStatus('current')
innominateLLDPStatsIfTable = MibTable((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1), )
if mibBuilder.loadTexts: innominateLLDPStatsIfTable.setStatus('current')
innominateLLDPStatsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1), ).setIndexNames((0, "INNOMINATE-LLDP-MIB", "innominateLLDPStatsIfaceGroupID"), (0, "INNOMINATE-LLDP-MIB", "innominateLLDPStatsIfaceID"))
if mibBuilder.loadTexts: innominateLLDPStatsIfEntry.setStatus('current')
innominateLLDPStatsIfaceGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceGroupID.setStatus('current')
innominateLLDPStatsIfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceID.setStatus('current')
innominateLLDPStatsIfaceTotalFDBEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceTotalFDBEntryCount.setStatus('current')
innominateLLDPStatsIfaceTotalEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceTotalEntryCount.setStatus('current')
innominateLLDPStatsIfaceIEEEEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceIEEEEntryCount.setStatus('current')
innominateLLDPStatsIfaceHirmaEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceHirmaEntryCount.setStatus('current')
innominateLLDPStatsIfaceFDBEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innominateLLDPStatsIfaceFDBEntryCount.setStatus('current')
mibBuilder.exportSymbols("INNOMINATE-LLDP-MIB", innominateLLDPStatsIfEntry=innominateLLDPStatsIfEntry, innominateLLDPAdminStatus=innominateLLDPAdminStatus, TimeFilter=TimeFilter, innominateLLDPIfaceHirmaMode=innominateLLDPIfaceHirmaMode, innominateLLDPIfaceFDBMode=innominateLLDPIfaceFDBMode, innominateLLDPStatsIfaceIEEEEntryCount=innominateLLDPStatsIfaceIEEEEntryCount, innominateLLDPStatsIfTable=innominateLLDPStatsIfTable, innominateLLDPStatsIfaceGroupID=innominateLLDPStatsIfaceGroupID, innominateLLDPStatsIfaceFDBEntryCount=innominateLLDPStatsIfaceFDBEntryCount, innominateLLDPIfaceMaxNeighbors=innominateLLDPIfaceMaxNeighbors, PYSNMP_MODULE_ID=innominateLldpMIB, innominateLLDPStatsIfaceID=innominateLLDPStatsIfaceID, innominateLldpMIB=innominateLldpMIB, innominateLLDPIfEntry=innominateLLDPIfEntry, innominateLLDPIfaceID=innominateLLDPIfaceID, innominateLLDPIfaceGroupID=innominateLLDPIfaceGroupID, innominateLLDPStatistics=innominateLLDPStatistics, innominateLLDPStatsIfaceTotalFDBEntryCount=innominateLLDPStatsIfaceTotalFDBEntryCount, innominateLLDPStatsIfaceTotalEntryCount=innominateLLDPStatsIfaceTotalEntryCount, innominateLLDPConfig=innominateLLDPConfig, innominateLLDPStatsIfaceHirmaEntryCount=innominateLLDPStatsIfaceHirmaEntryCount, innominateLLDPInterfaceTable=innominateLLDPInterfaceTable)