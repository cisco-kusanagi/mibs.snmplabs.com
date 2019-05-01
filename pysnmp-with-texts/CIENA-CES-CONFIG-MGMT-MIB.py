#
# PySNMP MIB module CIENA-CES-CONFIG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-CES-CONFIG-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
cienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter32, ObjectIdentity, Unsigned32, IpAddress, Integer32, Counter64, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
cienaCesConfigMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36))
cienaCesConfigMgmtMIB.setRevisions(('2015-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setLastUpdated('201502110000Z')
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setDescription('This module defines device configuration information and associated notifications.')
class CienaCesConfigMgmtContext(TextualConvention, Integer32):
    description = 'The context in which the configuration change was done. unknown(1) An unknown context. This value is used when the system cannot find what mechanism was used to modify the configuration state cli(2) The configuration state was modified using the command line interface snmp(3) The configuration state was modified using SNMP netconf(4) The configuration state was modified using NETCONF'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("cli", 2), ("snmp", 3), ("netconf", 4))

cienaCesConfigMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1))
cienaCesConfigMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1))
cienaCesConfigMgmtMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36))
cienaCesConfigMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0))
cienaCesConfigMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2))
cienaCesConfigMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 1))
cienaCesConfigMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 2))
cienaCesConfigMgmtConfigLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastSaved.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastSaved.setDescription('The date and time of the most recent running configuration save.')
cienaCesConfigMgmtConfigLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastChanged.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastChanged.setDescription('The date and time of the most recent running configuration change.')
cienaCesConfigMgmtConfigLastContext = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 3), CienaCesConfigMgmtContext()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastContext.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastContext.setDescription('The last context that modified the configuration state.')
cienaCesConfigMgmtConfigLastUser = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastUser.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastUser.setDescription('The last user that modified the configuration state.')
cienaCesConfigMgmtConfigLastOrigin = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastOrigin.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastOrigin.setDescription('The last origin that modified the configuration state such as an IP address or terminal.')
cienaCesConfigMgmtConfigSavedNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastSaved"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigSavedNotification.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigSavedNotification.setDescription('This notification is sent when the configuration is saved.')
cienaCesConfigMgmtConfigChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 2)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastContext"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastUser"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastOrigin"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigChangeNotification.setStatus('current')
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigChangeNotification.setDescription('This notification is sent when the configuration on the device changes. A hysteresis mechanism is evaluated before sending in an effort to limit the number of events generated. This mechanism will send out one notification when an accumulation rate threshold is crossed. If the context/user/origin of a configuration change does not match the currently tracked context/user/origin, then this notification will automatically be sent. The hysteresis algorithm will then be evaluated based on the new context/user/origin.')
mibBuilder.exportSymbols("CIENA-CES-CONFIG-MGMT-MIB", PYSNMP_MODULE_ID=cienaCesConfigMgmtMIB, cienaCesConfigMgmtConfigLastContext=cienaCesConfigMgmtConfigLastContext, cienaCesConfigMgmt=cienaCesConfigMgmt, cienaCesConfigMgmtMIB=cienaCesConfigMgmtMIB, cienaCesConfigMgmtConfigLastChanged=cienaCesConfigMgmtConfigLastChanged, cienaCesConfigMgmtMIBConformance=cienaCesConfigMgmtMIBConformance, cienaCesConfigMgmtConfigLastSaved=cienaCesConfigMgmtConfigLastSaved, cienaCesConfigMgmtConfigSavedNotification=cienaCesConfigMgmtConfigSavedNotification, cienaCesConfigMgmtMIBNotificationsPrefix=cienaCesConfigMgmtMIBNotificationsPrefix, cienaCesConfigMgmtMIBNotifications=cienaCesConfigMgmtMIBNotifications, cienaCesConfigMgmtMIBCompliances=cienaCesConfigMgmtMIBCompliances, cienaCesConfigMgmtConfigLastUser=cienaCesConfigMgmtConfigLastUser, CienaCesConfigMgmtContext=CienaCesConfigMgmtContext, cienaCesConfigMgmtMIBGroups=cienaCesConfigMgmtMIBGroups, cienaCesConfigMgmtConfigLastOrigin=cienaCesConfigMgmtConfigLastOrigin, cienaCesConfigMgmtConfigChangeNotification=cienaCesConfigMgmtConfigChangeNotification, cienaCesConfigMgmtMIBObjects=cienaCesConfigMgmtMIBObjects)
