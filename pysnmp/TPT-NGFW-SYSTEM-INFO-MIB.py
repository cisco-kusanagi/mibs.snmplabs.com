#
# PySNMP MIB module TPT-NGFW-SYSTEM-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-NGFW-SYSTEM-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, TimeTicks, Integer32, Bits, Counter64, ModuleIdentity, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Integer32", "Bits", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "ObjectIdentity")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
tpt_ngfw_objs, tptNgfwNotifySeverity, tpt_ngfw_compls, tpt_ngfw_groups, tpt_ngfw_eventsV2 = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tpt-ngfw-objs", "tptNgfwNotifySeverity", "tpt-ngfw-compls", "tpt-ngfw-groups", "tpt-ngfw-eventsV2")
tptNgfwSystemInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1))
tptNgfwSystemInfo.setRevisions(('2016-05-25 18:54', '2013-01-03 17:39',))
if mibBuilder.loadTexts: tptNgfwSystemInfo.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwSystemInfo.setOrganization('Trend Micro, Inc.')
class FipsState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("crypto", 2), ("full", 3))

class BuildType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("production", 1), ("development", 2))

tptNgfwSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSerial.setStatus('current')
tptNgfwSystemSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSoftwareVersion.setStatus('current')
tptNgfwSystemBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildDate.setStatus('current')
tptNgfwSystemBuildType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 4), BuildType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildType.setStatus('current')
tptNgfwSystemBuildRevision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildRevision.setStatus('current')
tptNgfwSystemDigitalVaccineVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemDigitalVaccineVersion.setStatus('current')
tptNgfwSystemModel = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemModel.setStatus('current')
tptNgfwSystemHardwareSerial = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemHardwareSerial.setStatus('current')
tptNgfwSystemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemHardwareRevision.setStatus('current')
tptNgfwSystemFailsafeVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFailsafeVersion.setStatus('current')
tptNgfwSystemBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBootTime.setStatus('current')
tptNgfwSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemUpTime.setStatus('current')
tptNgfwSystemSmsManaged = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsManaged.setStatus('current')
tptNgfwSystemSmsIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 14), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsIpAddressType.setStatus('current')
tptNgfwSystemSmsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 15), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsIpAddress.setStatus('current')
tptNgfwSystemFipsAdminState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 16), FipsState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFipsAdminState.setStatus('current')
tptNgfwSystemFipsOperState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 17), FipsState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFipsOperState.setStatus('current')
tptNgfwSystemMasterKeySet = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemMasterKeySet.setStatus('current')
tptNgfwSystemReadyNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 11)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemReadyNotify.setStatus('current')
tptNgfwSystemShutdownNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 12)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemShutdownNotify.setStatus('current')
tptNgfwSystemSmsNotAuthNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 13)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemSmsNotAuthNotify.setStatus('current')
tptNgfwSystemInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 1)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSoftwareVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildDate"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildRevision"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemDigitalVaccineVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemModel"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareRevision"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFailsafeVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBootTime"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemUpTime"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsManaged"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsAdminState"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsOperState"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemMasterKeySet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemInfoGroup = tptNgfwSystemInfoGroup.setStatus('current')
tptNgfwSystemNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemReadyNotify"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemShutdownNotify"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsNotAuthNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemNotificationGroup = tptNgfwSystemNotificationGroup.setStatus('current')
tptNgfwSystemInfoCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 1)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemInfoGroup"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemInfoCompl = tptNgfwSystemInfoCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-SYSTEM-INFO-MIB", tptNgfwSystemSmsIpAddress=tptNgfwSystemSmsIpAddress, tptNgfwSystemSmsManaged=tptNgfwSystemSmsManaged, tptNgfwSystemFipsOperState=tptNgfwSystemFipsOperState, tptNgfwSystemDigitalVaccineVersion=tptNgfwSystemDigitalVaccineVersion, tptNgfwSystemFipsAdminState=tptNgfwSystemFipsAdminState, tptNgfwSystemBootTime=tptNgfwSystemBootTime, PYSNMP_MODULE_ID=tptNgfwSystemInfo, tptNgfwSystemFailsafeVersion=tptNgfwSystemFailsafeVersion, tptNgfwSystemSerial=tptNgfwSystemSerial, tptNgfwSystemSoftwareVersion=tptNgfwSystemSoftwareVersion, tptNgfwSystemModel=tptNgfwSystemModel, tptNgfwSystemHardwareRevision=tptNgfwSystemHardwareRevision, BuildType=BuildType, FipsState=FipsState, tptNgfwSystemInfo=tptNgfwSystemInfo, tptNgfwSystemBuildRevision=tptNgfwSystemBuildRevision, tptNgfwSystemBuildType=tptNgfwSystemBuildType, tptNgfwSystemHardwareSerial=tptNgfwSystemHardwareSerial, tptNgfwSystemSmsNotAuthNotify=tptNgfwSystemSmsNotAuthNotify, tptNgfwSystemSmsIpAddressType=tptNgfwSystemSmsIpAddressType, tptNgfwSystemMasterKeySet=tptNgfwSystemMasterKeySet, tptNgfwSystemShutdownNotify=tptNgfwSystemShutdownNotify, tptNgfwSystemNotificationGroup=tptNgfwSystemNotificationGroup, tptNgfwSystemBuildDate=tptNgfwSystemBuildDate, tptNgfwSystemInfoGroup=tptNgfwSystemInfoGroup, tptNgfwSystemReadyNotify=tptNgfwSystemReadyNotify, tptNgfwSystemInfoCompl=tptNgfwSystemInfoCompl, tptNgfwSystemUpTime=tptNgfwSystemUpTime)
