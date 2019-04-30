#
# PySNMP MIB module ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Integer32, Counter64, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysMgmtAuthNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60))
etsysMgmtAuthNotificationMIB.setRevisions(('2011-03-08 20:40', '2005-11-14 16:48',))
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setLastUpdated('201103082040Z')
if mibBuilder.loadTexts: etsysMgmtAuthNotificationMIB.setOrganization('Enterasys Networks, Inc')
class EtsysMgmtAuthNotificationTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cliConsole", 0), ("cliSsh", 1), ("cliTelnet", 2), ("webview", 3), ("inactiveUser", 4), ("maxUserAttempt", 5), ("maxUserFail", 6))

etsysMgmtAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1))
etsysMgmtAuthNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0))
etsysMgmtAuthConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1))
etsysMgmtAuthAuthenticationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2))
etsysMgmtAuthNotificationsSupported = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationsSupported.setStatus('current')
etsysMgmtAuthNotificationEnabledStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 1, 2), EtsysMgmtAuthNotificationTypes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMgmtAuthNotificationEnabledStatus.setStatus('current')
etsysMgmtAuthType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 1), EtsysMgmtAuthNotificationTypes()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthType.setStatus('current')
etsysMgmtAuthUserName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthUserName.setStatus('current')
etsysMgmtAuthInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddressType.setStatus('current')
etsysMgmtAuthInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInetAddress.setStatus('current')
etsysMgmtAuthInIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 2, 5), InterfaceIndexOrZero()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysMgmtAuthInIfIndex.setStatus('current')
etsysMgmtAuthSuccessNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthSuccessNotificiation.setStatus('current')
etsysMgmtAuthFailNotificiation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthFailNotificiation.setStatus('current')
etsysMgmtAuthInactiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthInactiveNotification.setStatus('current')
etsysMgmtAuthMaxAuthAttemptNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxAuthAttemptNotification.setStatus('current')
etsysMgmtAuthMaxFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 1, 0, 5)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if mibBuilder.loadTexts: etsysMgmtAuthMaxFailNotification.setStatus('current')
etsysMgmtAuthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2))
etsysMgmtAuthGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1))
etsysMgmtAuthCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2))
etsysMgmtAuthConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationsSupported"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationEnabledStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthConfigGroup = etsysMgmtAuthConfigGroup.setStatus('current')
etsysMgmtAuthHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthUserName"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddressType"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInetAddress"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthHistoryGroup = etsysMgmtAuthHistoryGroup.setStatus('current')
etsysMgmtAuthNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 3)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthSuccessNotificiation"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthFailNotificiation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationGroup = etsysMgmtAuthNotificationGroup.setStatus('current')
etsysMgmtAuthNotificationUserGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 1, 4)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthInactiveNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxAuthAttemptNotification"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthMaxFailNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthNotificationUserGroup = etsysMgmtAuthNotificationUserGroup.setStatus('current')
etsysMgmtAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 1)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthConfigGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthHistoryGroup"), ("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthCompliance = etsysMgmtAuthCompliance.setStatus('current')
etsysMgmtAuthUserCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 60, 2, 2, 2)).setObjects(("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", "etsysMgmtAuthNotificationUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMgmtAuthUserCompliance = etsysMgmtAuthUserCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-MGMT-AUTH-NOTIFICATION-MIB", etsysMgmtAuthNotificationUserGroup=etsysMgmtAuthNotificationUserGroup, etsysMgmtAuthNotificationGroup=etsysMgmtAuthNotificationGroup, etsysMgmtAuthNotificationBranch=etsysMgmtAuthNotificationBranch, etsysMgmtAuthFailNotificiation=etsysMgmtAuthFailNotificiation, etsysMgmtAuthConfigGroup=etsysMgmtAuthConfigGroup, etsysMgmtAuthMaxFailNotification=etsysMgmtAuthMaxFailNotification, etsysMgmtAuthNotificationEnabledStatus=etsysMgmtAuthNotificationEnabledStatus, etsysMgmtAuthCompliance=etsysMgmtAuthCompliance, etsysMgmtAuthGroups=etsysMgmtAuthGroups, etsysMgmtAuthConformance=etsysMgmtAuthConformance, etsysMgmtAuthNotificationMIB=etsysMgmtAuthNotificationMIB, etsysMgmtAuthInetAddress=etsysMgmtAuthInetAddress, PYSNMP_MODULE_ID=etsysMgmtAuthNotificationMIB, etsysMgmtAuthNotificationsSupported=etsysMgmtAuthNotificationsSupported, etsysMgmtAuthConfigBranch=etsysMgmtAuthConfigBranch, etsysMgmtAuthInIfIndex=etsysMgmtAuthInIfIndex, etsysMgmtAuthSuccessNotificiation=etsysMgmtAuthSuccessNotificiation, etsysMgmtAuthType=etsysMgmtAuthType, etsysMgmtAuthUserCompliance=etsysMgmtAuthUserCompliance, etsysMgmtAuthUserName=etsysMgmtAuthUserName, etsysMgmtAuthAuthenticationBranch=etsysMgmtAuthAuthenticationBranch, etsysMgmtAuthObjects=etsysMgmtAuthObjects, etsysMgmtAuthInactiveNotification=etsysMgmtAuthInactiveNotification, etsysMgmtAuthMaxAuthAttemptNotification=etsysMgmtAuthMaxAuthAttemptNotification, etsysMgmtAuthInetAddressType=etsysMgmtAuthInetAddressType, EtsysMgmtAuthNotificationTypes=EtsysMgmtAuthNotificationTypes, etsysMgmtAuthCompliances=etsysMgmtAuthCompliances, etsysMgmtAuthHistoryGroup=etsysMgmtAuthHistoryGroup)
