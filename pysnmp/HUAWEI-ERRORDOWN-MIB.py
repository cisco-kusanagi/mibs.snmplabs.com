#
# PySNMP MIB module HUAWEI-ERRORDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ERRORDOWN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, TimeTicks, ObjectIdentity, Integer32, iso, Counter32, Gauge32, MibIdentifier, Unsigned32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hwErrordownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257))
hwErrordownMIB.setRevisions(('2011-08-08 10:00',))
if mibBuilder.loadTexts: hwErrordownMIB.setLastUpdated('201108081000Z')
if mibBuilder.loadTexts: hwErrordownMIB.setOrganization('Huawei Technologies co., Ltd.')
hwErrordownObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1))
hwErrordownNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2))
hwErrordownConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3))
hwErrordownCause = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwErrordownCause.setStatus('current')
hwErrordownRecoverType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwErrordownRecoverType.setStatus('current')
hwErrordown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 1)).setObjects(("IF-MIB", "ifName"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"))
if mibBuilder.loadTexts: hwErrordown.setStatus('current')
hwErrordownRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 2)).setObjects(("IF-MIB", "ifName"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
if mibBuilder.loadTexts: hwErrordownRecovery.setStatus('current')
hwErrordownCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1))
hwErrordowFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1, 1)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordownObjectGroup"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordowFullCompliance = hwErrordowFullCompliance.setStatus('current')
hwErrordownGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2))
hwErrordownObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 1)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordownObjectGroup = hwErrordownObjectGroup.setStatus('current')
hwErrordownNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 2)).setObjects(("HUAWEI-ERRORDOWN-MIB", "hwErrordown"), ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecovery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwErrordownNotificationGroup = hwErrordownNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-ERRORDOWN-MIB", hwErrordownGroups=hwErrordownGroups, hwErrordown=hwErrordown, hwErrordownObjectGroup=hwErrordownObjectGroup, hwErrordownNotifications=hwErrordownNotifications, hwErrordownMIB=hwErrordownMIB, hwErrordownConformance=hwErrordownConformance, hwErrordownCompliances=hwErrordownCompliances, hwErrordownRecoverType=hwErrordownRecoverType, hwErrordownCause=hwErrordownCause, hwErrordownObjects=hwErrordownObjects, hwErrordownRecovery=hwErrordownRecovery, hwErrordownNotificationGroup=hwErrordownNotificationGroup, PYSNMP_MODULE_ID=hwErrordownMIB, hwErrordowFullCompliance=hwErrordowFullCompliance)
