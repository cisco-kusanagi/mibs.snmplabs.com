#
# PySNMP MIB module USAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/USAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, iso, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Gauge32, ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32")
TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
deviceUsageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 4))
if mibBuilder.loadTexts: deviceUsageMIB.setLastUpdated('0211060300Z')
if mibBuilder.loadTexts: deviceUsageMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceUsageMIB.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: deviceUsageMIB.setDescription('The USAGE-MIB is used to monitor resource usage of the device.')
deviceUsageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1))
deviceUsageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2))
deviceUsageMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0))
class Percent(TextualConvention, Integer32):
    description = 'Percent value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class UsageStatus(TextualConvention, Integer32):
    description = 'Current status of the deviceUsagePercent. ok : value within limit. high : value surpassed high limit. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("high", 2))

deviceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1), )
if mibBuilder.loadTexts: deviceUsageTable.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTable.setDescription('This table lists the various attacks that are detected.')
deviceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1), ).setIndexNames((0, "USAGE-MIB", "deviceUsageIndex"))
if mibBuilder.loadTexts: deviceUsageEntry.setStatus('current')
if mibBuilder.loadTexts: deviceUsageEntry.setDescription('A deviceUsage entry describes the present usage of a resource.')
deviceUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceUsageIndex.setStatus('current')
if mibBuilder.loadTexts: deviceUsageIndex.setDescription('An arbitrary value which uniquely identifies a resource.')
deviceUsageTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceUsageTrapEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTrapEnabled.setDescription('This variable controls generation of deviceUsageTrap for this resource. When this variable is true(1), generation of deviceUsageTrap is enabled. When this variable is false(2), generation of deviceUsageTrap is disabled. The default start-up value is true(1).')
deviceUsageName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageName.setStatus('current')
if mibBuilder.loadTexts: deviceUsageName.setDescription('The textual name of the resource i.e. Disk.')
deviceUsagePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsagePercent.setStatus('current')
if mibBuilder.loadTexts: deviceUsagePercent.setDescription('Percent of resource in use. When the resource is Disk, it is the amount of disk used by the cache subsytem')
deviceUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 5), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceUsageHigh.setStatus('current')
if mibBuilder.loadTexts: deviceUsageHigh.setDescription('Percent usage which a notification will be sent when the value is reached. For example if deviceUsageHigh is set to 79 then notification will be send when the value changes from less than 79 to 79. The default is defined by the device for a particular resource. When the resource is Disk, it is the amount of disk used by the cache subsytem')
deviceUsageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 6), UsageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageStatus.setStatus('current')
if mibBuilder.loadTexts: deviceUsageStatus.setDescription('Comparison of deviceUsagePercent with deviceUsageHigh.')
deviceUsageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageTime.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTime.setDescription("value of 'sysUpTime.0' at last resource reading.")
deviceUsageTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0, 1)).setObjects(("USAGE-MIB", "deviceUsageName"), ("USAGE-MIB", "deviceUsagePercent"), ("USAGE-MIB", "deviceUsageStatus"))
if mibBuilder.loadTexts: deviceUsageTrap.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTrap.setDescription('At notification is sent when the deviceUsagePercent exceeds a threshold.')
mibBuilder.exportSymbols("USAGE-MIB", deviceUsageEntry=deviceUsageEntry, deviceUsageHigh=deviceUsageHigh, deviceUsageMIBNotificationsPrefix=deviceUsageMIBNotificationsPrefix, deviceUsageTrapEnabled=deviceUsageTrapEnabled, Percent=Percent, deviceUsageMIBObjects=deviceUsageMIBObjects, deviceUsageStatus=deviceUsageStatus, deviceUsageIndex=deviceUsageIndex, deviceUsageTime=deviceUsageTime, deviceUsageTrap=deviceUsageTrap, deviceUsageName=deviceUsageName, PYSNMP_MODULE_ID=deviceUsageMIB, deviceUsageMIBNotifications=deviceUsageMIBNotifications, deviceUsageTable=deviceUsageTable, deviceUsageMIB=deviceUsageMIB, deviceUsagePercent=deviceUsagePercent, UsageStatus=UsageStatus)
