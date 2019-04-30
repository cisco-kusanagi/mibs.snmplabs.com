#
# PySNMP MIB module H3C-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, IpAddress, Unsigned32, Integer32, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, iso, TimeTicks, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Unsigned32", "Integer32", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "iso", "TimeTicks", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55))
h3cObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: h3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: h3cObjectInfo.setOrganization(' Huawei 3Com Technologies Co., Ltd. ')
h3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1))
h3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: h3cObjectInfoTable.setStatus('current')
h3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoOID"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoType"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: h3cObjectInfoEntry.setStatus('current')
h3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: h3cObjectInfoOID.setStatus('current')
h3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: h3cObjectInfoType.setStatus('current')
h3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setStatus('current')
h3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cObjectInfoValue.setStatus('current')
h3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2))
h3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1))
h3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoMIBCompliance = h3cObjectInfoMIBCompliance.setStatus('current')
h3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2))
h3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoTableGroup = h3cObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-OBJECT-INFO-MIB", h3cObjectInfoEntry=h3cObjectInfoEntry, h3cObjectInfo=h3cObjectInfo, h3cObjectInfoTable=h3cObjectInfoTable, h3cObjectInfoType=h3cObjectInfoType, h3cObjectInfoValue=h3cObjectInfoValue, h3cObjectInfoMIBConformance=h3cObjectInfoMIBConformance, h3cObjectInformation=h3cObjectInformation, h3cObjectInfoTypeExtension=h3cObjectInfoTypeExtension, h3cObjectInfoTableGroup=h3cObjectInfoTableGroup, h3cObjectInfoMIBGroups=h3cObjectInfoMIBGroups, h3cObjectInfoMIBCompliances=h3cObjectInfoMIBCompliances, h3cObjectInfoOID=h3cObjectInfoOID, h3cObjectInfoMIBCompliance=h3cObjectInfoMIBCompliance, PYSNMP_MODULE_ID=h3cObjectInfo)
