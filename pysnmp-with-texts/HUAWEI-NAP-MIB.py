#
# PySNMP MIB module HUAWEI-NAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, TextualConvention, Gauge32, ModuleIdentity, ObjectIdentity, Counter32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "TextualConvention", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Counter32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Integer32", "Unsigned32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwNap = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206))
hwNap.setRevisions(('2009-03-17 10:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwNap.setRevisionsDescriptions(('The initial revision of this MIB module .',))
if mibBuilder.loadTexts: hwNap.setLastUpdated('200903171027Z')
if mibBuilder.loadTexts: hwNap.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwNap.setContactInfo('VRP Team Huawei Technologies Co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwNap.setDescription('The MIB module for nap between host and netmanager.')
class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
hwNapScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1))
hwNapTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2))
hwNapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3))
hwNapNeighborNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborNum.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborNum.setDescription('current configed nap neighbor num.')
hwNapNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1), )
if mibBuilder.loadTexts: hwNapNeighborTable.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborTable.setDescription('This table contains the records of configed nap neighbor.')
hwNapNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1), ).setIndexNames((0, "HUAWEI-NAP-MIB", "hwNapNeighborIndex"))
if mibBuilder.loadTexts: hwNapNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborEntry.setDescription('Entry of hwNapNeighborTable.')
hwNapNeighborIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborIndex.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborIndex.setDescription('Index of nap neighbor table.')
hwNapLocalPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapLocalPortName.setStatus('current')
if mibBuilder.loadTexts: hwNapLocalPortName.setDescription('The local port name of nap neighbor.')
hwNapNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("detecting", 1), ("established", 2), ("ipAssigned", 3), ("abnormal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborStatus.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborStatus.setDescription('The status of nap neighbor.')
hwNapNeighborAbnormalReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 0), ("portNotSupport", 1), ("slaveDisable", 2), ("masterIpAssignError", 3), ("slaveIpAssignError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNapNeighborAbnormalReason.setStatus('current')
if mibBuilder.loadTexts: hwNapNeighborAbnormalReason.setDescription('The abnormal reason for nap neighbor.')
hwNapStatusNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 206, 3, 1)).setObjects(("HUAWEI-NAP-MIB", "hwNapLocalPortName"), ("HUAWEI-NAP-MIB", "hwNapNeighborStatus"), ("HUAWEI-NAP-MIB", "hwNapNeighborAbnormalReason"))
if mibBuilder.loadTexts: hwNapStatusNotify.setStatus('current')
if mibBuilder.loadTexts: hwNapStatusNotify.setDescription('If the system configuration is changed in given time, a notification will be generated.')
mibBuilder.exportSymbols("HUAWEI-NAP-MIB", hwNapNeighborNum=hwNapNeighborNum, hwNapNeighborAbnormalReason=hwNapNeighborAbnormalReason, hwNapTableObjects=hwNapTableObjects, hwNap=hwNap, hwNapLocalPortName=hwNapLocalPortName, hwNapNeighborStatus=hwNapNeighborStatus, hwNapNotifications=hwNapNotifications, hwNapStatusNotify=hwNapStatusNotify, hwNapNeighborTable=hwNapNeighborTable, DateAndTime=DateAndTime, hwNapNeighborEntry=hwNapNeighborEntry, PYSNMP_MODULE_ID=hwNap, hwNapScalarObjects=hwNapScalarObjects, hwNapNeighborIndex=hwNapNeighborIndex)
