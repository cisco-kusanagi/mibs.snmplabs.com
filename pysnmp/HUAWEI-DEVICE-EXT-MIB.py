#
# PySNMP MIB module HUAWEI-DEVICE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DEVICE-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, TimeTicks, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, Counter32, IpAddress, Gauge32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "Counter32", "IpAddress", "Gauge32", "Counter64", "ModuleIdentity")
RowStatus, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "DisplayString")
hwDeviceExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188))
hwDeviceExt.setRevisions(('2008-12-17 14:14',))
if mibBuilder.loadTexts: hwDeviceExt.setLastUpdated('200901051414Z')
if mibBuilder.loadTexts: hwDeviceExt.setOrganization('Huawei Technologies Co.,Ltd.')
hwDeviceExtObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1))
hwDeviceEsn = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceEsn.setStatus('current')
hwPlatformName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPlatformName.setStatus('current')
hwPlatformVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPlatformVersion.setStatus('current')
hwProductName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwProductName.setStatus('current')
hwProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwProductVersion.setStatus('current')
hwDeviceExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4))
hwDeviceExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1))
hwDeviceExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1, 1)).setObjects(("HUAWEI-DEVICE-EXT-MIB", "hwDeviceInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceExtCompliance = hwDeviceExtCompliance.setStatus('current')
hwDeviceExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2))
hwDeviceInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2, 1)).setObjects(("HUAWEI-DEVICE-EXT-MIB", "hwDeviceEsn"), ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformName"), ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformVersion"), ("HUAWEI-DEVICE-EXT-MIB", "hwProductName"), ("HUAWEI-DEVICE-EXT-MIB", "hwProductVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceInfoGroup = hwDeviceInfoGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-DEVICE-EXT-MIB", hwPlatformName=hwPlatformName, hwDeviceExtGroups=hwDeviceExtGroups, hwDeviceExtCompliances=hwDeviceExtCompliances, PYSNMP_MODULE_ID=hwDeviceExt, hwDeviceExtCompliance=hwDeviceExtCompliance, hwDeviceExtObject=hwDeviceExtObject, hwProductName=hwProductName, hwDeviceInfoGroup=hwDeviceInfoGroup, hwDeviceExtConformance=hwDeviceExtConformance, hwProductVersion=hwProductVersion, hwDeviceExt=hwDeviceExt, hwPlatformVersion=hwPlatformVersion, hwDeviceEsn=hwDeviceEsn)
