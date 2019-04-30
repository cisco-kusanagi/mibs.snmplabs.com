#
# PySNMP MIB module TPT-NGFW-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-NGFW-LOGGING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, TimeTicks, Integer32, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, iso, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "iso", "MibIdentifier", "NotificationType", "Counter32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
tpt_ngfw_compls, tpt_ngfw_objs, tpt_ngfw_params, tpt_ngfw_groups, Severity, tpt_ngfw_eventsV2 = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tpt-ngfw-compls", "tpt-ngfw-objs", "tpt-ngfw-params", "tpt-ngfw-groups", "Severity", "tpt-ngfw-eventsV2")
tptNgfwSystemSerial, = mibBuilder.importSymbols("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial")
tptNgfwLogging = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 5))
tptNgfwLogging.setRevisions(('2016-05-25 18:54', '2013-03-13 12:00',))
if mibBuilder.loadTexts: tptNgfwLogging.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwLogging.setOrganization('Trend Micro, Inc.')
class AuditLogResult(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("failed", 2))

class AuditLogCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("undefined", 1), ("general", 2), ("login", 3), ("logout", 4), ("user", 5), ("time", 6), ("policy", 7), ("update", 8), ("boot", 9), ("report", 10), ("host", 11), ("cfg", 12), ("device", 13), ("sms", 14), ("server", 15), ("segment", 16), ("license", 17), ("ha", 18), ("monitor", 19), ("ipFilter", 20), ("connTable", 21), ("hostComm", 22), ("tse", 23), ("cf", 24))

tptNgfwSysLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 15)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
if mibBuilder.loadTexts: tptNgfwSysLogNotify.setStatus('current')
tptNgfwLogNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 60), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyTime.setStatus('current')
tptNgfwLogNotifyHost = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 61), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyHost.setStatus('current')
tptNgfwLogNotifySource = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 62), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifySource.setStatus('current')
tptNgfwLogNotifySeverity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 63), Severity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifySeverity.setStatus('current')
tptNgfwLogNotifyText = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 64), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyText.setStatus('current')
tptNgfwAuditLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 16)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
if mibBuilder.loadTexts: tptNgfwAuditLogNotify.setStatus('current')
tptNgfwAuditLogNotifyAccess = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 65), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyAccess.setStatus('current')
tptNgfwAuditLogNotifyType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 66), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyType.setStatus('current')
tptNgfwAuditLogNotifyIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 67), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyIpAddrType.setStatus('current')
tptNgfwAuditLogNotifyIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 68), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyIpAddr.setStatus('current')
tptNgfwAuditLogNotifyCategory = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 69), AuditLogCategory()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyCategory.setStatus('current')
tptNgfwAuditLogNotifyResult = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 70), AuditLogResult()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyResult.setStatus('current')
tptNgfwAuditLogNotifyUser = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 71), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyUser.setStatus('current')
tptNgfwAuditLogNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 72), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyMessage.setStatus('current')
tptNgfwVpnLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 17)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
if mibBuilder.loadTexts: tptNgfwVpnLogNotify.setStatus('current')
tptNgfwLoggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingGroup = tptNgfwLoggingGroup.setStatus('current')
tptNgfwLoggingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 10)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwSysLogNotify"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotify"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwVpnLogNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingNotificationGroup = tptNgfwLoggingNotificationGroup.setStatus('current')
tptNgfwLoggingCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 3)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingGroup"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingCompl = tptNgfwLoggingCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-LOGGING-MIB", tptNgfwLogNotifyText=tptNgfwLogNotifyText, tptNgfwLogging=tptNgfwLogging, tptNgfwAuditLogNotifyAccess=tptNgfwAuditLogNotifyAccess, tptNgfwLoggingCompl=tptNgfwLoggingCompl, AuditLogCategory=AuditLogCategory, AuditLogResult=AuditLogResult, tptNgfwSysLogNotify=tptNgfwSysLogNotify, tptNgfwVpnLogNotify=tptNgfwVpnLogNotify, tptNgfwAuditLogNotifyUser=tptNgfwAuditLogNotifyUser, tptNgfwAuditLogNotifyIpAddr=tptNgfwAuditLogNotifyIpAddr, PYSNMP_MODULE_ID=tptNgfwLogging, tptNgfwLoggingNotificationGroup=tptNgfwLoggingNotificationGroup, tptNgfwLogNotifyTime=tptNgfwLogNotifyTime, tptNgfwLoggingGroup=tptNgfwLoggingGroup, tptNgfwAuditLogNotifyIpAddrType=tptNgfwAuditLogNotifyIpAddrType, tptNgfwLogNotifySeverity=tptNgfwLogNotifySeverity, tptNgfwLogNotifyHost=tptNgfwLogNotifyHost, tptNgfwAuditLogNotifyType=tptNgfwAuditLogNotifyType, tptNgfwAuditLogNotifyCategory=tptNgfwAuditLogNotifyCategory, tptNgfwLogNotifySource=tptNgfwLogNotifySource, tptNgfwAuditLogNotifyMessage=tptNgfwAuditLogNotifyMessage, tptNgfwAuditLogNotifyResult=tptNgfwAuditLogNotifyResult, tptNgfwAuditLogNotify=tptNgfwAuditLogNotify)
