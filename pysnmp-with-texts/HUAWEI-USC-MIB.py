#
# PySNMP MIB module HUAWEI-USC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-USC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Integer32, TimeTicks, Counter32, MibIdentifier, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwUSC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19))
hwUSC.setRevisions(('2014-07-11 16:00', '2010-08-11 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwUSC.setRevisionsDescriptions(('V1.01, initial version.', 'V1.00, initial version.',))
if mibBuilder.loadTexts: hwUSC.setLastUpdated('201407111600Z')
if mibBuilder.loadTexts: hwUSC.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwUSC.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com")
if mibBuilder.loadTexts: hwUSC.setDescription('Please provide the descritpion.')
hwUSCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1))
hwUSCConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1), )
if mibBuilder.loadTexts: hwUSCConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwUSCConfigTable.setDescription('The table describes USC configuration.')
hwUSCConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1), ).setIndexNames((0, "HUAWEI-USC-MIB", "hwUSCPortIndex"))
if mibBuilder.loadTexts: hwUSCConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwUSCConfigEntry.setDescription('Description.')
hwUSCPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUSCPortIndex.setStatus('current')
if mibBuilder.loadTexts: hwUSCPortIndex.setDescription('USC Portindex.')
hwUSCInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCInterfaceName.setStatus('current')
if mibBuilder.loadTexts: hwUSCInterfaceName.setDescription('The name of USC interface.')
hwAuthenControlPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAuthenControlPoint.setStatus('current')
if mibBuilder.loadTexts: hwAuthenControlPoint.setDescription('Control-point status on this interface')
hwUSCLinkDownOffline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCLinkDownOffline.setStatus('current')
if mibBuilder.loadTexts: hwUSCLinkDownOffline.setDescription('The port LinkDownOffline<0 60>, unlimited:65535')
hwUSCControlDownOffline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCControlDownOffline.setStatus('current')
if mibBuilder.loadTexts: hwUSCControlDownOffline.setDescription('The port ControlDownOffline<0 60>, unlimited:65535')
hwUSCUserSyncInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCUserSyncInterval.setStatus('current')
if mibBuilder.loadTexts: hwUSCUserSyncInterval.setDescription('user-sync interval.seconds:60')
hwUSCUserSyncRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCUserSyncRetry.setStatus('current')
if mibBuilder.loadTexts: hwUSCUserSyncRetry.setDescription('user-sync retry.times:5')
mibBuilder.exportSymbols("HUAWEI-USC-MIB", hwUSCPortIndex=hwUSCPortIndex, hwUSCLinkDownOffline=hwUSCLinkDownOffline, hwUSCObjects=hwUSCObjects, hwUSCControlDownOffline=hwUSCControlDownOffline, hwUSCUserSyncInterval=hwUSCUserSyncInterval, hwUSCUserSyncRetry=hwUSCUserSyncRetry, hwUSCConfigTable=hwUSCConfigTable, hwUSCInterfaceName=hwUSCInterfaceName, hwAuthenControlPoint=hwAuthenControlPoint, hwUSCConfigEntry=hwUSCConfigEntry, hwUSC=hwUSC, PYSNMP_MODULE_ID=hwUSC)
