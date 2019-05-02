#
# PySNMP MIB module HUAWEI-SYS-CLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SYS-CLOCK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Integer32, ModuleIdentity, iso, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Integer32", "ModuleIdentity", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, RowStatus, DateAndTime, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TimeStamp", "TextualConvention")
hwSysClockMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205))
hwSysClockMIB.setRevisions(('2009-07-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwSysClockMIB.setRevisionsDescriptions(('The initial revision of this MIB module .',))
if mibBuilder.loadTexts: hwSysClockMIB.setLastUpdated('200907250000Z')
if mibBuilder.loadTexts: hwSysClockMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwSysClockMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwSysClockMIB.setDescription('HUAWEI-SYS-CLOCK-MIB is used to configure and query time information, such as the system time, time zone, and daylight saving time. Root object: iso(1).org(3).dod(6).internet(1).private(4).enterprises(1). huawei(2011).huaweiMgmt(5).hwDatacomm(25).hwSysClockMIB(205) ')
huaweiClockObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1))
hwLocalClock = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 1), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalClock.setStatus('current')
if mibBuilder.loadTexts: hwLocalClock.setDescription("This object is used to set and query the local time that is in the format of 'YYYY-MM-DD,HH:MM:SS'. ")
hwUTCClock = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwUTCClock.setStatus('current')
if mibBuilder.loadTexts: hwUTCClock.setDescription("This object is used to configure and query the system UTC time that is in the format of 'YYYY-MM-DD,HH:MM:SS'. ")
huaweiClockNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2))
hwClockChanged = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock"))
if mibBuilder.loadTexts: hwClockChanged.setStatus('current')
if mibBuilder.loadTexts: hwClockChanged.setDescription('This object indicates the alarm reported when the system time changes. In addition, the new system time is recorded.')
huaweiClockMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3))
hwClockMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1))
hwClockMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwClockSetGroup"), ("HUAWEI-SYS-CLOCK-MIB", "hwClockNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockMIBCompliance = hwClockMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwClockMIBCompliance.setDescription(' The compliance statement for entities that support the huawei Clock MIB. ')
huaweiClockMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2))
hwClockSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwLocalClock"), ("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockSetGroup = hwClockSetGroup.setStatus('current')
if mibBuilder.loadTexts: hwClockSetGroup.setDescription('A collection of objects on Clock setting level information. ')
hwClockNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 2)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwClockChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockNotificationGroup = hwClockNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwClockNotificationGroup.setDescription('The collection of notifications in the module')
mibBuilder.exportSymbols("HUAWEI-SYS-CLOCK-MIB", hwSysClockMIB=hwSysClockMIB, hwUTCClock=hwUTCClock, hwClockSetGroup=hwClockSetGroup, huaweiClockObjects=huaweiClockObjects, huaweiClockMIBGroups=huaweiClockMIBGroups, huaweiClockNotifications=huaweiClockNotifications, PYSNMP_MODULE_ID=hwSysClockMIB, hwClockChanged=hwClockChanged, huaweiClockMIBConformance=huaweiClockMIBConformance, hwClockMIBCompliances=hwClockMIBCompliances, hwClockMIBCompliance=hwClockMIBCompliance, hwClockNotificationGroup=hwClockNotificationGroup, hwLocalClock=hwLocalClock)
