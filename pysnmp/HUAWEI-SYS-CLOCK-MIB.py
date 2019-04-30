#
# PySNMP MIB module HUAWEI-SYS-CLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SYS-CLOCK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Bits, MibIdentifier, iso, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, IpAddress, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "iso", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "IpAddress", "Gauge32", "ModuleIdentity")
TimeStamp, DisplayString, RowStatus, DateAndTime, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue")
hwSysClockMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205))
hwSysClockMIB.setRevisions(('2009-07-25 00:00',))
if mibBuilder.loadTexts: hwSysClockMIB.setLastUpdated('200907250000Z')
if mibBuilder.loadTexts: hwSysClockMIB.setOrganization('Huawei Technologies Co.,Ltd.')
huaweiClockObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1))
hwLocalClock = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 1), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwLocalClock.setStatus('current')
hwUTCClock = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwUTCClock.setStatus('current')
huaweiClockNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2))
hwClockChanged = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock"))
if mibBuilder.loadTexts: hwClockChanged.setStatus('current')
huaweiClockMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3))
hwClockMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1))
hwClockMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwClockSetGroup"), ("HUAWEI-SYS-CLOCK-MIB", "hwClockNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockMIBCompliance = hwClockMIBCompliance.setStatus('current')
huaweiClockMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2))
hwClockSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 1)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwLocalClock"), ("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockSetGroup = hwClockSetGroup.setStatus('current')
hwClockNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 2)).setObjects(("HUAWEI-SYS-CLOCK-MIB", "hwClockChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwClockNotificationGroup = hwClockNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SYS-CLOCK-MIB", huaweiClockMIBGroups=huaweiClockMIBGroups, huaweiClockMIBConformance=huaweiClockMIBConformance, hwClockNotificationGroup=hwClockNotificationGroup, PYSNMP_MODULE_ID=hwSysClockMIB, hwUTCClock=hwUTCClock, huaweiClockNotifications=huaweiClockNotifications, hwClockSetGroup=hwClockSetGroup, hwClockChanged=hwClockChanged, hwClockMIBCompliances=hwClockMIBCompliances, hwLocalClock=hwLocalClock, hwSysClockMIB=hwSysClockMIB, hwClockMIBCompliance=hwClockMIBCompliance, huaweiClockObjects=huaweiClockObjects)
