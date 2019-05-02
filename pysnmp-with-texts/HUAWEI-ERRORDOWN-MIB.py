#
# PySNMP MIB module HUAWEI-ERRORDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ERRORDOWN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, ModuleIdentity, NotificationType, ObjectIdentity, Counter32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "iso", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hwErrordownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257))
hwErrordownMIB.setRevisions(('2011-08-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwErrordownMIB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hwErrordownMIB.setLastUpdated('201108081000Z')
if mibBuilder.loadTexts: hwErrordownMIB.setOrganization('Huawei Technologies co., Ltd.')
if mibBuilder.loadTexts: hwErrordownMIB.setContactInfo(' R&D NanJing, Huawei Technologies co.,Ltd. NO.101 YuHua Rd., Software District NanJing P.R. China Zip:210001 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwErrordownMIB.setDescription('The HUAWEI-ERRORDOWN-MIB contains objects to Manage configuration and Monitor running state for ERROR-DOWN feature.')
hwErrordownObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1))
hwErrordownNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2))
hwErrordownConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3))
hwErrordownCause = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwErrordownCause.setStatus('current')
if mibBuilder.loadTexts: hwErrordownCause.setDescription('The cause of error-down.')
hwErrordownRecoverType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwErrordownRecoverType.setStatus('current')
if mibBuilder.loadTexts: hwErrordownRecoverType.setDescription('The type of error-down recovery.')
hwErrordown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 1)).setObjects(("IF-MIB", "ifName"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"))
if mibBuilder.loadTexts: hwErrordown.setStatus('current')
if mibBuilder.loadTexts: hwErrordown.setDescription('The event is reported when error-down occur.')
hwErrordownRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 2)).setObjects(("IF-MIB", "ifName"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
if mibBuilder.loadTexts: hwErrordownRecovery.setStatus('current')
if mibBuilder.loadTexts: hwErrordownRecovery.setDescription('The event is reported when error-down recover.')
hwErrordownCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1))
hwErrordowFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1, 1)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordownObjectGroup"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordowFullCompliance = hwErrordowFullCompliance.setStatus('current')
if mibBuilder.loadTexts: hwErrordowFullCompliance.setDescription('This is the Error-down compliance.')
hwErrordownGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2))
hwErrordownObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 1)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordownObjectGroup = hwErrordownObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwErrordownObjectGroup.setDescription('This is the Error-down object group.')
hwErrordownNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 2)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordown"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecovery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordownNotificationGroup = hwErrordownNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwErrordownNotificationGroup.setDescription('This is the Error-down notification group.')
mibBuilder.exportSymbols("HUAWEI-ERRORDOWN-MIB", hwErrordownRecoverType=hwErrordownRecoverType, hwErrordownGroups=hwErrordownGroups, hwErrordownRecovery=hwErrordownRecovery, hwErrordownNotificationGroup=hwErrordownNotificationGroup, hwErrordownMIB=hwErrordownMIB, hwErrordownCause=hwErrordownCause, hwErrordownConformance=hwErrordownConformance, PYSNMP_MODULE_ID=hwErrordownMIB, hwErrordownCompliances=hwErrordownCompliances, hwErrordownObjectGroup=hwErrordownObjectGroup, hwErrordowFullCompliance=hwErrordowFullCompliance, hwErrordownNotifications=hwErrordownNotifications, hwErrordown=hwErrordown, hwErrordownObjects=hwErrordownObjects)
