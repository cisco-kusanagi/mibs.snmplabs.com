#
# PySNMP MIB module HH3C-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Gauge32, iso, ModuleIdentity, IpAddress, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "iso", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 55))
hh3cObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: hh3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: hh3cObjectInfo.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1))
hh3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1), )
if mibBuilder.loadTexts: hh3cObjectInfoTable.setStatus('current')
hh3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1), ).setIndexNames((0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoOID"), (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoType"), (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: hh3cObjectInfoEntry.setStatus('current')
hh3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: hh3cObjectInfoOID.setStatus('current')
hh3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: hh3cObjectInfoType.setStatus('current')
hh3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hh3cObjectInfoTypeExtension.setStatus('current')
hh3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cObjectInfoValue.setStatus('current')
hh3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2))
hh3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1))
hh3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1, 1)).setObjects(("HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cObjectInfoMIBCompliance = hh3cObjectInfoMIBCompliance.setStatus('current')
hh3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2))
hh3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2, 1)).setObjects(("HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cObjectInfoTableGroup = hh3cObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-OBJECT-INFO-MIB", hh3cObjectInfoMIBGroups=hh3cObjectInfoMIBGroups, hh3cObjectInfoEntry=hh3cObjectInfoEntry, hh3cObjectInfoTableGroup=hh3cObjectInfoTableGroup, hh3cObjectInfo=hh3cObjectInfo, hh3cObjectInfoTypeExtension=hh3cObjectInfoTypeExtension, hh3cObjectInfoMIBCompliances=hh3cObjectInfoMIBCompliances, hh3cObjectInfoMIBCompliance=hh3cObjectInfoMIBCompliance, hh3cObjectInfoValue=hh3cObjectInfoValue, hh3cObjectInfoOID=hh3cObjectInfoOID, hh3cObjectInformation=hh3cObjectInformation, hh3cObjectInfoMIBConformance=hh3cObjectInfoMIBConformance, PYSNMP_MODULE_ID=hh3cObjectInfo, hh3cObjectInfoType=hh3cObjectInfoType, hh3cObjectInfoTable=hh3cObjectInfoTable)
