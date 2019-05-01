#
# PySNMP MIB module HUAWEI-DEVICE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DEVICE-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, Integer32, NotificationType, Counter32, Gauge32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "Integer32", "NotificationType", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks")
RowStatus, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString")
hwDeviceExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188))
hwDeviceExt.setRevisions(('2008-12-17 14:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwDeviceExt.setRevisionsDescriptions(('The initial revision of this MIB module .',))
if mibBuilder.loadTexts: hwDeviceExt.setLastUpdated('200901051414Z')
if mibBuilder.loadTexts: hwDeviceExt.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwDeviceExt.setContactInfo('VRP Team Huawei Technologies Co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwDeviceExt.setDescription('The MIB module for collect base device information.')
hwDeviceExtObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1))
hwDeviceEsn = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDeviceEsn.setStatus('current')
if mibBuilder.loadTexts: hwDeviceEsn.setDescription("The equipment serial number of device.Its type is string.If the esn of lr0 is xxx, then the esn of lrn is xxx.ss,ss is the lrn's id.")
hwPlatformName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPlatformName.setStatus('current')
if mibBuilder.loadTexts: hwPlatformName.setDescription('The name of a platform.For example,Huawei Versatile Routing Platform Software.')
hwPlatformVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPlatformVersion.setStatus('current')
if mibBuilder.loadTexts: hwPlatformVersion.setDescription('The version of a platform.For example,VRP (R) Software,Version 3.10.')
hwProductName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwProductName.setStatus('current')
if mibBuilder.loadTexts: hwProductName.setDescription('The name of a product.For example,Quidway NetEngine 5000E.The product name is not equal to the system name. the system name is an instance of the product name.User can config the system name of a device,bot can not change the product name of the device.')
hwProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwProductVersion.setStatus('current')
if mibBuilder.loadTexts: hwProductVersion.setDescription('The version of a product.For example,NE5000E V200R002C01B39L.')
hwDeviceExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4))
hwDeviceExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1))
hwDeviceExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1, 1)).setObjects(("HUAWEI-DEVICE-EXT-MIB", "hwDeviceInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceExtCompliance = hwDeviceExtCompliance.setStatus('current')
if mibBuilder.loadTexts: hwDeviceExtCompliance.setDescription('Compliance statement for agents that provide full support for hwDeviceExt.')
hwDeviceExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2))
hwDeviceInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2, 1)).setObjects(("HUAWEI-DEVICE-EXT-MIB", "hwDeviceEsn"), ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformName"), ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformVersion"), ("HUAWEI-DEVICE-EXT-MIB", "hwProductName"), ("HUAWEI-DEVICE-EXT-MIB", "hwProductVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceInfoGroup = hwDeviceInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwDeviceInfoGroup.setDescription('Group for base device information.')
mibBuilder.exportSymbols("HUAWEI-DEVICE-EXT-MIB", hwDeviceExtGroups=hwDeviceExtGroups, PYSNMP_MODULE_ID=hwDeviceExt, hwPlatformName=hwPlatformName, hwPlatformVersion=hwPlatformVersion, hwProductVersion=hwProductVersion, hwDeviceExtObject=hwDeviceExtObject, hwDeviceEsn=hwDeviceEsn, hwDeviceExtCompliances=hwDeviceExtCompliances, hwDeviceExtCompliance=hwDeviceExtCompliance, hwProductName=hwProductName, hwDeviceInfoGroup=hwDeviceInfoGroup, hwDeviceExt=hwDeviceExt, hwDeviceExtConformance=hwDeviceExtConformance)
