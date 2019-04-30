#
# PySNMP MIB module A3COM-HUAWEI-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Counter64, iso, Unsigned32, ObjectIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter64", "iso", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55))
h3cObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: h3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: h3cObjectInfo.setOrganization(' Huawei 3Com Technologies Co., Ltd. ')
h3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1))
h3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: h3cObjectInfoTable.setStatus('current')
h3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoOID"), (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoType"), (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: h3cObjectInfoEntry.setStatus('current')
h3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: h3cObjectInfoOID.setStatus('current')
h3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: h3cObjectInfoType.setStatus('current')
h3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setStatus('current')
h3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cObjectInfoValue.setStatus('current')
h3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2))
h3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1))
h3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1, 1)).setObjects(("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoMIBCompliance = h3cObjectInfoMIBCompliance.setStatus('current')
h3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2))
h3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2, 1)).setObjects(("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoTableGroup = h3cObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-OBJECT-INFO-MIB", h3cObjectInfoMIBConformance=h3cObjectInfoMIBConformance, h3cObjectInfoEntry=h3cObjectInfoEntry, h3cObjectInfoType=h3cObjectInfoType, h3cObjectInfoValue=h3cObjectInfoValue, h3cObjectInfoOID=h3cObjectInfoOID, h3cObjectInfoTable=h3cObjectInfoTable, h3cObjectInfoMIBCompliance=h3cObjectInfoMIBCompliance, h3cObjectInfoMIBGroups=h3cObjectInfoMIBGroups, h3cObjectInfoTableGroup=h3cObjectInfoTableGroup, h3cObjectInformation=h3cObjectInformation, PYSNMP_MODULE_ID=h3cObjectInfo, h3cObjectInfo=h3cObjectInfo, h3cObjectInfoMIBCompliances=h3cObjectInfoMIBCompliances, h3cObjectInfoTypeExtension=h3cObjectInfoTypeExtension)
